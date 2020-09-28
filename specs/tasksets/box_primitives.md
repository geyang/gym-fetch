
write_protected: true
---

# Primitive Tasks

## Box Diagnostic Tasks

| Name                     | Observation Spec                  | Goal Init/Comment     |                                |
| -----------------        | ----------------                  | -------               | ------                         |
| **Box-fixed-v0**         | achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (25,)    | box is in the middle  | ![](figures/Box-fixed-v0.gif)  |
| **Box-aside-v0**         | achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (25,)    | box is on the side    | ![](figures/Box-aside-v0.gif)  |
                                                                                                                                                   
## New Latent Planning Tasks                                                                                                                      
                                                                                                                                                    
| Name                         | Observation Spec                            | Goal Init/Comment     |                                            |
| -----------------            | ----------------                            | -------               | ------                                     |
| **Box-fixed-place-train-v0** | achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (25,)  | box is on the side    | ![](figures/Box-fixed-place-train-v0.gif)  |
| **Box-fixed-place-v0**       | achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (25,)        | box is on the side    | ![](figures/Box-fixed-place-v0.gif)        |
| **Box-aside-place-train-v0** | achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (25,)  | box is on the side    | ![](figures/Box-aside-place-train-v0.gif)  |
| **Box-aside-place-v0**       | achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (25,)        | box is on the side    | ![](figures/Box-aside-place-v0.gif)        |

## Details of Each Task

```python
box_envs = ['fetch:Box-aside-v0',
            'fetch:Box-fixed-v0',
            'fetch:Box-aside-place-train-v0',
            'fetch:Box-aside-place-v0',
            'fetch:Box-fixed-place-train-v0',
            'fetch:Box-fixed-place-v0']
```
| **Box-aside-v0** | **distribution** |   |
|:----------------:|:----------------:|:-:|
| ![figures/Box-aside-v0_init.png?ts=977820](figures/Box-aside-v0_init.png?ts=977820) | ![figures/Box-aside-v0_reset.png?ts=125799](figures/Box-aside-v0_reset.png?ts=125799) | ![figures/Box-aside-v0.gif?ts=931075](figures/Box-aside-v0.gif?ts=931075) |
| **Box-fixed-v0** | **distribution** |   |
| ![figures/Box-fixed-v0_init.png?ts=409527](figures/Box-fixed-v0_init.png?ts=409527) | ![figures/Box-fixed-v0_reset.png?ts=545510](figures/Box-fixed-v0_reset.png?ts=545510) | ![figures/Box-fixed-v0.gif?ts=312517](figures/Box-fixed-v0.gif?ts=312517) |
| **Box-aside-place-train-v0** | **distribution** |   |
| ![figures/Box-aside-place-train-v0_init.png?ts=918974](figures/Box-aside-place-train-v0_init.png?ts=918974) | ![figures/Box-aside-place-train-v0_reset.png?ts=097742](figures/Box-aside-place-train-v0_reset.png?ts=097742) | ![figures/Box-aside-place-train-v0.gif?ts=996088](figures/Box-aside-place-train-v0.gif?ts=996088) |
| **Box-aside-place-v0** | **distribution** |   |
| ![figures/Box-aside-place-v0_init.png?ts=719940](figures/Box-aside-place-v0_init.png?ts=719940) | ![figures/Box-aside-place-v0_reset.png?ts=834885](figures/Box-aside-place-v0_reset.png?ts=834885) | ![figures/Box-aside-place-v0.gif?ts=919929](figures/Box-aside-place-v0.gif?ts=919929) |
| **Box-fixed-place-train-v0** | **distribution** |   |
| ![figures/Box-fixed-place-train-v0_init.png?ts=762373](figures/Box-fixed-place-train-v0_init.png?ts=762373) | ![figures/Box-fixed-place-train-v0_reset.png?ts=921547](figures/Box-fixed-place-train-v0_reset.png?ts=921547) | ![figures/Box-fixed-place-train-v0.gif?ts=990160](figures/Box-fixed-place-train-v0.gif?ts=990160) |
| **Box-fixed-place-v0** | **distribution** |   |
| ![figures/Box-fixed-place-v0_init.png?ts=833559](figures/Box-fixed-place-v0_init.png?ts=833559) | ![figures/Box-fixed-place-v0_reset.png?ts=912473](figures/Box-fixed-place-v0_reset.png?ts=912473) | ![figures/Box-fixed-place-v0.gif?ts=562322](figures/Box-fixed-place-v0.gif?ts=562322) |
