from cmx import doc

from specs.__init__ import get_obs_spec, render_initial, render_video

if __name__ == '__main__':
    doc @ f"""
    ## Twin Box Pick and Place

    Name                        | Observation Spec                          | Goal Init/Comment                                             | 
    -----------------           | ----------------                          | -------                                                       | ------
    **TwinBox-place-single-v0** | {get_obs_spec('fetch:TwinBox-place-single-v0')}  | place a single object at target location               | ![](figures/TwinBox-place-single-v0.gif)
    **TwinBox-red-v0**          | {get_obs_spec('fetch:TwinBox-red-v0')}    | place <span color="red">red</span> block at target location   | ![](figures/TwinBox-red-v0.gif)
    **TwinBox-blue-v0**         | {get_obs_spec('fetch:TwinBox-blue-v0')}   | place <span color="blue">blue</span> block at target location | ![](figures/TwinBox-blue-v0.gif)
    **TwinBox-mixed-v0**        | {get_obs_spec('fetch:TwinBox-mixed-v0')}  | place either one to target location                           | ![](figures/TwinBox-mixed-v0.gif)                     
    **TwinBox-place-v0**        | {get_obs_spec('fetch:TwinBox-place-v0')}  | place both objects to target location                         | ![](figures/TwinBox-place-v0.gif)
    """
    with doc:
        twin_box_envs = ['fetch:TwinBox-place-v0',
                         'fetch:TwinBox-red-v0',
                         'fetch:TwinBox-blue-v0',
                         'fetch:TwinBox-mixed-v0',
                         'fetch:TwinBox-both-v0', ]
    table = doc.table()
    for env_id in twin_box_envs:
        with table.figure_row() as row:
            render_initial(env_id, row)
            render_video(env_id, 15, row)
