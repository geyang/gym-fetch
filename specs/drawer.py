from cmx import doc

from specs import get_obs_spec, render_initial, render_video

if __name__ == '__main__':
    debug_envs = ["fetch:Drawer-fixed-v0",
                  "fetch:Drawer-fixed-open-v0", ]

    drawer_envs = ["fetch:Drawer-open-v0",
                   "fetch:Drawer-close-v0",
                   "fetch:Drawer-place-easy-v0",
                   "fetch:Drawer-place-v0", ]
    all_envs = drawer_envs
    doc @ f"""
# Drawer Open and Pick and Place Tasks

## Debugging Tasks

Name                     | Observation Spec                       | Goal Init/Comment                       | 
-----------------        | ----------------                       | -------                                 | ------
**Drawer-fixed-v0**      | {get_obs_spec('Drawer-fixed-v0')}      | Drawer at a fixed location on the desk  | ![](figures/Drawer-fixed-v0.gif)
**Drawer-fixed-open-v0** | {get_obs_spec('Drawer-fixed-open-v0')} | Drawer at the same location, but open. This one<br>occupies a different area closer to the middle. | ![](figures/Drawer-place-v0.gif) 
"""
    table = doc.table()
    for env_id in debug_envs:
        with table.figure_row() as row:
            render_initial(env_id, row)
            render_video(env_id, 15, row)

    doc @ """
## Drawer Primitive Tasks

> **Note**: To test the agent's performance in placing the object into 
> the drawer, we need to fix the target location to the drawer.

Name                     | Observation Spec                       | Goal Init/Comment                       | 
-----------------        | ----------------                       | -------                                 | ------
**Drawer-open-v0**       | {get_obs_spec('Drawer-open-v0')}       | open the drawer                         | ![](figures/Drawer-open-v0.gif)
**Drawer-close-v0**      | {get_obs_spec('Drawer-close-v0')}      | closing the drawer                      | ![](figures/Drawer-close-v0.gif)
**Drawer-place-easy-v0** | {get_obs_spec('Drawer-place-easy-v0')} | Drawer is open to begin with. Same as gym<br> pick and place. Eventually we want to<br>specify goals inside the drawer | ![](figures/Drawer-place-easy-v0.gif)
**Drawer-place-v0**      | {get_obs_spec('Drawer-place-v0')}      | need to first open the drawer, otherwise<br> same as above.               | ![](figures/Drawer-place-v0.gif) 

## Details of Each Task
"""
    table = doc.table()
    for env_id in all_envs:
        with table.figure_row() as row:
            render_initial(env_id, row)
            render_video(env_id, 15, row)

    doc.flush()
