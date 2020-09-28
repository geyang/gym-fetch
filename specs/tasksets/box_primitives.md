
write_protected: true
---

# Box Single Task Taskset

## Simple Goal Distributions

The goal distribution of these tasks are pure. Tasks with `place` postfix have the goal
initialized at the center of the box, whereas the other two uses the goal distribution
from standard gym `FetchPickAndPlace-v1` environment.

| Name                     | Observation Spec                      | Goal Init/Comment     |                                |
| -----------------        | ----------------                      | -------               | ------                         |
| **Box-fixed-v0**         | achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (25,)        | box is in the middle  | ![](figures/Box-fixed-v0.gif)  |
| **Box-aside-v0**         | achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (25,)        | box is on the side    | ![](figures/Box-aside-v0.gif)  |
| **Box-fixed-place-v0**   | achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (25,)  | box is on the side    | ![](figures/Box-fixed-place-v0.gif)        |
| **Box-aside-place-v0**   | achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (25,)  | box is on the side    | ![](figures/Box-aside-place-v0.gif)        |
                                                                                                                                                   
## Mixture Goal Distributions

These two training environments uses a mixture of 20/80% of pick-and-place distribution vs target inside the box.

| Name                         | Observation Spec                            | Goal Init/Comment     |                                            |
| -----------------            | ----------------                            | -------               | ------                                     |
| **Box-fixed-place-train-v0** | achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (25,)  | box is on the side    | ![](figures/Box-fixed-place-train-v0.gif)  |
| **Box-aside-place-train-v0** | achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (25,)  | box is on the side    | ![](figures/Box-aside-place-train-v0.gif)  |

## Details of Each Task

```python
box_envs = ['fetch:Box-aside-v0',
            'fetch:Box-aside-place-v0',
            'fetch:Box-aside-place-train-v0',
            'fetch:Box-fixed-v0',
            'fetch:Box-fixed-place-v0',
            'fetch:Box-fixed-place-train-v0']
```
| **Box-aside-v0** | **distribution** |   |
|:----------------:|:----------------:|:-:|
| ![figures/Box-aside-v0_init.png?ts=633888](figures/Box-aside-v0_init.png?ts=633888) | ![figures/Box-aside-v0_reset.png?ts=771788](figures/Box-aside-v0_reset.png?ts=771788) | ![figures/Box-aside-v0.gif?ts=564926](figures/Box-aside-v0.gif?ts=564926) |
| **Box-aside-place-v0** | **distribution** |   |
| ![figures/Box-aside-place-v0_init.png?ts=935533](figures/Box-aside-place-v0_init.png?ts=935533) | ![figures/Box-aside-place-v0_reset.png?ts=077962](figures/Box-aside-place-v0_reset.png?ts=077962) | ![figures/Box-aside-place-v0.gif?ts=771020](figures/Box-aside-place-v0.gif?ts=771020) |
| **Box-aside-place-train-v0** | **distribution** |   |
| ![figures/Box-aside-place-train-v0_init.png?ts=333087](figures/Box-aside-place-train-v0_init.png?ts=333087) | ![figures/Box-aside-place-train-v0_reset.png?ts=480236](figures/Box-aside-place-train-v0_reset.png?ts=480236) | ![figures/Box-aside-place-train-v0.gif?ts=493045](figures/Box-aside-place-train-v0.gif?ts=493045) |
| **Box-fixed-v0** | **distribution** |   |
| ![figures/Box-fixed-v0_init.png?ts=855975](figures/Box-fixed-v0_init.png?ts=855975) | ![figures/Box-fixed-v0_reset.png?ts=973603](figures/Box-fixed-v0_reset.png?ts=973603) | ![figures/Box-fixed-v0.gif?ts=661487](figures/Box-fixed-v0.gif?ts=661487) |
| **Box-fixed-place-v0** | **distribution** |   |
| ![figures/Box-fixed-place-v0_init.png?ts=023976](figures/Box-fixed-place-v0_init.png?ts=023976) | ![figures/Box-fixed-place-v0_reset.png?ts=176225](figures/Box-fixed-place-v0_reset.png?ts=176225) | ![figures/Box-fixed-place-v0.gif?ts=988257](figures/Box-fixed-place-v0.gif?ts=988257) |
| **Box-fixed-place-train-v0** | **distribution** |   |
| ![figures/Box-fixed-place-train-v0_init.png?ts=601948](figures/Box-fixed-place-train-v0_init.png?ts=601948) | ![figures/Box-fixed-place-train-v0_reset.png?ts=769822](figures/Box-fixed-place-train-v0_reset.png?ts=769822) | ![figures/Box-fixed-place-train-v0.gif?ts=719687](figures/Box-fixed-place-train-v0.gif?ts=719687) |
