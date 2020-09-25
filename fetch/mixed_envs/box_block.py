import numpy as np
from gym import utils
from fetch import fetch_env
from typing import Sequence


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
                             'box:joint': [1.15, 0.53, 0.4, 0, 0., 0., 0.],
                             'object0:joint': [1.15, 0.53, 0.6, 0, 0., 0., 0.],
                             'lid:joint': [1.15, 0.53, 0.8, 0, 0., 0., 0.]}

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

        # -----  Box Initialization ------
        if "box-fixed" in self.action:
            original_pos = self.initial_qpos['box:joint']
            original_pos[2] = self.initial_heights['box']
            obj_pos = lid_pos = box_pos = self._reset_body("box", original_pos)
        else:
            obj_pos = lid_pos = box_pos = self._reset_body("box")

        # lid init
        if self.action.startswith('open'):
            lid_pos = self._reset_body("lid", box_pos)
        # elif self.action.startswith("close"):
        else:
            while np.linalg.norm(lid_pos[:2] - box_pos[:2]) < 0.1:
                lid_pos = self._reset_body("lid", h=self.initial_heights['object0'])

        # object init
        if 'place' in self.action:
            # when both set to 0.2, initialization can lock in a dead loop forever.
            while np.linalg.norm(obj_pos[:2] - box_pos[:2]) < 0.1 or np.linalg.norm(obj_pos[:2] - lid_pos[:2]) < 0.1:
                obj_pos = self._reset_body("object0")
        else:
            self._reset_body("object0")
        self.sim.forward()
        return True

    def _step_callback(self):
        super()._step_callback()

        if not isinstance(self.goal_key, str):

            action, *fixed = self.action.split("@")
            goal = {}
            if action in ["open", "close"]:
                goal['object0'] = self.sim.data.get_site_xpos("object0").copy()
            if action in "close":
                goal['lid'] = self.sim.data.get_site_xpos("box").copy()
                goal['lid'][2] = self.initial_heights['lid']
            if action == "place":
                goal['lid'] = self.sim.data.get_site_xpos("lid").copy()
                goal['object0'] = self.sim.data.get_site_xpos("box").copy()
                goal['object0'][2] = self.initial_heights['object0']

            self.goal.update(goal)

        if "box-fixed" in self.action:
            original_pos = self.initial_qpos['box:joint']
            original_pos[2] = self.initial_heights['box']
            self._reset_body("box", original_pos)

    def _sample_open_lid_goal(self):
        xpos = box_xpos = self.sim.data.get_site_xpos("box").copy()
        while np.linalg.norm(xpos - box_xpos) < 0.2:
            xpos = super()._sample_single_goal("lid")  # 50% in the air.
        return xpos

    def _sample_closed_lid_goal(self):
        xpos = self.sim.data.get_site_xpos("box").copy()
        xpos[2] = self.initial_heights['lid']
        return xpos

    # not currently used
    def _sample_table_lid_goal(self):
        # todo: needs attention: is the height correct, and is the range okay?
        xpos = box_xpos = self.sim.data.get_site_xpos("box").copy()
        while np.linalg.norm(xpos - box_xpos) < 0.2:
            xpos = super()._sample_single_goal(h=0.404)
        return xpos

    def _sample_place_goal(self):
        # Place means placing into the box.
        # assumes that the object is initialized inside the box.
        # if not, add 0.02 to the vertical position.
        xpos = self.sim.data.get_site_xpos("box").copy()
        xpos[2] = self.initial_heights['object0']  # + 0.02
        return xpos

    # 重要的事情说三遍！！
    def _sample_goal(self):
        action, *fixed = self.action.split('@')
        if action == "open":
            if isinstance(self.goal_key, str):
                return self._sample_open_lid_goal()
            else:  # track the other object.
                return {"object0": self.sim.data.get_site_xpos("box").copy(),
                        "lid": self._sample_open_lid_goal()}
        elif action == "close":
            if isinstance(self.goal_key, str):
                return self._sample_closed_lid_goal()
            else:  # track the other object.
                return {"object0": self.sim.data.get_site_xpos("box").copy(),
                        "lid": self._sample_closed_lid_goal()}
        elif action == "place":
            if isinstance(self.goal_key, str):
                return self._sample_place_goal()
            else:  # track the other object.
                return {"object0": self._sample_place_goal(),
                        "lid": self.sim.data.get_site_xpos("lid").copy()}
        elif action == "open+place":
            return {"object0": self._sample_place_goal(),
                    "lid": self._sample_open_lid_goal()}
        elif action == "open+place+close":
            return {"object0": self._sample_place_goal(),
                    "lid": self._sample_closed_lid_goal()}
        raise NotImplementedError(f"Support for {self.action} is not implemented")
