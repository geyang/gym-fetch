from cmx import doc

from specs.__init__ import get_obs_spec, render_initial, render_video

box_envs = ["fetch:Box-aside-v0",
            "fetch:Box-fixed-v0",
            # Box Environments
            "fetch:Box-open-v0",
            "fetch:Box-close-v0",
            "fetch:Box-place-easy-v0",
            "fetch:Box-place-medium-v0",
            "fetch:Box-place-v0", ]

if __name__ == '__main__':
    all_envs = box_envs
    doc @ f"""
write_protected: true
---

# Primitive Tasks

Per our discussion, we want a domain that includes at least 1 complex maneuver 
involving opening up a box/drawer, and placing the block inside. 

## Box Diagnostic Tasks
Name                     | Observation Spec                  | Goal Init/Comment     | 
-----------------        | ----------------                  | -------               | ------
**Box-aside-v0**         | {get_obs_spec('Box-aside-v0')}    | box is on the side    | ![](figures/Box-aside-v0.gif)
**Box-fixed-v0**        | {get_obs_spec('Box-fixed-v0')}     | box is in the middle  | ![](figures/Box-fixed-v0.gif)

## Box Primitive Tasks

Name                     | Observation Spec                    | Goal Init/Comment                  | 
-----------------        | ----------------                    | -------                            | ------
**Box-open-v0**          | {get_obs_spec('Box-open-v0')}       | move lid to specific location      | ![](figures/Box-open-v0.gif)
**Box-close-v0**         | {get_obs_spec('Box-close-v0')}      | pick up lid, place on top of box   | ![](figures/Box-close-v0.gif)
**Box-place-easy-v0**    | {get_obs_spec('Box-place-easy-v0')} | place the block inside an open box | ![](figures/Box-place-easy-v0.gif)
**Box-place-medium-v0**  | {get_obs_spec('Box-place-medium-v0')} | place the block inside an open box | ![](figures/Box-place-medium-v0.gif)
**Box-place-v0**         | {get_obs_spec('Box-place-v0')}      | need to first open the box         | ![](figures/Box-place-v0.gif)

## Details of Each Task
"""
    table = doc.table()
    for env_id in all_envs:
        with table.figure_row() as row:
            render_initial(env_id, row)
            render_video(env_id, 15, row)

    doc.flush()
