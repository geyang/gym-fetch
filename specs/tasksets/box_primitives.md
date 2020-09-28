
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
| ![figures/Box-aside-v0_init.png?ts=753736](figures/Box-aside-v0_init.png?ts=753736) | ![figures/Box-aside-v0_reset.png?ts=855653](figures/Box-aside-v0_reset.png?ts=855653) | ![figures/Box-aside-v0.gif?ts=728861](figures/Box-aside-v0.gif?ts=728861) |
| **Box-aside-place-v0** | **distribution** |   |
| ![figures/Box-aside-place-v0_init.png?ts=763820](figures/Box-aside-place-v0_init.png?ts=763820) | ![figures/Box-aside-place-v0_reset.png?ts=832693](figures/Box-aside-place-v0_reset.png?ts=832693) | ![figures/Box-aside-place-v0.gif?ts=634047](figures/Box-aside-place-v0.gif?ts=634047) |
| **Box-aside-place-train-v0** | **distribution** |   |
| ![figures/Box-aside-place-train-v0_init.png?ts=308148](figures/Box-aside-place-train-v0_init.png?ts=308148) | ![figures/Box-aside-place-train-v0_reset.png?ts=459642](figures/Box-aside-place-train-v0_reset.png?ts=459642) | ![figures/Box-aside-place-train-v0.gif?ts=534584](figures/Box-aside-place-train-v0.gif?ts=534584) |
| **Box-fixed-v0** | **distribution** |   |
| ![figures/Box-fixed-v0_init.png?ts=208252](figures/Box-fixed-v0_init.png?ts=208252) | ![figures/Box-fixed-v0_reset.png?ts=301333](figures/Box-fixed-v0_reset.png?ts=301333) | ![figures/Box-fixed-v0.gif?ts=211651](figures/Box-fixed-v0.gif?ts=211651) |
| **Box-fixed-place-v0** | **distribution** |   |
| ![figures/Box-fixed-place-v0_init.png?ts=023390](figures/Box-fixed-place-v0_init.png?ts=023390) | ![figures/Box-fixed-place-v0_reset.png?ts=113182](figures/Box-fixed-place-v0_reset.png?ts=113182) | ![figures/Box-fixed-place-v0.gif?ts=811487](figures/Box-fixed-place-v0.gif?ts=811487) |
| **Box-fixed-place-train-v0** | **distribution** |   |
| ![figures/Box-fixed-place-train-v0_init.png?ts=230948](figures/Box-fixed-place-train-v0_init.png?ts=230948) | ![figures/Box-fixed-place-train-v0_reset.png?ts=393039](figures/Box-fixed-place-train-v0_reset.png?ts=393039) | ![figures/Box-fixed-place-train-v0.gif?ts=304488](figures/Box-fixed-place-train-v0.gif?ts=304488) |
