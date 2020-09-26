
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
| ![figures/Drawer-fixed-v0_init.png?ts=842559](figures/Drawer-fixed-v0_init.png?ts=842559) | ![figures/Drawer-fixed-v0_reset.png?ts=958209](figures/Drawer-fixed-v0_reset.png?ts=958209) | ![figures/Drawer-fixed-v0.gif?ts=608934](figures/Drawer-fixed-v0.gif?ts=608934) |
| **Drawer-fixed-open-v0** | **distribution** |   |
| ![figures/Drawer-fixed-open-v0_init.png?ts=276849](figures/Drawer-fixed-open-v0_init.png?ts=276849) | ![figures/Drawer-fixed-open-v0_reset.png?ts=350157](figures/Drawer-fixed-open-v0_reset.png?ts=350157) | ![figures/Drawer-fixed-open-v0.gif?ts=972904](figures/Drawer-fixed-open-v0.gif?ts=972904) |
| **Drawer-fixed-mixed-v0** | **distribution** |   |
| ![figures/Drawer-fixed-mixed-v0_init.png?ts=692850](figures/Drawer-fixed-mixed-v0_init.png?ts=692850) | ![figures/Drawer-fixed-mixed-v0_reset.png?ts=743430](figures/Drawer-fixed-mixed-v0_reset.png?ts=743430) | ![figures/Drawer-fixed-mixed-v0.gif?ts=147751](figures/Drawer-fixed-mixed-v0.gif?ts=147751) |


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
| ![figures/Drawer-open-v0_init.png?ts=307708](figures/Drawer-open-v0_init.png?ts=307708) | ![figures/Drawer-open-v0_reset.png?ts=380216](figures/Drawer-open-v0_reset.png?ts=380216) | ![figures/Drawer-open-v0.gif?ts=082637](figures/Drawer-open-v0.gif?ts=082637) |
| **Drawer-close-v0** | **distribution** |   |
| ![figures/Drawer-close-v0_init.png?ts=328950](figures/Drawer-close-v0_init.png?ts=328950) | ![figures/Drawer-close-v0_reset.png?ts=382075](figures/Drawer-close-v0_reset.png?ts=382075) | ![figures/Drawer-close-v0.gif?ts=324423](figures/Drawer-close-v0.gif?ts=324423) |
| **Drawer-place-easy-v0** | **distribution** |   |
| ![figures/Drawer-place-easy-v0_init.png?ts=879674](figures/Drawer-place-easy-v0_init.png?ts=879674) | ![figures/Drawer-place-easy-v0_reset.png?ts=980399](figures/Drawer-place-easy-v0_reset.png?ts=980399) | ![figures/Drawer-place-easy-v0.gif?ts=862672](figures/Drawer-place-easy-v0.gif?ts=862672) |
| **Drawer-place-v0** | **distribution** |   |
| ![figures/Drawer-place-v0_init.png?ts=360364](figures/Drawer-place-v0_init.png?ts=360364) | ![figures/Drawer-place-v0_reset.png?ts=482005](figures/Drawer-place-v0_reset.png?ts=482005) | ![figures/Drawer-place-v0.gif?ts=357711](figures/Drawer-place-v0.gif?ts=357711) |
