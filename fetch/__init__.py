from gym.envs.registration import register

from .box import BoxEnv
from .bin import BinEnv
from .box_block import BoxBlockEnv
from .drawer import DrawerEnv
from .drawer_block import DrawerBlockEnv
from .mixed_envs.box_bin import BoxBinEnv
from .mixed_envs.drawer_bin import DrawerBinEnv
from .mixed_envs.box_bin_drawer import BoxBinDrawerEnv

kwargs = {}
# Fetch
register(
    id='Bin-v0',
    entry_point=BinEnv,
    kwargs=dict(action=None, **kwargs),
    max_episode_steps=50,
)
register(
    # http://localhost:3001/geyang/latent-planning/
    id='Bin-fixed-v0',
    entry_point=BinEnv,
    kwargs=dict(action="fix-bin", **kwargs),
    max_episode_steps=50,
)
register(
    id='Bin-pick-v0',
    entry_point=BinEnv,
    kwargs=dict(action="pick", **kwargs),
    max_episode_steps=50,
)
register(
    id='Bin-place-v0',
    entry_point=BinEnv,
    kwargs=dict(action="place", **kwargs),
    max_episode_steps=50,
)
register(
    id='Bin-place-fixed-v0',
    entry_point=BinEnv,
    kwargs=dict(action="place-fix-block", **kwargs),
    max_episode_steps=50,
)
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
    id='Box-pick-v0',
    entry_point=BoxBlockEnv,
    kwargs=dict(action="pick", **kwargs),
    max_episode_steps=50,
)
register(
    id='Box-place-v0',
    entry_point=BoxBlockEnv,
    kwargs=dict(action="place", **kwargs),
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
    id='Drawer-pick-v0',
    entry_point=DrawerBlockEnv,
    kwargs=dict(action="pick", **kwargs),
    max_episode_steps=50,
)
register(
    id='Drawer-place-v0',
    entry_point=DrawerBlockEnv,
    kwargs=dict(action="place", **kwargs),
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
