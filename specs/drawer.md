
# Drawer Open and Pick and Place Tasks

## Debugging Tasks

Name                      | Observation Spec                        | Goal Init/Comment                         | 
-----------------         | ----------------                        | -------                                   | ------
**Drawer-fixed-v0**       | achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (40,)       | Drawer at a fixed location on the desk    | ![](figures/Drawer-fixed-v0.gif)
**Drawer-fixed-open-v0**  | achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (40,)  | Drawer at the same location, but open. This one<br>occupies a different area closer to the middle. | ![](figures/Drawer-fixed-open-v0.gif) 
**Drawer-fixed-mixed-v0** | achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (40,) | Mix of these two envs at 50% of the time. | ![](figures/Drawer-fixed-mixed-v0.gif) 

The drawer open environment does not learn (only learns to push the block around on the table). We engineer a mixed environment that is open 50% of the time. **Add this as a new debug environment**.

| **Drawer-fixed-v0** | **distribution** |   |
|:-------------------:|:----------------:|:-:|
| ![figures/Drawer-fixed-v0_init.png?ts=956931](figures/Drawer-fixed-v0_init.png?ts=956931) | ![figures/Drawer-fixed-v0_reset.png?ts=096490](figures/Drawer-fixed-v0_reset.png?ts=096490) | ![figures/Drawer-fixed-v0.gif?ts=841406](figures/Drawer-fixed-v0.gif?ts=841406) |
| **Drawer-fixed-open-v0** | **distribution** |   |
| ![figures/Drawer-fixed-open-v0_init.png?ts=523768](figures/Drawer-fixed-open-v0_init.png?ts=523768) | ![figures/Drawer-fixed-open-v0_reset.png?ts=598417](figures/Drawer-fixed-open-v0_reset.png?ts=598417) | ![figures/Drawer-fixed-open-v0.gif?ts=514083](figures/Drawer-fixed-open-v0.gif?ts=514083) |
| **Drawer-fixed-mixed-v0** | **distribution** |   |
| ![figures/Drawer-fixed-mixed-v0_init.png?ts=783598](figures/Drawer-fixed-mixed-v0_init.png?ts=783598) | ![figures/Drawer-fixed-mixed-v0_reset.png?ts=842339](figures/Drawer-fixed-mixed-v0_reset.png?ts=842339) | ![figures/Drawer-fixed-mixed-v0.gif?ts=637647](figures/Drawer-fixed-mixed-v0.gif?ts=637647) |


## Drawer Primitive Tasks

> **Note**: To test the agent's performance in placing the object into 
> the drawer, we need to fix the target location to the drawer.

Name                     | Observation Spec                       | Goal Init/Comment                       | 
-----------------        | ----------------                       | -------                                 | ------
**Drawer-open-v0**       | achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (25,)       | open the drawer                         | ![](figures/Drawer-open-v0.gif)
**Drawer-close-v0**      | achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (25,)      | closing the drawer                      | ![](figures/Drawer-close-v0.gif)
**Drawer-place-easy-v0** | achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (40,) | Drawer is open to begin with. Same as gym<br> pick and place. Eventually we want to<br>specify goals inside the drawer | ![](figures/Drawer-place-easy-v0.gif)
**Drawer-place-v0**      | achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (40,)      | need to first open the drawer, otherwise<br> same as above.               | ![](figures/Drawer-place-v0.gif) 

## Details of Each Task

| **Drawer-open-v0** | **distribution** |   |
|:------------------:|:----------------:|:-:|
| ![figures/Drawer-open-v0_init.png?ts=674980](figures/Drawer-open-v0_init.png?ts=674980) | ![figures/Drawer-open-v0_reset.png?ts=778593](figures/Drawer-open-v0_reset.png?ts=778593) | ![figures/Drawer-open-v0.gif?ts=872853](figures/Drawer-open-v0.gif?ts=872853) |
| **Drawer-close-v0** | **distribution** |   |
| ![figures/Drawer-close-v0_init.png?ts=522553](figures/Drawer-close-v0_init.png?ts=522553) | ![figures/Drawer-close-v0_reset.png?ts=601940](figures/Drawer-close-v0_reset.png?ts=601940) | ![figures/Drawer-close-v0.gif?ts=166382](figures/Drawer-close-v0.gif?ts=166382) |
| **Drawer-place-easy-v0** | **distribution** |   |
| ![figures/Drawer-place-easy-v0_init.png?ts=933411](figures/Drawer-place-easy-v0_init.png?ts=933411) | ![figures/Drawer-place-easy-v0_reset.png?ts=022304](figures/Drawer-place-easy-v0_reset.png?ts=022304) | ![figures/Drawer-place-easy-v0.gif?ts=705867](figures/Drawer-place-easy-v0.gif?ts=705867) |
| **Drawer-place-v0** | **distribution** |   |
| ![figures/Drawer-place-v0_init.png?ts=220179](figures/Drawer-place-v0_init.png?ts=220179) | ![figures/Drawer-place-v0_reset.png?ts=309566](figures/Drawer-place-v0_reset.png?ts=309566) | ![figures/Drawer-place-v0.gif?ts=878025](figures/Drawer-place-v0.gif?ts=878025) |
