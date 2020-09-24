
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
| ![figures/Box-aside-v0_init.png?ts=892274](figures/Box-aside-v0_init.png?ts=892274) | ![figures/Box-aside-v0_reset.png?ts=145711](figures/Box-aside-v0_reset.png?ts=145711) | ![figures/Box-aside-v0.gif?ts=872883](figures/Box-aside-v0.gif?ts=872883) |
| **Box-fixed-v0** | **distribution** |   |
| ![figures/Box-fixed-v0_init.png?ts=600827](figures/Box-fixed-v0_init.png?ts=600827) | ![figures/Box-fixed-v0_reset.png?ts=658440](figures/Box-fixed-v0_reset.png?ts=658440) | ![figures/Box-fixed-v0.gif?ts=228962](figures/Box-fixed-v0.gif?ts=228962) |
| **Box-open-v0** | **distribution** |   |
| ![figures/Box-open-v0_init.png?ts=797850](figures/Box-open-v0_init.png?ts=797850) | ![figures/Box-open-v0_reset.png?ts=852788](figures/Box-open-v0_reset.png?ts=852788) | ![figures/Box-open-v0.gif?ts=597491](figures/Box-open-v0.gif?ts=597491) |
| **Box-close-v0** | **distribution** |   |
| ![figures/Box-close-v0_init.png?ts=245884](figures/Box-close-v0_init.png?ts=245884) | ![figures/Box-close-v0_reset.png?ts=299150](figures/Box-close-v0_reset.png?ts=299150) | ![figures/Box-close-v0.gif?ts=851496](figures/Box-close-v0.gif?ts=851496) |
| **Box-place-easy-v0** | **distribution** |   |
| ![figures/Box-place-easy-v0_init.png?ts=564027](figures/Box-place-easy-v0_init.png?ts=564027) | ![figures/Box-place-easy-v0_reset.png?ts=619268](figures/Box-place-easy-v0_reset.png?ts=619268) | ![figures/Box-place-easy-v0.gif?ts=426371](figures/Box-place-easy-v0.gif?ts=426371) |
| **Box-place-medium-v0** | **distribution** |   |
| ![figures/Box-place-medium-v0_init.png?ts=020781](figures/Box-place-medium-v0_init.png?ts=020781) | ![figures/Box-place-medium-v0_reset.png?ts=075024](figures/Box-place-medium-v0_reset.png?ts=075024) | ![figures/Box-place-medium-v0.gif?ts=063824](figures/Box-place-medium-v0.gif?ts=063824) |
| **Box-place-v0** | **distribution** |   |
| ![figures/Box-place-v0_init.png?ts=670137](figures/Box-place-v0_init.png?ts=670137) | ![figures/Box-place-v0_reset.png?ts=727676](figures/Box-place-v0_reset.png?ts=727676) | ![figures/Box-place-v0.gif?ts=517437](figures/Box-place-v0.gif?ts=517437) |
