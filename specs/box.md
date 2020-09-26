
write_protected: true
---

# Primitive Tasks

Per our discussion, we want a domain that includes at least 1 complex maneuver 
involving opening up a box/drawer, and placing the block inside. 

## Box Diagnostic Tasks
Name                     | Observation Spec                  | Goal Init/Comment     | 
-----------------        | ----------------                  | -------               | ------
**Box-aside-v0**         | achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (25,)    | box is on the side    | ![](figures/Box-aside-v0.gif)
**Box-fixed-v0**        | achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (25,)     | box is in the middle  | ![](figures/Box-fixed-v0.gif)

## Box Primitive Tasks

Name                     | Observation Spec                    | Goal Init/Comment                  | 
-----------------        | ----------------                    | -------                            | ------
**Box-open-v0**          | achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (25,)       | move lid to specific location      | ![](figures/Box-open-v0.gif)
**Box-close-v0**         | achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (25,)      | pick up lid, place on top of box   | ![](figures/Box-close-v0.gif)
**Box-place-easy-v0**    | achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (43,) | place the block inside an open box | ![](figures/Box-place-easy-v0.gif)
**Box-place-medium-v0**  | achieved_goal: (6,)<br>desired_goal: (6,)<br>observation: (43,) | place the block inside an open box | ![](figures/Box-place-medium-v0.gif)
**Box-place-v0**         | achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (43,)      | need to first open the box         | ![](figures/Box-place-v0.gif)

## Details of Each Task

| **Box-aside-v0** | **distribution** |   |
|:----------------:|:----------------:|:-:|
| ![figures/Box-aside-v0_init.png?ts=749410](figures/Box-aside-v0_init.png?ts=749410) | ![figures/Box-aside-v0_reset.png?ts=843346](figures/Box-aside-v0_reset.png?ts=843346) | ![figures/Box-aside-v0.gif?ts=562655](figures/Box-aside-v0.gif?ts=562655) |
| **Box-fixed-v0** | **distribution** |   |
| ![figures/Box-fixed-v0_init.png?ts=969266](figures/Box-fixed-v0_init.png?ts=969266) | ![figures/Box-fixed-v0_reset.png?ts=043016](figures/Box-fixed-v0_reset.png?ts=043016) | ![figures/Box-fixed-v0.gif?ts=873057](figures/Box-fixed-v0.gif?ts=873057) |
| **Box-open-v0** | **distribution** |   |
| ![figures/Box-open-v0_init.png?ts=354351](figures/Box-open-v0_init.png?ts=354351) | ![figures/Box-open-v0_reset.png?ts=428297](figures/Box-open-v0_reset.png?ts=428297) | ![figures/Box-open-v0.gif?ts=313986](figures/Box-open-v0.gif?ts=313986) |
| **Box-close-v0** | **distribution** |   |
| ![figures/Box-close-v0_init.png?ts=797171](figures/Box-close-v0_init.png?ts=797171) | ![figures/Box-close-v0_reset.png?ts=883028](figures/Box-close-v0_reset.png?ts=883028) | ![figures/Box-close-v0.gif?ts=764764](figures/Box-close-v0.gif?ts=764764) |
| **Box-place-easy-v0** | **distribution** |   |
| ![figures/Box-place-easy-v0_init.png?ts=242643](figures/Box-place-easy-v0_init.png?ts=242643) | ![figures/Box-place-easy-v0_reset.png?ts=309477](figures/Box-place-easy-v0_reset.png?ts=309477) | ![figures/Box-place-easy-v0.gif?ts=209534](figures/Box-place-easy-v0.gif?ts=209534) |
| **Box-place-medium-v0** | **distribution** |   |
| ![figures/Box-place-medium-v0_init.png?ts=152389](figures/Box-place-medium-v0_init.png?ts=152389) | ![figures/Box-place-medium-v0_reset.png?ts=218162](figures/Box-place-medium-v0_reset.png?ts=218162) | ![figures/Box-place-medium-v0.gif?ts=198053](figures/Box-place-medium-v0.gif?ts=198053) |
| **Box-place-v0** | **distribution** |   |
| ![figures/Box-place-v0_init.png?ts=962916](figures/Box-place-v0_init.png?ts=962916) | ![figures/Box-place-v0_reset.png?ts=059942](figures/Box-place-v0_reset.png?ts=059942) | ![figures/Box-place-v0.gif?ts=116958](figures/Box-place-v0.gif?ts=116958) |
