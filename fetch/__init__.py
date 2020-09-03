from .box import BoxEnv
from .bin import BinEnv
from .drawer import DrawerEnv

from gym.envs.registration import register

from .mixed_envs.box_bin import BoxBinEnv
from .mixed_envs.drawer_bin import DrawerBinEnv
from .mixed_envs.box_bin_drawer import BoxBinDrawerEnv

kwargs = {}
# Fetch
register(
    id='Box-open-v0',
    entry_point=BoxEnv,
    kwargs=dict(action="open", **kwargs),
    max_episode_steps=50,
)
register(
    id='Box-close-v0',
    entry_point=BoxEnv,
    kwargs=dict(action="close", **kwargs),
    max_episode_steps=50,
)
register(
    id='Bin-picking-v0',
    entry_point=BinEnv,
    kwargs=dict(action="close", **kwargs),
    max_episode_steps=50,
)
register(
    id='Drawer-open-v0',
    entry_point=DrawerEnv,
    kwargs=dict(action="open", **kwargs),
    max_episode_steps=50,
)
register(
    id='Drawer-close-v0',
    entry_point=DrawerEnv,
    kwargs=dict(action="close", **kwargs),
    max_episode_steps=50,
)
register(
    id='BoxBin-v0',
    entry_point=BoxBinEnv,
    kwargs=dict(action=None, **kwargs),
    max_episode_steps=50,
)
register(
    id='DrawerBin-v0',
    entry_point=DrawerBinEnv,
    kwargs=dict(action=None, **kwargs),
    max_episode_steps=50,
)
register(
    id='BoxBinDrawer-v0',
    entry_point=BoxBinDrawerEnv,
    kwargs=dict(action=None, **kwargs),
    max_episode_steps=50,
)
