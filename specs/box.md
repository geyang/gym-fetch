
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
| ![figures/Box-aside-v0_init.png?ts=621515](figures/Box-aside-v0_init.png?ts=621515) | ![figures/Box-aside-v0_reset.png?ts=788066](figures/Box-aside-v0_reset.png?ts=788066) | ![figures/Box-aside-v0.gif?ts=504451](figures/Box-aside-v0.gif?ts=504451) |
| **Box-fixed-v0** | **distribution** |   |
| ![figures/Box-fixed-v0_init.png?ts=280709](figures/Box-fixed-v0_init.png?ts=280709) | ![figures/Box-fixed-v0_reset.png?ts=386771](figures/Box-fixed-v0_reset.png?ts=386771) | ![figures/Box-fixed-v0.gif?ts=975020](figures/Box-fixed-v0.gif?ts=975020) |
| **Box-open-v0** | **distribution** |   |
| ![figures/Box-open-v0_init.png?ts=628606](figures/Box-open-v0_init.png?ts=628606) | ![figures/Box-open-v0_reset.png?ts=733366](figures/Box-open-v0_reset.png?ts=733366) | ![figures/Box-open-v0.gif?ts=797238](figures/Box-open-v0.gif?ts=797238) |
| **Box-close-v0** | **distribution** |   |
| ![figures/Box-close-v0_init.png?ts=416739](figures/Box-close-v0_init.png?ts=416739) | ![figures/Box-close-v0_reset.png?ts=528232](figures/Box-close-v0_reset.png?ts=528232) | ![figures/Box-close-v0.gif?ts=528459](figures/Box-close-v0.gif?ts=528459) |
| **Box-place-easy-v0** | **distribution** |   |
| ![figures/Box-place-easy-v0_init.png?ts=241221](figures/Box-place-easy-v0_init.png?ts=241221) | ![figures/Box-place-easy-v0_reset.png?ts=366780](figures/Box-place-easy-v0_reset.png?ts=366780) | ![figures/Box-place-easy-v0.gif?ts=475285](figures/Box-place-easy-v0.gif?ts=475285) |
| **Box-place-medium-v0** | **distribution** |   |
| ![figures/Box-place-medium-v0_init.png?ts=280097](figures/Box-place-medium-v0_init.png?ts=280097) | ![figures/Box-place-medium-v0_reset.png?ts=393046](figures/Box-place-medium-v0_reset.png?ts=393046) | ![figures/Box-place-medium-v0.gif?ts=559232](figures/Box-place-medium-v0.gif?ts=559232) |
| **Box-place-v0** | **distribution** |   |
| ![figures/Box-place-v0_init.png?ts=144415](figures/Box-place-v0_init.png?ts=144415) | ![figures/Box-place-v0_reset.png?ts=251487](figures/Box-place-v0_reset.png?ts=251487) | ![figures/Box-place-v0.gif?ts=667020](figures/Box-place-v0.gif?ts=667020) |
