
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
**Box-place-medium-v0**  | achieved_goal: None<br>desired_goal: None<br>observation: (43,) | place the block inside an open box | ![](figures/Box-place-medium-v0.gif)
**Box-place-v0**         | achieved_goal: None<br>desired_goal: None<br>observation: (43,)      | need to first open the box         | ![](figures/Box-place-v0.gif)

## Details of Each Task

| **Box-aside-v0** | **distribution** |   |
|:----------------:|:----------------:|:-:|
| ![figures/Box-aside-v0_init.png?ts=335480](figures/Box-aside-v0_init.png?ts=335480) | ![figures/Box-aside-v0_reset.png?ts=467326](figures/Box-aside-v0_reset.png?ts=467326) | ![figures/Box-aside-v0.gif?ts=543905](figures/Box-aside-v0.gif?ts=543905) |
| **Box-fixed-v0** | **distribution** |   |
| ![figures/Box-fixed-v0_init.png?ts=926958](figures/Box-fixed-v0_init.png?ts=926958) | ![figures/Box-fixed-v0_reset.png?ts=093375](figures/Box-fixed-v0_reset.png?ts=093375) | ![figures/Box-fixed-v0.gif?ts=039587](figures/Box-fixed-v0.gif?ts=039587) |
| **Box-open-v0** | **distribution** |   |
| ![figures/Box-open-v0_init.png?ts=452358](figures/Box-open-v0_init.png?ts=452358) | ![figures/Box-open-v0_reset.png?ts=589121](figures/Box-open-v0_reset.png?ts=589121) | ![figures/Box-open-v0.gif?ts=979080](figures/Box-open-v0.gif?ts=979080) |
| **Box-close-v0** | **distribution** |   |
| ![figures/Box-close-v0_init.png?ts=401699](figures/Box-close-v0_init.png?ts=401699) | ![figures/Box-close-v0_reset.png?ts=544369](figures/Box-close-v0_reset.png?ts=544369) | ![figures/Box-close-v0.gif?ts=275603](figures/Box-close-v0.gif?ts=275603) |
| **Box-place-easy-v0** | **distribution** |   |
| ![figures/Box-place-easy-v0_init.png?ts=348085](figures/Box-place-easy-v0_init.png?ts=348085) | ![figures/Box-place-easy-v0_reset.png?ts=455615](figures/Box-place-easy-v0_reset.png?ts=455615) | ![figures/Box-place-easy-v0.gif?ts=621828](figures/Box-place-easy-v0.gif?ts=621828) |
| **Box-place-medium-v0** | **distribution** |   |
| ![figures/Box-place-medium-v0_init.png?ts=473429](figures/Box-place-medium-v0_init.png?ts=473429) | ![figures/Box-place-medium-v0_reset.png?ts=785850](figures/Box-place-medium-v0_reset.png?ts=785850) | ![figures/Box-place-medium-v0.gif?ts=421104](figures/Box-place-medium-v0.gif?ts=421104) |
| **Box-place-v0** | **distribution** |   |
| ![figures/Box-place-v0_init.png?ts=974918](figures/Box-place-v0_init.png?ts=974918) | ![figures/Box-place-v0_reset.png?ts=123965](figures/Box-place-v0_reset.png?ts=123965) | ![figures/Box-place-v0.gif?ts=886667](figures/Box-place-v0.gif?ts=886667) |
