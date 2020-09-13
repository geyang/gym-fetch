from gym.envs.registration import register

from .box import BoxEnv
from .bin import BinEnv
from fetch.mixed_envs.box_block import BoxBlockEnv
from .drawer import DrawerEnv
from fetch.mixed_envs.drawer_block import DrawerBlockEnv
from .gym_fetch import GymFetchEnv
from .mixed_envs.box_bin import BoxBinEnv
from .mixed_envs.drawer_bin import DrawerBinEnv
from .mixed_envs.box_bin_drawer import BoxBinDrawerEnv

kwargs = {}
# original gym envs
for action in ['reach', 'push', 'pick-place', 'slide']:
    register(
        # Same as FetchPickAndPlace, with a bin.
        id=f"{action.title().replace('-', '')}-v0",
        entry_point=GymFetchEnv,
        kwargs=dict(action=action, **kwargs),
        max_episode_steps=50,
    )
# Fetch
register(
    # Same as FetchPickAndPlace
    id='Bin-no-bin-v0',
    entry_point=BinEnv,
    kwargs=dict(action='no-bin', **kwargs),
    max_episode_steps=50,
)
register(
    # Same as FetchPickAndPlace
    id='Bin-pp-xml-v0',
    entry_point=BinEnv,
    kwargs=dict(action='pp-xml', **kwargs),
    max_episode_steps=50,
)
register(
    # Same as FetchPickAndPlace, but with a bin in model (not shown)
    id='Bin-no-init-v0',
    entry_point=BinEnv,
    kwargs=dict(action='no-init', **kwargs),
    max_episode_steps=50,
)
register(
    # Bin is welded in-place
    id='Bin-aside-v0',
    entry_point=BinEnv,
    kwargs=dict(action="bin-aside", obs_keys=['object0']),
    max_episode_steps=50,
)
register(
    # Bin is welded in-place
    id='Bin-aside-pos-v0',
    entry_point=BinEnv,
    kwargs=dict(action="bin-aside", obs_keys=['object0', 'bin@pos']),
    max_episode_steps=50,
)
# register(
#     # block is initialized from a fixed location.
#     # todo: deprecate and delete
#     id='Bin-place-fixed-v0',
#     entry_point=BinEnv,
#     kwargs=dict(action="place-fix-block", **kwargs),
#     max_episode_steps=50,
# )
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
