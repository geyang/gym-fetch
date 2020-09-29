from gym import utils
from fetch import fetch_env


def assign(d, *objs):
    for o in objs:
        d.update(o)
    return d


class CleanTable(fetch_env.FetchEnv, utils.EzPickle):

    def __init__(self,
                 block_gripper=False, n_substeps=20,
                 gripper_extra_height=0.2, target_in_the_air=0.5, target_offset=0.0,
                 obj_range=0.15, target_range=0.15, distance_threshold=0.05,
                 reward_type='sparse',
                 obj_keys=("box", "object0", "object1"),
                 obs_keys=("box@pos", "object0", "object1"),
                 goal_key=["object0", "object1"],
                 initial_qpos=None,
                 obj_reset=None,
                 goal_sampling=None,
                 freeze_objects=['box'],
                 ):

        initial_qpos = assign({'box:joint': [1.1, 0.75, 0.4, 0, 0., 0., 0.],
                               'object0:joint': [1.1, 0.75, 0.5, 0, 0., 0., 0.],
                               'object1:joint': [1.1, 0.75, 0.6, 0, 0., 0., 0.], }, initial_qpos or {})

        local_vars = locals()

        del local_vars['self']

        fetch_env.FetchEnv.__init__(self, "clean_table.xml", **local_vars)
        utils.EzPickle.__init__(self)
