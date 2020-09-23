
# Drawer Open and Pick and Place Tasks

## Debugging Tasks

Name                      | Observation Spec                        | Goal Init/Comment                         | 
-----------------         | ----------------                        | -------                                   | ------
**Drawer-fixed-v0**       | achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (40,)       | Drawer at a fixed location on the desk    | ![](figures/Drawer-fixed-v0.gif)
**Drawer-fixed-open-v0**  | achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (40,)  | Drawer at the same location, but open. This one<br>occupies a different area closer to the middle. | ![](figures/Drawer-fixed-open-v0.gif) 
**Drawer-fixed-mixed-v0** | achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (40,) | Mix of these two envs at 50% of the time. | ![](figures/Drawer-fixed-mixed-v0.gif) 

The drawer open environment does not learn (only learns to push the block around on the table). We engineer a mixed environment that is open 50% of the time. **Add this as a new debug environment**.

| **Drawer-fixed-v0** | **distribution** |   | |
|:-------------------:|:----------------:|:-:|---------------------|
| ![figures/Drawer-fixed-v0_init.png?ts=729334](figures/Drawer-fixed-v0_init.png?ts=729334) | ![figures/Drawer-fixed-v0_reset.png?ts=923109](figures/Drawer-fixed-v0_reset.png?ts=923109) | ![figures/Drawer-fixed-v0.gif?ts=716299](figures/Drawer-fixed-v0.gif?ts=716299) | |
| **Drawer-fixed-open-v0** | **distribution** |   | |
| ![figures/Drawer-fixed-open-v0_init.png?ts=144152](figures/Drawer-fixed-open-v0_init.png?ts=144152) | ![figures/Drawer-fixed-open-v0_reset.png?ts=279344](figures/Drawer-fixed-open-v0_reset.png?ts=279344) | ![figures/Drawer-fixed-open-v0.gif?ts=314836](figures/Drawer-fixed-open-v0.gif?ts=314836) | |
| **Drawer-fixed-mixed-v0** | **distribution** |   | |
| ![figures/Drawer-fixed-mixed-v0_init.png?ts=058919](figures/Drawer-fixed-mixed-v0_init.png?ts=058919) | ![figures/Drawer-fixed-mixed-v0_reset.png?ts=121809](figures/Drawer-fixed-mixed-v0_reset.png?ts=121809) | ![figures/Drawer-fixed-mixed-v0.gif?ts=006540](figures/Drawer-fixed-mixed-v0.gif?ts=006540) | achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (40,)<br>Mix of these two envs at 50% of the time. |


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
| ![figures/Drawer-open-v0_init.png?ts=518138](figures/Drawer-open-v0_init.png?ts=518138) | ![figures/Drawer-open-v0_reset.png?ts=646194](figures/Drawer-open-v0_reset.png?ts=646194) | ![figures/Drawer-open-v0.gif?ts=485721](figures/Drawer-open-v0.gif?ts=485721) |
| **Drawer-close-v0** | **distribution** |   |
| ![figures/Drawer-close-v0_init.png?ts=106469](figures/Drawer-close-v0_init.png?ts=106469) | ![figures/Drawer-close-v0_reset.png?ts=202166](figures/Drawer-close-v0_reset.png?ts=202166) | ![figures/Drawer-close-v0.gif?ts=009403](figures/Drawer-close-v0.gif?ts=009403) |
| **Drawer-place-easy-v0** | **distribution** |   |
| ![figures/Drawer-place-easy-v0_init.png?ts=452615](figures/Drawer-place-easy-v0_init.png?ts=452615) | ![figures/Drawer-place-easy-v0_reset.png?ts=559956](figures/Drawer-place-easy-v0_reset.png?ts=559956) | ![figures/Drawer-place-easy-v0.gif?ts=419291](figures/Drawer-place-easy-v0.gif?ts=419291) |
| **Drawer-place-v0** | **distribution** |   |
| ![figures/Drawer-place-v0_init.png?ts=927383](figures/Drawer-place-v0_init.png?ts=927383) | ![figures/Drawer-place-v0_reset.png?ts=059441](figures/Drawer-place-v0_reset.png?ts=059441) | ![figures/Drawer-place-v0.gif?ts=936736](figures/Drawer-place-v0.gif?ts=936736) |
