import numpy as np

from gym.envs.robotics import rotations, utils
from .common import robot_env


def goal_distance(goal_a, goal_b):
    assert goal_a.shape == goal_b.shape
    return np.linalg.norm(goal_a - goal_b, axis=-1)


class FetchEnv(robot_env.RobotEnv):
    """Superclass for all Fetch environments.
    """

    def __init__(
            self, model_path, n_substeps, gripper_extra_height, block_gripper,
            target_in_the_air, target_offset, obj_range, target_range,
            distance_threshold, initial_qpos, reward_type,
            obj_keys, goal_key, obs_keys=None,
    ):
        """Initializes a new Fetch environment.

        On initialization, the objects are initialized according to the `init_qpos` dictionary.
        We record the height info to be reused later. We then call `_reset_sim` and `_get_goal`
        on reset.

        Args:
            model_path (string): path to the environments XML file
            n_substeps (int): number of substeps the simulation runs on every call to step
            gripper_extra_height (float): additional height above the table when positioning the gripper
            block_gripper (boolean): whether or not the gripper is blocked (i.e. not movable) or not
            target_in_the_air (boolean): whether or not the target should be in the air above the table or on the table surface
            target_offset (float or array with 3 elements): offset of the target
            obj_range (float): range of a uniform distribution for sampling initial object positions
            target_range (float): range of a uniform distribution for sampling a target
            distance_threshold (float): the threshold after which a goal is considered achieved
            initial_qpos (dict): a dictionary of joint names and values that define the initial configuration
            reward_type ('sparse' or 'dense'): the reward type, i.e. sparse or dense
        """
        self.gripper_extra_height = gripper_extra_height
        self.block_gripper = block_gripper
        self.obj_keys = obj_keys or []
        self.obs_keys = obs_keys
        self.goal_key = goal_key
        self.target_in_the_air = target_in_the_air
        self.target_offset = target_offset
        self.obj_range = obj_range
        self.target_range = target_range
        self.distance_threshold = distance_threshold
        self.reward_type = reward_type

        super().__init__(
            model_path=model_path, n_substeps=n_substeps, n_actions=4,
            initial_qpos=initial_qpos)

    # GoalEnv methods
    # ----------------------------

    def compute_reward(self, achieved_goal, goal, info):
        # Compute distance between goal and the achieved goal.
        d = goal_distance(achieved_goal, goal)
        if self.reward_type == 'sparse':
            return -(d > self.distance_threshold).astype(np.float32)
        else:
            return -d

    # RobotEnv methods
    # ----------------------------

    def _step_callback(self):
        if self.block_gripper:
            self.sim.data.set_joint_qpos('robot0:l_gripper_finger_joint', 0.)
            self.sim.data.set_joint_qpos('robot0:r_gripper_finger_joint', 0.)
            self.sim.forward()

    def _set_action(self, action):
        assert action.shape == (4,)
        action = action.copy()  # ensure that we don't change the action outside of this scope
        pos_ctrl, gripper_ctrl = action[:3], action[3]

        pos_ctrl *= 0.05  # limit maximum change in position
        rot_ctrl = [1., 0., 1., 0.]  # fixed rotation of the end effector, expressed as a quaternion
        gripper_ctrl = np.array([gripper_ctrl, gripper_ctrl])
        assert gripper_ctrl.shape == (2,)
        if self.block_gripper:
            gripper_ctrl = np.zeros_like(gripper_ctrl)
        action = np.concatenate([pos_ctrl, rot_ctrl, gripper_ctrl])

        # Apply action to simulation.
        utils.ctrl_set_action(self.sim, action)
        utils.mocap_set_action(self.sim, action)

    def _get_obs(self):
        # positions
        grip_pos = self.sim.data.get_site_xpos('robot0:grip')
        dt = self.sim.nsubsteps * self.sim.model.opt.timestep
        grip_velp = self.sim.data.get_site_xvelp('robot0:grip') * dt

        robot_qpos, robot_qvel = utils.robot_get_obs(self.sim)
        gripper_state = robot_qpos[-2:]
        gripper_vel = robot_qvel[-2:] * dt  # change to a scalar if the gripper is made symmetric

        obs_stack = grip_pos, gripper_vel, gripper_state, grip_velp,

        for obj_key in self.obs_keys or self.obj_keys:
            object_pos = self.sim.data.get_site_xpos(obj_key)
            object_rot = rotations.mat2euler(self.sim.data.get_site_xmat(obj_key))
            object_velp = self.sim.data.get_site_xvelp(obj_key) * dt
            object_velr = self.sim.data.get_site_xvelr(obj_key) * dt

            # gripper state
            object_rel_pos = object_pos - grip_pos
            object_velp -= grip_velp

            obs_stack += object_pos, object_rot, object_velp, object_velr, object_rel_pos

        achieved_goal = self.sim.data.get_site_xpos(self.goal_key).copy()

        return {
            'observation': np.concatenate(obs_stack).copy(),
            'achieved_goal': achieved_goal.copy(),
            'desired_goal': self.goal.copy(),
        }

    def _viewer_setup(self):
        body_id = self.sim.model.body_name2id('robot0:gripper_link')
        lookat = self.sim.data.body_xpos[body_id]
        for idx, value in enumerate(lookat):
            self.viewer.cam.lookat[idx] = value
        self.viewer.cam.distance = 2.5
        self.viewer.cam.azimuth = 132.
        self.viewer.cam.elevation = -14.

    def _render_callback(self):
        # Visualize target.
        sites_offset = (self.sim.data.site_xpos - self.sim.model.site_pos).copy()
        site_id = self.sim.model.site_name2id('target0')
        self.sim.model.site_pos[site_id] = self.goal - sites_offset[0]
        self.sim.forward()

    def _reset_slide(self, obj_key, slide_pos=None):
        if slide_pos is None:
            ctrl_ind = self.sim.model.joint_names.index(f"{obj_key}:slide")
            low, high = self.sim.model.jnt_range[ctrl_ind]
            slide_pos = self.np_random.uniform(low, high)
        self.sim.data.set_joint_qpos(f'{obj_key}:slide', slide_pos)

    def _reset_body(self, obj_key, pos=None):
        """returns the xy position"""
        current_obj_qpos = self.sim.data.get_joint_qpos(f'{obj_key}:joint').copy()
        assert len(current_obj_qpos) == 7, "should be a single object."
        if pos is not None:
            current_obj_qpos[:len(pos)] = pos
        else:
            obj_xpos = self.initial_gripper_xpos[:2]
            while np.linalg.norm(obj_xpos - self.initial_gripper_xpos[:2]) < 0.1:
                obj_xpos = self.initial_gripper_xpos[:2] \
                           + self.np_random.uniform(-self.obj_range, self.obj_range, size=2)
            current_obj_qpos[:2] = obj_xpos
        current_obj_qpos[2] = self.initial_heights[obj_key]
        self.sim.data.set_joint_qpos(f'{obj_key}:joint', current_obj_qpos)
        return current_obj_qpos

    def _reset_sim(self):
        self.sim.set_state(self.initial_state)
        # Randomize start position. Object in pick and place, gripper in reach.
        if self.obj_keys:
            self._reset_body(self.goal_key)
        self.sim.forward()
        return True

    def _sample_goal(self):
        if self.goal_key == "robot0:grip":
            goal = self.initial_gripper_xpos[:3] + self.np_random.uniform(-self.target_range, self.target_range, size=3)
        else:
            # sets the goal to be where the gripper is.
            goal = self.initial_gripper_xpos[:3] + self.np_random.uniform(-self.target_range, self.target_range, size=3)
            goal += self.target_offset
            # sets the goal to the table top.
            goal[2] = self.initial_heights[self.goal_key]
            if self.target_in_the_air and self.np_random.uniform() < 0.5:
                goal[2] += self.np_random.uniform(0, 0.45)
        return goal

    def _is_success(self, achieved_goal, desired_goal):
        d = goal_distance(achieved_goal, desired_goal)
        return (d < self.distance_threshold).astype(np.float32)

    def _env_setup(self, initial_qpos):
        for name, value in initial_qpos.items():
            # qpos = self.sim.data.get_joint_qpos(name)
            # print(f"{name}: {qpos}")
            self.sim.data.set_joint_qpos(name, value)
        utils.reset_mocap_welds(self.sim)
        self.sim.forward()

        # Move end effector into position.
        gripper_target = np.array([-0.498, 0.005, -0.431 + self.gripper_extra_height]) \
                         + self.sim.data.get_site_xpos('robot0:grip')
        gripper_rotation = np.array([1., 0., 1., 0.])
        self.sim.data.set_mocap_pos('robot0:mocap', gripper_target)
        self.sim.data.set_mocap_quat('robot0:mocap', gripper_rotation)
        for _ in range(10):
            self.sim.step()

        # Extract information for sampling goals.
        self.initial_gripper_xpos = self.sim.data.get_site_xpos('robot0:grip').copy()
        self.initial_heights = {}
        for obj_key in self.obj_keys:
            self.initial_heights[obj_key] = self.sim.data.get_site_xpos(obj_key)[2]

    def render(self, mode='human', width=500, height=500):
        return super(FetchEnv, self).render(mode, width, height)
