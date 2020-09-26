
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
**Box-place-medium-v0**  | achieved_goal:<br>&nbsp;&nbsp;&nbsp;&nbsp;lid: (3,)<br>&nbsp;&nbsp;&nbsp;&nbsp;object0: (3,)<br>desired_goal:<br>&nbsp;&nbsp;&nbsp;&nbsp;lid: (3,)<br>&nbsp;&nbsp;&nbsp;&nbsp;object0: (3,)<br>observation: (43,) | place the block inside an open box | ![](figures/Box-place-medium-v0.gif)
**Box-place-v0**         | achieved_goal:<br>&nbsp;&nbsp;&nbsp;&nbsp;lid: (3,)<br>&nbsp;&nbsp;&nbsp;&nbsp;object0: (3,)<br>desired_goal:<br>&nbsp;&nbsp;&nbsp;&nbsp;lid: (3,)<br>&nbsp;&nbsp;&nbsp;&nbsp;object0: (3,)<br>observation: (43,)      | need to first open the box         | ![](figures/Box-place-v0.gif)

## Details of Each Task

| **Box-aside-v0** | **distribution** |   |
|:----------------:|:----------------:|:-:|
| ![figures/Box-aside-v0_init.png?ts=944004](figures/Box-aside-v0_init.png?ts=944004) | ![figures/Box-aside-v0_reset.png?ts=054440](figures/Box-aside-v0_reset.png?ts=054440) | ![figures/Box-aside-v0.gif?ts=986759](figures/Box-aside-v0.gif?ts=986759) |
| **Box-fixed-v0** | **distribution** |   |
| ![figures/Box-fixed-v0_init.png?ts=757403](figures/Box-fixed-v0_init.png?ts=757403) | ![figures/Box-fixed-v0_reset.png?ts=842749](figures/Box-fixed-v0_reset.png?ts=842749) | ![figures/Box-fixed-v0.gif?ts=319363](figures/Box-fixed-v0.gif?ts=319363) |
| **Box-open-v0** | **distribution** |   |
| ![figures/Box-open-v0_init.png?ts=143898](figures/Box-open-v0_init.png?ts=143898) | ![figures/Box-open-v0_reset.png?ts=197544](figures/Box-open-v0_reset.png?ts=197544) | ![figures/Box-open-v0.gif?ts=340640](figures/Box-open-v0.gif?ts=340640) |
| **Box-close-v0** | **distribution** |   |
| ![figures/Box-close-v0_init.png?ts=212386](figures/Box-close-v0_init.png?ts=212386) | ![figures/Box-close-v0_reset.png?ts=299787](figures/Box-close-v0_reset.png?ts=299787) | ![figures/Box-close-v0.gif?ts=263764](figures/Box-close-v0.gif?ts=263764) |
| **Box-place-easy-v0** | **distribution** |   |
| ![figures/Box-place-easy-v0_init.png?ts=028538](figures/Box-place-easy-v0_init.png?ts=028538) | ![figures/Box-place-easy-v0_reset.png?ts=121860](figures/Box-place-easy-v0_reset.png?ts=121860) | ![figures/Box-place-easy-v0.gif?ts=712006](figures/Box-place-easy-v0.gif?ts=712006) |
| **Box-place-medium-v0** | **distribution** |   |
| ![figures/Box-place-medium-v0_init.png?ts=345219](figures/Box-place-medium-v0_init.png?ts=345219) | ![figures/Box-place-medium-v0_reset.png?ts=412982](figures/Box-place-medium-v0_reset.png?ts=412982) | ![figures/Box-place-medium-v0.gif?ts=821978](figures/Box-place-medium-v0.gif?ts=821978) |
| **Box-place-v0** | **distribution** |   |
| ![figures/Box-place-v0_init.png?ts=419282](figures/Box-place-v0_init.png?ts=419282) | ![figures/Box-place-v0_reset.png?ts=493567](figures/Box-place-v0_reset.png?ts=493567) | ![figures/Box-place-v0.gif?ts=876521](figures/Box-place-v0.gif?ts=876521) |
