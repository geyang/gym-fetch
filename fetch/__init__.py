from .box import BoxEnv
from .bin import BinEnv
from .drawer import DrawerEnv

from gym.envs.registration import register

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
