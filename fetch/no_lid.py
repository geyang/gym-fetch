import os
from gym.utils import EzPickle
from . import fetch_env
import numpy as np


class BoxNoLidEnv(fetch_env.FetchEnv, EzPickle):
    def __init__(self, action, reward_type="sparse",
                 obs_keys=("object0",),
                 goal_key="object0",
                 block_gripper=False,
                 n_substeps=20,
                 gripper_extra_height=0.2,
                 target_in_the_air=0.5,
                 target_offset=0.0,
                 obj_range=0.15,
                 target_range=0.15,
                 distance_threshold=0.05,
                 ):

        self.action = action
        self.initial_qpos = {
            'robot0:slide0': 0.405,
            'robot0:slide1': 0.48,
            'robot0:slide2': 0.0,
        }
        # todo: add uniform distribution to box location in box-aside mode.
        if action == "box-aside":
            self.initial_qpos['box:joint'] = [1.25, 0.33, 0.6, 0, 0., 0., 0.]
            self.initial_qpos['object0:joint'] = [1.25, 0.53, 0.6, 0, 0., 0., 0.]
        elif action == "box-fixed":
            self.initial_qpos['box:joint'] = [1.1, 0.75, 0.6, 0, 0., 0., 0.]
            self.initial_qpos['object0:joint'] = [1.25, 0.75, 0.6, 0, 0., 0., 0.]
        elif action in ["pick", "place", "place+air"]:
            self.initial_qpos['box:joint'] = [1.25, 0.50, 0.6, 0, 0., 0., 0.]
            self.initial_qpos['object0:joint'] = [1.25, 0.75, 0.6, 0, 0., 0., 0.]

        obj_keys = 'box', 'object0'
        model_path = "box_no_lid.xml"

        local_vars = locals()
        del local_vars['action']
        del local_vars['self']

        fetch_env.FetchEnv.__init__(self, initial_qpos=self.initial_qpos, **local_vars)
        EzPickle.__init__(self)

    def _reset_sim(self):
        """
        :return: True, Read by the reset function to know this is ready.
        """
        self.sim.set_state(self.initial_state)

        if self.action in ["box-aside", "box-fixed"]:
            for obj_key in self.obj_keys:
                if obj_key is not 'box':
                    self._reset_body(obj_key)

            original_pos = self.initial_qpos['box:joint']
            original_pos[2] = self.initial_heights['box']
            self._reset_body("box", original_pos)
        elif self.action == "pick":
            box_xpos = self._reset_body('box').copy()
            # randomize relative position
            box_xpos[:2] += self.np_random.uniform(-0.08, 0.08, size=2)
            # Δh when block is on the box
            box_xpos[2] = self.initial_heights['object0'] + 0.02
            self._reset_body('object0', box_xpos)
        elif "place" in self.action:
            obj_xpos = box_xpos = self._reset_body('box')[:2].copy()
            # randomize relative position
            while np.linalg.norm(obj_xpos - box_xpos) < 0.2:
                obj_xpos = self._reset_body('object0')[:2]
        else:
            for obj_key in self.obj_keys:
                self._reset_body(obj_key)

        self.sim.forward()
        return True

    def _step_callback(self):
        super()._step_callback()
        if not self.action:
            return
        elif self.action in ["box-aside", "box-fixed"]:
            # todo: fix the location of the box
            original_pos = self.initial_qpos['box:joint']
            original_pos[2] = self.initial_heights['box']
            self._reset_body("box", original_pos)
        elif "place" in self.action and self.goal_box_offset is not None:
            # if self.np_random.uniform() < 0.1:
            self.goal = self.sim.data.get_site_xpos("box")[:3].copy() + self.goal_box_offset

    goal_box_offset = None

    def _sample_goal(self):
        rdn = self.np_random.uniform()
        if self.action == "place" or (self.action == "place+air" and rdn > (self.target_in_the_air or 1)):
            # if self.np_random.uniform() < 0.1:
            self.goal_box_offset = [*self.np_random.uniform(-0.08, 0.08, size=2), 0.02]
            goal = self.sim.data.get_site_xpos("box")[:3].copy() + self.goal_box_offset
            return goal
        elif self.action == "place+air":
            # randomly initialize the target in the air, fix through out episode
            self.goal_box_offset = None
            goal = self.initial_gripper_xpos[:3] + self.np_random.uniform(-self.target_range, self.target_range, size=3)
            # sets the goal to the table top. Change height range to 0.45 to 0.25 to make it easier
            goal[2] = self.initial_heights[self.goal_key] + self.np_random.uniform(0, 0.25)
            return goal

        return super()._sample_goal()
