import numpy as np
from gym import utils
from fetch import fetch_env


class BoxBlockEnv(fetch_env.FetchEnv, utils.EzPickle):

    def __init__(self, action,
                 block_gripper=False, n_substeps=20,
                 goal_key="object0",
                 gripper_extra_height=0.2, target_in_the_air=0.5, target_offset=0.0,
                 obj_range=0.15, target_range=0.15, distance_threshold=0.05,
                 reward_type='sparse',
                 obj_keys=("box", "lid", "object0"),
                 obs_keys=("box@pos", "lid", "object0")
                 ):
        self.action = action
        self.initial_qpos = {'robot0:slide0': 0.405,
                             'robot0:slide1': 0.48,
                             'robot0:slide2': 0.0,
                             'box:joint': [1.25, 0.53, 0.4, 0, 0., 0., 0.],
                             'object0:joint': [1.25, 0.53, 0.6, 0, 0., 0., 0.],
                             'lid:joint': [1.25, 0.53, 0.8, 0, 0., 0., 0.]}

        if self.action in ["open+place", "open+place+close"]:
            goal_key = "object0", "lid"

        local_vars = locals()
        del local_vars['action']
        del local_vars['self']

        fetch_env.FetchEnv.__init__(self, "box_block.xml", initial_qpos=self.initial_qpos, **local_vars)
        utils.EzPickle.__init__(self)

    def _reset_sim(self):
        """
        :return: True, Read by the reset function to know this is ready.
        """
        self.sim.set_state(self.initial_state)

        obj_pos = lid_pos = box_pos = self._reset_body("box")
        if self.action.startswith('open'):
            lid_pos = self._reset_body("lid", box_pos)
        elif self.action.startswith("close"):
            while np.linalg.norm(lid_pos[:2] - box_pos[:2]) < 0.2:
                lid_pos = self._reset_body("lid")
        if 'place' in self.action:
            while np.linalg.norm(obj_pos[:2] - box_pos[:2]) < 0.2 or np.linalg.norm(obj_pos[:2] - lid_pos[:2]) < 0.2:
                obj_pos = self._reset_body("object0")
        else:
            self._reset_body("object0")
        self.sim.forward()
        return True

    def _step_callback(self):
        super()._step_callback()
        if self.action == "close":
            bin_xpos = self.sim.data.get_site_xpos("box").copy()
            bin_xpos[2] = self.initial_heights['lid']
            self.goal = bin_xpos

    def _sample_open_lid_goal(self):
        xpos = box_xpos = self.sim.data.get_site_xpos("box").copy()
        while np.linalg.norm(xpos - box_xpos) < 0.2:
            xpos = super()._sample_single_goal("lid")
        return xpos

    def _sample_closed_lid_goal(self):
        xpos = self.sim.data.get_site_xpos("box").copy()
        xpos[2] = self.initial_heights['lid']
        return xpos

    def _sample_place_goal(self):
        # assumes that the object is initialized inside the box.
        # if not, add 0.02 to the vertical position
        xpos = self.sim.data.get_site_xpos("box").copy()
        xpos[2] = self.initial_heights['object0']  # + 0.02
        return xpos

    # 重要的事情说三遍！！
    def _sample_goal(self):
        if self.action == "open":
            return self._sample_open_lid_goal()
        elif self.action == "close":
            return self._sample_closed_lid_goal()
        elif self.action == "place":
            return self._sample_place_goal()
        elif self.action == "open+place":
            return {"object0": self._sample_place_goal(), "lid": self._sample_open_lid_goal()}
        elif self.action == "open+place+close":
            return {"object0": self._sample_place_goal(), "lid": self._sample_closed_lid_goal()}
        raise NotImplementedError(f"Support for {self.action} is not implemented")
