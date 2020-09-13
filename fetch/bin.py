import os
from gym.utils import EzPickle
from . import fetch_env
import numpy as np


class BinEnv(fetch_env.FetchEnv, EzPickle):
    def __init__(self, action, reward_type="sparse",
                 obs_keys=("object0",),
                 goal_key="object0",
                 block_gripper=False,
                 n_substeps=20,
                 gripper_extra_height=0.2,
                 target_in_the_air=True,
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
        if action == "no-bin" or action == "no-init":
            pass
        elif action == "bin-aside":
            self.initial_qpos['bin:joint'] = [1.25, 0.33, 0.6, 0, 0., 0., 0.]

        self.initial_qpos['object0:joint'] = [1.25, 0.53, 0.6, 0, 0., 0., 0.]
        if action == "no-bin":
            obj_keys = "object0",
            model_path = "bin_null.xml"
        elif action == "pp-xml":
            obj_keys = "object0",
            model_path = "pick_place.xml"
        else:
            obj_keys = 'bin', 'object0'
            model_path = "bin.xml"

        local_vars = locals()
        del local_vars['action']
        del local_vars['self']

        fetch_env.FetchEnv.__init__(self, **local_vars)
        EzPickle.__init__(self)

    def _reset_sim(self):
        """
        :return: True, Read by the reset function to know this is ready.
        """
        self.sim.set_state(self.initial_state)

        for obj_key in self.obj_keys:
            self._reset_body(obj_key)
        if self.action == "bin-aside":
            # todo: fix the location of the bin
            original_pos = self.initial_qpos['bin:joint']
            original_pos[2] = self.initial_heights['bin']
            self._reset_body("bin", original_pos)
        self.sim.forward()
        return True

    def _step_callback(self):
        super()._step_callback()
        if not self.action:
            return
        elif self.action == "bin-aside":
            # todo: fix the location of the bin
            original_pos = self.initial_qpos['bin:joint']
            original_pos[2] = self.initial_heights['bin']
            self._reset_body("bin", original_pos)
