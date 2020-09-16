

# Drawer Open and Pick and Place Tasks

## Debugging Tasks

Name                     | Observation Spec                       | Goal Init/Comment                       | 
-----------------        | ----------------                       | -------                                 | ------
**Drawer-fixed-v0**      | achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (40,)      | Drawer at a fixed location on the desk  | ![](figures/Drawer-fixed-v0.gif)
**Drawer-fixed-open-v0** | achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (40,) | Drawer at the same location, but open. This one<br> occupies a different area closer to the middle. | ![](figures/Drawer-place-v0.gif) 

| **Drawer-fixed-v0** | **distribution** |   |
|:-------------------:|:----------------:|:-:|
| ![figures/Drawer-fixed-v0_init.png?ts=977038](figures/Drawer-fixed-v0_init.png?ts=977038) | ![figures/Drawer-fixed-v0_reset.png?ts=133110](figures/Drawer-fixed-v0_reset.png?ts=133110) | ![figures/Drawer-fixed-v0.gif?ts=739064](figures/Drawer-fixed-v0.gif?ts=739064) |
| **Drawer-fixed-open-v0** | **distribution** |   |
| ![figures/Drawer-fixed-open-v0_init.png?ts=413324](figures/Drawer-fixed-open-v0_init.png?ts=413324) | ![figures/Drawer-fixed-open-v0_reset.png?ts=463517](figures/Drawer-fixed-open-v0_reset.png?ts=463517) | ![figures/Drawer-fixed-open-v0.gif?ts=034054](figures/Drawer-fixed-open-v0.gif?ts=034054) |


## Drawer Primitive Tasks

> **Note**: To test the agent's performance in placing the object into 
> the drawer, we need to fix the target location to the drawer.

Name                     | Observation Spec                       | Goal Init/Comment                       | 
-----------------        | ----------------                       | -------                                 | ------
**Drawer-open-v0**       | {get_obs_spec('Drawer-open-v0')}       | open the drawer                         | ![](figures/Drawer-open-v0.gif)
**Drawer-close-v0**      | {get_obs_spec('Drawer-close-v0')}      | closing the drawer                      | ![](figures/Drawer-close-v0.gif)
**Drawer-place-easy-v0** | {get_obs_spec('Drawer-place-easy-v0')} | Drawer is open to begin with. Same as gym<br> pick and place. Eventually we want to<br>specify goals inside the drawer | ![](figures/Drawer-place-easy-v0.gif)
**Drawer-place-v0**      | {get_obs_spec('Drawer-place-v0')}      | need to first open the drawer, otherwise<br> same as above.               | ![](figures/Drawer-place-v0.gif) 



## Details of Each Task

| **Drawer-open-v0** | **distribution** |   |
|:------------------:|:----------------:|:-:|
| ![figures/Drawer-open-v0_init.png?ts=489947](figures/Drawer-open-v0_init.png?ts=489947) | ![figures/Drawer-open-v0_reset.png?ts=539597](figures/Drawer-open-v0_reset.png?ts=539597) | ![figures/Drawer-open-v0.gif?ts=370212](figures/Drawer-open-v0.gif?ts=370212) |
| **Drawer-close-v0** | **distribution** |   |
| ![figures/Drawer-close-v0_init.png?ts=857490](figures/Drawer-close-v0_init.png?ts=857490) | ![figures/Drawer-close-v0_reset.png?ts=906814](figures/Drawer-close-v0_reset.png?ts=906814) | ![figures/Drawer-close-v0.gif?ts=650241](figures/Drawer-close-v0.gif?ts=650241) |
| **Drawer-place-easy-v0** | **distribution** |   |
| ![figures/Drawer-place-easy-v0_init.png?ts=119704](figures/Drawer-place-easy-v0_init.png?ts=119704) | ![figures/Drawer-place-easy-v0_reset.png?ts=174163](figures/Drawer-place-easy-v0_reset.png?ts=174163) | ![figures/Drawer-place-easy-v0.gif?ts=738261](figures/Drawer-place-easy-v0.gif?ts=738261) |
| **Drawer-place-v0** | **distribution** |   |
| ![figures/Drawer-place-v0_init.png?ts=315477](figures/Drawer-place-v0_init.png?ts=315477) | ![figures/Drawer-place-v0_reset.png?ts=366109](figures/Drawer-place-v0_reset.png?ts=366109) | ![figures/Drawer-place-v0.gif?ts=969196](figures/Drawer-place-v0.gif?ts=969196) |
