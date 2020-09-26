
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
| ![figures/Box-aside-v0_init.png?ts=273283](figures/Box-aside-v0_init.png?ts=273283) | ![figures/Box-aside-v0_reset.png?ts=383816](figures/Box-aside-v0_reset.png?ts=383816) | ![figures/Box-aside-v0.gif?ts=959084](figures/Box-aside-v0.gif?ts=959084) |
| **Box-fixed-v0** | **distribution** |   |
| ![figures/Box-fixed-v0_init.png?ts=529715](figures/Box-fixed-v0_init.png?ts=529715) | ![figures/Box-fixed-v0_reset.png?ts=584749](figures/Box-fixed-v0_reset.png?ts=584749) | ![figures/Box-fixed-v0.gif?ts=251219](figures/Box-fixed-v0.gif?ts=251219) |
| **Box-open-v0** | **distribution** |   |
| ![figures/Box-open-v0_init.png?ts=752077](figures/Box-open-v0_init.png?ts=752077) | ![figures/Box-open-v0_reset.png?ts=814828](figures/Box-open-v0_reset.png?ts=814828) | ![figures/Box-open-v0.gif?ts=770176](figures/Box-open-v0.gif?ts=770176) |
| **Box-close-v0** | **distribution** |   |
| ![figures/Box-close-v0_init.png?ts=404572](figures/Box-close-v0_init.png?ts=404572) | ![figures/Box-close-v0_reset.png?ts=463133](figures/Box-close-v0_reset.png?ts=463133) | ![figures/Box-close-v0.gif?ts=175005](figures/Box-close-v0.gif?ts=175005) |
| **Box-place-easy-v0** | **distribution** |   |
| ![figures/Box-place-easy-v0_init.png?ts=870730](figures/Box-place-easy-v0_init.png?ts=870730) | ![figures/Box-place-easy-v0_reset.png?ts=935566](figures/Box-place-easy-v0_reset.png?ts=935566) | ![figures/Box-place-easy-v0.gif?ts=901326](figures/Box-place-easy-v0.gif?ts=901326) |
| **Box-place-medium-v0** | **distribution** |   |
| ![figures/Box-place-medium-v0_init.png?ts=613576](figures/Box-place-medium-v0_init.png?ts=613576) | ![figures/Box-place-medium-v0_reset.png?ts=676965](figures/Box-place-medium-v0_reset.png?ts=676965) | ![figures/Box-place-medium-v0.gif?ts=647639](figures/Box-place-medium-v0.gif?ts=647639) |
| **Box-place-v0** | **distribution** |   |
| ![figures/Box-place-v0_init.png?ts=260221](figures/Box-place-v0_init.png?ts=260221) | ![figures/Box-place-v0_reset.png?ts=326238](figures/Box-place-v0_reset.png?ts=326238) | ![figures/Box-place-v0.gif?ts=867621](figures/Box-place-v0.gif?ts=867621) |
