from cmx import doc

from specs.__init__ import get_obs_spec, render_initial, render_video

if __name__ == '__main__':
    doc @ f"""
    ## Task: Cleaning Table

    **Primitives**
    1. place A into box, both on table.
    2. place B into box, with A already inside the box.

    **Training Mixture**: 1 + 2, 50:50.

    **Test**: Both A and B on table, and place both into the box. (edited) 

    Name               | Observation Spec                 | Goal Init/Comment                        | 
    -----------------  | ----------------                 | -------                                  | ------
    **Clean-i-v0**     | {get_obs_spec('Clean-i-v0')}     | place the first object<br>into the box | ![](figures/Clean-i-v0.gif)
    **Clean-ii-v0**    | {get_obs_spec('Clean-ii-v0')}    | place the second object<br>into the box while the<br>first one is already in there. | ![](figures/Clean-ii-v0.gif)
    **Clean-train-v0** | {get_obs_spec('Clean-train-v0')} | 50/50 mixture of both | ![](figures/Clean-train-v0.gif)
    **Clean-v0**       | {get_obs_spec('Clean-v0')}       | Start with both on the<br>table, place both into<br>the box. | ![](figures/Clean-v0.gif)
    """
    with doc:
        twin_box_envs = [
            'fetch:Clean-i-v0',
            'fetch:Clean-ii-v0',
            'fetch:Clean-train-v0',
            'fetch:Clean-v0',
            'fetch:Clean-aside-i-v0',
            'fetch:Clean-aside-ii-v0',
            'fetch:Clean-aside-train-v0',
            'fetch:Clean-aside-v0',
        ]

    table = doc.table()
    for env_id in twin_box_envs:
        with table.figure_row() as row:
            render_initial(env_id, row)
            render_video(env_id, 15, row)

    doc.flush()