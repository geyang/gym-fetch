from gym.utils import EzPickle
import numpy as np

from fetch import fetch_env

from fetch.fetch_env import assign


class BoxNoLidEnv(fetch_env.FetchEnv, EzPickle):
    def __init__(self,
                 reward_type="sparse",
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
                 goal_sampling=None,
                 freeze_objects=None,
                 initial_qpos=None
                 ):

        obj_keys = 'box', 'object0'
        model_path = "box_no_lid.xml"

        local_vars = locals()
        del local_vars['self']

        fetch_env.FetchEnv.__init__(self, **local_vars)
        EzPickle.__init__(self)

    # def _reset_sim(self):
    #     """
    #     :return: True, Read by the reset function to know this is ready.
    #     """
    #     self.sim.set_state(self.initial_state)
    #
    #     if self.action in ["box-aside", "box-fixed"]:
    #         for obj_key in self.obj_keys:
    #             if obj_key is not 'box':
    #                 self._reset_body(obj_key)
    #
    #         original_pos = self.initial_qpos['box:joint']
    #         original_pos[2] = self.initial_heights['box']
    #         self._reset_body("box", original_pos)
    #
    #     self.sim.forward()
    #     return True

    # def _step_callback(self):
    #     super()._step_callback()
    #     if not self.action:
    #         return
    #     elif self.action in ["box-aside", "box-fixed"]:
    #         # todo: fix the location of the box
    #         original_pos = self.initial_qpos['box:joint']
    #         self._reset_body("box", original_pos[:2])
    #     elif "place" in self.action and self.goal_box_offset is not None:
    #         # if self.np_random.uniform() < 0.1:
    #         self.goal = self.sim.data.get_site_xpos("box")[:3].copy() + self.goal_box_offset

    # goal_box_offset = None

    # def _sample_goal(self):
    #     rdn = self.np_random.uniform()
    #     if self.action == "place" or (self.action == "place+air" and rdn > (self.target_in_the_air or 1)):
    #         # if self.np_random.uniform() < 0.1:
    #         self.goal_box_offset = [*self.np_random.uniform(-0.08, 0.08, size=2), 0.02]
    #         goal = self.sim.data.get_site_xpos("box")[:3].copy() + self.goal_box_offset
    #         return goal
    #     elif self.action == "place+air":
    #         # randomly initialize the target in the air, fix through out episode
    #         self.goal_box_offset = None
    #         goal = self.initial_gripper_xpos[:3] + self.np_random.uniform(-self.target_range, self.target_range, size=3)
    #         # sets the goal to the table top. Change height range to 0.45 to 0.25 to make it easier
    #         goal[2] = self.initial_heights[self.goal_key] + self.np_random.uniform(0, 0.25)
    #         return goal
    #
    #     return super()._sample_goal()
