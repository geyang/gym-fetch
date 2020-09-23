
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
- [ ] launch extended fetch tasks.

Primitive Tasks               | Observation Spec                            | Goal Init/Comment                   | 
-----------------             | ----------------                            | -------                             | ------
**Box-fixed-open-v0**         | achieved_goal: None<br>desired_goal: None<br>observation: (43,)         | box fixed on the side<br>lift lid.<br>**object target tracks object** | ![](figures/Box-fixed-open-v0.gif)
**Box-fixed-close-v0**        | achieved_goal: None<br>desired_goal: None<br>observation: (43,)        | box fixed on the side<br>close lid.<br>**object target tracks**.  | ![](figures/Box-fixed-close-v0.gif)
**Box-fixed-place-easy-v0**   | achieved_goal: None<br>desired_goal: None<br>observation: (43,)   | box is open and fixed<br>place into the box<br>**lid target trakcs**. | ![](figures/Box-fixed-place-easy-v0.gif)
**Box-fixed-place-medium-v0** | achieved_goal: None<br>desired_goal: None<br>observation: (43,) | Place both the lid and<br>the object to the target location | ![](figures/Box-fixed-place-medium-v0.gif)
**Box-fixed-place-v0**        | achieved_goal: None<br>desired_goal: None<br>observation: (43,)        | place the lid back after<br>placing the object.   | ![](figures/Box-fixed-place-v0.gif)

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
**Box-open-v0**          | achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (25,)       | move lid to specific location      | ![](figures/Box-open-v0.gif)
**Box-close-v0**         | achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (25,)      | pick up lid, place on top of box   | ![](figures/Box-close-v0.gif)
**Box-place-easy-v0**    | achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (43,) | place the block inside an open box | ![](figures/Box-place-easy-v0.gif)
**Box-place-medium-v0**  | achieved_goal: None<br>desired_goal: None<br>observation: (43,) | place the block inside an open box | ![](figures/Box-place-medium-v0.gif)
**Box-place-v0**         | achieved_goal: None<br>desired_goal: None<br>observation: (43,)      | need to first open the box         | ![](figures/Box-place-v0.gif)

## Details of Each Task
| **Box-aside-v0** | **distribution** |   |
|:----------------:|:----------------:|:-:|
| ![figures/Box-aside-v0_init.png?ts=339932](figures/Box-aside-v0_init.png?ts=339932) | ![figures/Box-aside-v0_reset.png?ts=478335](figures/Box-aside-v0_reset.png?ts=478335) | ![figures/Box-aside-v0.gif?ts=737526](figures/Box-aside-v0.gif?ts=737526) |
| **Box-fixed-v0** | **distribution** |   |
| ![figures/Box-fixed-v0_init.png?ts=978948](figures/Box-fixed-v0_init.png?ts=978948) | ![figures/Box-fixed-v0_reset.png?ts=132100](figures/Box-fixed-v0_reset.png?ts=132100) | ![figures/Box-fixed-v0.gif?ts=250342](figures/Box-fixed-v0.gif?ts=250342) |
| **Box-fixed-open-v0** | **distribution** |   |
| ![figures/Box-fixed-open-v0_init.png?ts=306584](figures/Box-fixed-open-v0_init.png?ts=306584) | ![figures/Box-fixed-open-v0_reset.png?ts=393046](figures/Box-fixed-open-v0_reset.png?ts=393046) | ![figures/Box-fixed-open-v0.gif?ts=334035](figures/Box-fixed-open-v0.gif?ts=334035) |
| **Box-fixed-close-v0** | **distribution** |   |
| ![figures/Box-fixed-close-v0_init.png?ts=171727](figures/Box-fixed-close-v0_init.png?ts=171727) | ![figures/Box-fixed-close-v0_reset.png?ts=231937](figures/Box-fixed-close-v0_reset.png?ts=231937) | ![figures/Box-fixed-close-v0.gif?ts=260645](figures/Box-fixed-close-v0.gif?ts=260645) |
| **Box-fixed-place-easy-v0** | **distribution** |   |
| ![figures/Box-fixed-place-easy-v0_init.png?ts=223678](figures/Box-fixed-place-easy-v0_init.png?ts=223678) | ![figures/Box-fixed-place-easy-v0_reset.png?ts=320459](figures/Box-fixed-place-easy-v0_reset.png?ts=320459) | ![figures/Box-fixed-place-easy-v0.gif?ts=463324](figures/Box-fixed-place-easy-v0.gif?ts=463324) |
| **Box-fixed-place-medium-v0** | **distribution** |   |
| ![figures/Box-fixed-place-medium-v0_init.png?ts=604598](figures/Box-fixed-place-medium-v0_init.png?ts=604598) | ![figures/Box-fixed-place-medium-v0_reset.png?ts=852464](figures/Box-fixed-place-medium-v0_reset.png?ts=852464) | ![figures/Box-fixed-place-medium-v0.gif?ts=516032](figures/Box-fixed-place-medium-v0.gif?ts=516032) |
| **Box-fixed-place-v0** | **distribution** |   |
| ![figures/Box-fixed-place-v0_init.png?ts=177709](figures/Box-fixed-place-v0_init.png?ts=177709) | ![figures/Box-fixed-place-v0_reset.png?ts=349920](figures/Box-fixed-place-v0_reset.png?ts=349920) | ![figures/Box-fixed-place-v0.gif?ts=001790](figures/Box-fixed-place-v0.gif?ts=001790) |
