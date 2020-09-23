from cmx import doc

from specs.__init__ import get_obs_spec, render_initial, render_video

if __name__ == '__main__':
    doc @ """
    ## Twin Box Pick and Place

    Name                     | Observation Spec                    | Goal Init/Comment                  | 
    -----------------        | ----------------                    | -------                            | ------
    **Box-open-v0**          | {get_obs_spec('Box-open-v0')}       | move lid to specific location      | ![](figures/Box-open-v0.gif)
    **Box-close-v0**         | {get_obs_spec('Box-close-v0')}      | pick up lid, place on top of box   | ![](figures/Box-close-v0.gif)
    **Box-place-easy-v0**    | {get_obs_spec('Box-place-easy-v0')} | place the block inside an open box | ![](figures/Box-place-easy-v0.gif)
    **Box-place-medium-v0**  | {get_obs_spec('Box-place-medium-v0')} | place the block inside an open box | ![](figures/Box-place-medium-v0.gif)
    **Box-place-v0**         | {get_obs_spec('Box-place-v0')}      | need to first open the box         | ![](figures/Box-place-v0.gif)
    """
    with doc:
        twin_box_envs = ["fetch:TwinBox-place-v0",
                         "fetch:TwinBox-pick-v0",
                         "fetch:TwinBox-place-easy-v0",
                         "fetch:TwinBox-place-medium-v0",
                         "fetch:TwinBox-place-v0", ]
    table = doc.table()
    for env_id in twin_box_envs:
        with table.figure_row() as row:
            render_initial(env_id, row)
            render_video(env_id, 15, row)
