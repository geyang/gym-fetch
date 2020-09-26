
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
| ![figures/Drawer-fixed-v0_init.png?ts=326281](figures/Drawer-fixed-v0_init.png?ts=326281) | ![figures/Drawer-fixed-v0_reset.png?ts=441545](figures/Drawer-fixed-v0_reset.png?ts=441545) | ![figures/Drawer-fixed-v0.gif?ts=043396](figures/Drawer-fixed-v0.gif?ts=043396) |
| **Drawer-fixed-open-v0** | **distribution** |   |
| ![figures/Drawer-fixed-open-v0_init.png?ts=845705](figures/Drawer-fixed-open-v0_init.png?ts=845705) | ![figures/Drawer-fixed-open-v0_reset.png?ts=926017](figures/Drawer-fixed-open-v0_reset.png?ts=926017) | ![figures/Drawer-fixed-open-v0.gif?ts=939865](figures/Drawer-fixed-open-v0.gif?ts=939865) |
| **Drawer-fixed-mixed-v0** | **distribution** |   |
| ![figures/Drawer-fixed-mixed-v0_init.png?ts=634889](figures/Drawer-fixed-mixed-v0_init.png?ts=634889) | ![figures/Drawer-fixed-mixed-v0_reset.png?ts=692923](figures/Drawer-fixed-mixed-v0_reset.png?ts=692923) | ![figures/Drawer-fixed-mixed-v0.gif?ts=945127](figures/Drawer-fixed-mixed-v0.gif?ts=945127) |


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
| ![figures/Drawer-open-v0_init.png?ts=518502](figures/Drawer-open-v0_init.png?ts=518502) | ![figures/Drawer-open-v0_reset.png?ts=579406](figures/Drawer-open-v0_reset.png?ts=579406) | ![figures/Drawer-open-v0.gif?ts=890584](figures/Drawer-open-v0.gif?ts=890584) |
| **Drawer-close-v0** | **distribution** |   |
| ![figures/Drawer-close-v0_init.png?ts=401881](figures/Drawer-close-v0_init.png?ts=401881) | ![figures/Drawer-close-v0_reset.png?ts=483758](figures/Drawer-close-v0_reset.png?ts=483758) | ![figures/Drawer-close-v0.gif?ts=822165](figures/Drawer-close-v0.gif?ts=822165) |
| **Drawer-place-easy-v0** | **distribution** |   |
| ![figures/Drawer-place-easy-v0_init.png?ts=418737](figures/Drawer-place-easy-v0_init.png?ts=418737) | ![figures/Drawer-place-easy-v0_reset.png?ts=564158](figures/Drawer-place-easy-v0_reset.png?ts=564158) | ![figures/Drawer-place-easy-v0.gif?ts=435316](figures/Drawer-place-easy-v0.gif?ts=435316) |
| **Drawer-place-v0** | **distribution** |   |
| ![figures/Drawer-place-v0_init.png?ts=819721](figures/Drawer-place-v0_init.png?ts=819721) | ![figures/Drawer-place-v0_reset.png?ts=889448](figures/Drawer-place-v0_reset.png?ts=889448) | ![figures/Drawer-place-v0.gif?ts=680905](figures/Drawer-place-v0.gif?ts=680905) |
