from cmx import doc

from specs.__init__ import get_obs_spec, render_initial, render_video

if __name__ == '__main__':
    doc @ f"""
    write_protected: true
    ---

    # Primitive Tasks

    ## Box Diagnostic Tasks

    | Name                     | Observation Spec                  | Goal Init/Comment     |                                |
    | -----------------        | ----------------                  | -------               | ------                         |
    | **Box-fixed-v0**         | {get_obs_spec('Box-fixed-v0')}    | box is in the middle  | ![](figures/Box-fixed-v0.gif)  |
    | **Box-aside-v0**         | {get_obs_spec('Box-aside-v0')}    | box is on the side    | ![](figures/Box-aside-v0.gif)  |
                                                                                                                                                       
    ## New Latent Planning Tasks                                                                                                                      
                                                                                                                                                        
    | Name                         | Observation Spec                            | Goal Init/Comment     |                                            |
    | -----------------            | ----------------                            | -------               | ------                                     |
    | **Box-fixed-place-train-v0** | {get_obs_spec('Box-fixed-place-train-v0')}  | box is on the side    | ![](figures/Box-fixed-place-train-v0.gif)  |
    | **Box-fixed-place-v0**       | {get_obs_spec('Box-fixed-place-v0')}        | box is on the side    | ![](figures/Box-fixed-place-v0.gif)        |
    | **Box-aside-place-train-v0** | {get_obs_spec('Box-aside-place-train-v0')}  | box is on the side    | ![](figures/Box-aside-place-train-v0.gif)  |
    | **Box-aside-place-v0**       | {get_obs_spec('Box-aside-place-v0')}        | box is on the side    | ![](figures/Box-aside-place-v0.gif)        |

    ## Details of Each Task
    """
    with doc:
        box_envs = ['fetch:Box-aside-v0',
                    'fetch:Box-fixed-v0',
                    'fetch:Box-aside-place-train-v0',
                    'fetch:Box-aside-place-v0',
                    'fetch:Box-fixed-place-train-v0',
                    'fetch:Box-fixed-place-v0']
    table = doc.table()
    for env_id in box_envs:
        with table.figure_row() as row:
            render_initial(env_id, row)
            render_video(env_id, 15, row)

    doc.flush()
