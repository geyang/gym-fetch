from cmx import doc

from specs.__init__ import get_obs_spec, render_initial, render_video

box_envs = ["fetch:Box-aside-v0",
            "fetch:Box-fixed-v0",
            # Box Environments
            # "fetch:Box-open-v0",
            # "fetch:Box-close-v0",
            # "fetch:Box-place-easy-v0",
            # "fetch:Box-place-medium-v0",
            # "fetch:Box-place-v0",
            "fetch:Box-fixed-open-v0",
            "fetch:Box-fixed-close-v0",
            "fetch:Box-fixed-place-easy-v0",
            "fetch:Box-fixed-place-medium-v0",
            "fetch:Box-fixed-place-v0", ]

if __name__ == '__main__':
    all_envs = box_envs
    doc @ f"""
write_protected: true
---
# Latent Planning Task Suite

This task suite includes two sets of tasks: **box open and place**, **twin box pick and place**. 
Each task set is composed of a few manipulation primitives, and one (or a few) complex tasks
that require stitching together the primitives in order to succeed. The goal space is composed
of multiple objects, for example both a goal location for the object and the lid. The original 
hindsight experience replay has trouble with learning these complex tasks.

## Complex Box Pick and Place

- [x] which base env class to choose? `BoxBlockEnv`.
- [x] what would be the action type? `open+place` for the `test` environment, mixed for the training env.
- [x] register new env
- [x] implement
- [x] launch extended fetch tasks.

Primitive Tasks               | Observation Spec                            | Goal Init/Comment                   | 
-----------------             | ----------------                            | -------                             | ------
**Box-fixed-open-v0**         | {get_obs_spec('Box-fixed-open-v0')}         | box fixed on the side<br>lift lid.<br>**object target tracks object** | ![](figures/Box-fixed-open-v0.gif)
**Box-fixed-close-v0**        | {get_obs_spec('Box-fixed-close-v0')}        | box fixed on the side<br>close lid.<br>**object target tracks**.  | ![](figures/Box-fixed-close-v0.gif)
**Box-fixed-place-easy-v0**   | {get_obs_spec('Box-fixed-place-easy-v0')}   | box is open and fixed<br>place into the box<br>**lid target trakcs**. | ![](figures/Box-fixed-place-easy-v0.gif)
**Box-fixed-place-medium-v0** | {get_obs_spec('Box-fixed-place-medium-v0')} | Place both the lid and<br>the object to the target location | ![](figures/Box-fixed-place-medium-v0.gif)
**Box-fixed-place-v0**        | {get_obs_spec('Box-fixed-place-v0')}        | place the lid back after<br>placing the object.   | ![](figures/Box-fixed-place-v0.gif)

### Primitive Tasks
### Complex Task

## Twin Box Pick and Place

### Primitive Tasks
### Complex Task

Per our discussion, we want a domain that includes at least 1 complex maneuver 
involving opening up a box/drawer, and placing the block inside. 

## Box Diagnostic Tasks

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
    doc.flush()

    table = doc.table()
    for env_id in all_envs:
        with table.figure_row() as row:
            render_initial(env_id, row)
            render_video(env_id, 15, row)

    doc.flush()
