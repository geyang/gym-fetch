import gym

all_envs = [
    "fetch:Bin-picking-v0",
    "fetch:Box-open-v0",
    "fetch:Box-close-v0",
    "fetch:Drawer-open-v0",
    "fetch:Drawer-close-v0",
    "fetch:DrawerBin-v0",
    "fetch:BoxBin-v0",
    "fetch:BoxBinDrawer-v0",
]


def test_all():
    for env_id in all_envs:
        env = gym.make(env_id)
        env.reset()
        env.close()

        assert env, f"{env}"
