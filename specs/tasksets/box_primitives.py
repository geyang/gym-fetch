from cmx import doc

from specs.__init__ import get_obs_spec, render_initial, render_video

if __name__ == '__main__':
    doc @ f"""
    write_protected: true
    ---

    # Box Single Task Taskset
    
    ## Simple Goal Distributions

    The goal distribution of these tasks are pure. Tasks with `place` postfix have the goal
    initialized at the center of the box, whereas the other two uses the goal distribution
    from standard gym `FetchPickAndPlace-v1` environment.
    
    | Name                     | Observation Spec                      | Goal Init/Comment     |                                |
    | -----------------        | ----------------                      | -------               | ------                         |
    | **Box-fixed-v0**         | {get_obs_spec('Box-fixed-v0')}        | box is in the middle  | ![](figures/Box-fixed-v0.gif)  |
    | **Box-aside-v0**         | {get_obs_spec('Box-aside-v0')}        | box is on the side    | ![](figures/Box-aside-v0.gif)  |
    | **Box-fixed-place-v0**   | {get_obs_spec('Box-fixed-place-v0')}  | box is on the side    | ![](figures/Box-fixed-place-v0.gif)        |
    | **Box-aside-place-v0**   | {get_obs_spec('Box-aside-place-v0')}  | box is on the side    | ![](figures/Box-aside-place-v0.gif)        |
                                                                                                                                                       
    ## Mixture Goal Distributions
    
    These two training environments uses a mixture of 20/80% of pick-and-place distribution vs target inside the box.

    | Name                         | Observation Spec                            | Goal Init/Comment     |                                            |
    | -----------------            | ----------------                            | -------               | ------                                     |
    | **Box-fixed-place-train-v0** | {get_obs_spec('Box-fixed-place-train-v0')}  | box is on the side    | ![](figures/Box-fixed-place-train-v0.gif)  |
    | **Box-aside-place-train-v0** | {get_obs_spec('Box-aside-place-train-v0')}  | box is on the side    | ![](figures/Box-aside-place-train-v0.gif)  |

    ## Details of Each Task
    """
    with doc:
        box_envs = ['fetch:Box-aside-v0',
                    'fetch:Box-aside-place-v0',
                    'fetch:Box-aside-place-train-v0',
                    'fetch:Box-fixed-v0',
                    'fetch:Box-fixed-place-v0',
                    'fetch:Box-fixed-place-train-v0']
    table = doc.table()
    for env_id in box_envs:
        with table.figure_row() as row:
            render_initial(env_id, row)
            render_video(env_id, 15, row)

    doc.flush()
