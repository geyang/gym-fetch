
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
**Box-fixed-place-easy-v0**    | achieved_goal:<br>&nbsp;&nbsp;&nbsp;&nbsp;object0: (3,)<br>desired_goal:<br>&nbsp;&nbsp;&nbsp;&nbsp;object0: (3,)<br>observation: (43,) | place the block inside an open box | ![](figures/Box-fixed-place-easy-v0.gif)
**Box-fixed-place-medium-v0**  | achieved_goal: (6,)<br>desired_goal: (6,)<br>observation: (43,) | place the block inside an open box | ![](figures/Box-fixed-place-medium-v0.gif)
**Box-fixed-place-v0**         | achieved_goal: (6,)<br>desired_goal: (6,)<br>observation: (43,)      | need to first open the box         | ![](figures/Box-fixed-place-v0.gif)

## Details of Each Task

```python
box_envs = [
    "fetch:Box-aside-v0",
    "fetch:Box-fixed-v0",
    # Box Environments
    "fetch:Box-open-v0",
    "fetch:Box-close-v0",
    "fetch:Box-fixed-place-easy-v0",
    "fetch:Box-fixed-place-medium-v0",
    "fetch:Box-fixed-place-v0", ]
```
| **Box-aside-v0** | **distribution** |   |
|:----------------:|:----------------:|:-:|
| ![figures/Box-aside-v0_init.png?ts=716172](figures/Box-aside-v0_init.png?ts=716172) | ![figures/Box-aside-v0_reset.png?ts=821791](figures/Box-aside-v0_reset.png?ts=821791) | ![figures/Box-aside-v0.gif?ts=450551](figures/Box-aside-v0.gif?ts=450551) |
| **Box-fixed-v0** | **distribution** |   |
| ![figures/Box-fixed-v0_init.png?ts=400246](figures/Box-fixed-v0_init.png?ts=400246) | ![figures/Box-fixed-v0_reset.png?ts=508313](figures/Box-fixed-v0_reset.png?ts=508313) | ![figures/Box-fixed-v0.gif?ts=448630](figures/Box-fixed-v0.gif?ts=448630) |
| **Box-open-v0** | **distribution** |   |
| ![figures/Box-open-v0_init.png?ts=021632](figures/Box-open-v0_init.png?ts=021632) | ![figures/Box-open-v0_reset.png?ts=125141](figures/Box-open-v0_reset.png?ts=125141) | ![figures/Box-open-v0.gif?ts=239264](figures/Box-open-v0.gif?ts=239264) |
| **Box-close-v0** | **distribution** |   |
| ![figures/Box-close-v0_init.png?ts=815275](figures/Box-close-v0_init.png?ts=815275) | ![figures/Box-close-v0_reset.png?ts=916138](figures/Box-close-v0_reset.png?ts=916138) | ![figures/Box-close-v0.gif?ts=804750](figures/Box-close-v0.gif?ts=804750) |
| **Box-fixed-place-easy-v0** | **distribution** |   |
| ![figures/Box-fixed-place-easy-v0_init.png?ts=550288](figures/Box-fixed-place-easy-v0_init.png?ts=550288) | ![figures/Box-fixed-place-easy-v0_reset.png?ts=628765](figures/Box-fixed-place-easy-v0_reset.png?ts=628765) | ![figures/Box-fixed-place-easy-v0.gif?ts=577659](figures/Box-fixed-place-easy-v0.gif?ts=577659) |
| **Box-fixed-place-medium-v0** | **distribution** |   |
| ![figures/Box-fixed-place-medium-v0_init.png?ts=500662](figures/Box-fixed-place-medium-v0_init.png?ts=500662) | ![figures/Box-fixed-place-medium-v0_reset.png?ts=557333](figures/Box-fixed-place-medium-v0_reset.png?ts=557333) | ![figures/Box-fixed-place-medium-v0.gif?ts=249616](figures/Box-fixed-place-medium-v0.gif?ts=249616) |
| **Box-fixed-place-v0** | **distribution** |   |
| ![figures/Box-fixed-place-v0_init.png?ts=980399](figures/Box-fixed-place-v0_init.png?ts=980399) | ![figures/Box-fixed-place-v0_reset.png?ts=063234](figures/Box-fixed-place-v0_reset.png?ts=063234) | ![figures/Box-fixed-place-v0.gif?ts=011123](figures/Box-fixed-place-v0.gif?ts=011123) |
