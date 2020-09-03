import os
from gym import utils
from .. import fetch_env


class DrawerBinEnv(fetch_env.FetchEnv, utils.EzPickle):
    def __init__(self, action, reward_type='sparse'):
        initial_qpos = {
            'robot0:slide0': 0.405,
            'robot0:slide1': 0.48,
            'robot0:slide2': 0.0,
            'object0:joint': [1.25, 0.53, 0.4, 1., 0., 0., 0.],
            'drawer:joint': [1.45, 1.1, 0.4, 1, 0., 0., 0.],
            'cabinet:joint': [1.45, 1.1, 1, 1, 0., 0., 0.],
            'bin:joint': [1.25, 0.53, 0.4, 1, 0., 0., 0.],
        }
        fetch_env.FetchEnv.__init__(
            self, "drawer_bin.xml", has_object=True, block_gripper=False, n_substeps=20,
            gripper_extra_height=0.2, target_in_the_air=True, target_offset=0.0,
            obj_range=0.15, target_range=0.15, distance_threshold=0.05,
            initial_qpos=initial_qpos, reward_type=reward_type)
        utils.EzPickle.__init__(self)
