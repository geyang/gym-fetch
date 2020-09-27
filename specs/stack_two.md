
write_protected: true
---

# Stack-2 Environment


```python
initial_types = [
    'table-top',
    'in-hand',
    'obj1-in-hand',
    "train"
]

for init_type in initial_types:
    env = gym.make("fetch:StackTwo-v0", action=init_type)
    render_video(f"StackTwo-{initial_types}", 15, row, env=env, title=init_type,
                 filename=f"Stack2-{init_type}.gif")
```

| **table-top** | **in-hand** | **obj1-in-hand** | **train** |
|:-------------:|:-----------:|:----------------:|:---------:|
| ![figures/Stack2-table-top.gif?ts=570259](figures/Stack2-table-top.gif?ts=570259) | ![figures/Stack2-in-hand.gif?ts=748526](figures/Stack2-in-hand.gif?ts=748526) | ![figures/Stack2-obj1-in-hand.gif?ts=897911](figures/Stack2-obj1-in-hand.gif?ts=897911) | ![figures/Stack2-train.gif?ts=950058](figures/Stack2-train.gif?ts=950058) |

## Box Diagnostic Tasks

| Name                           | Observation Spec                             | Goal Init/Comment               |                                             |
| -----------------              | ----------------                             | -------                         | ------                                      |
| **StackTwo-train-v0**          | achieved_goal: (6,)<br>desired_goal: (6,)<br>observation: (40,)          | Three parts<br>- table-top<br>- in-hand<br>- obj1-in-hand  | ![](figures/StackTwo-train-v0.gif) |
| **StackTwo-fixed-v0**          | achieved_goal: (6,)<br>desired_goal: (6,)<br>observation: (40,)          | object 0 welded in-place        | ![](figures/StackTwo-fixed-v0.gif)          |
| **StackTwo-fixed-pp-goals-v0** | achieved_goal: (6,)<br>desired_goal: (6,)<br>observation: (40,) | object 0 welded in-place        | ![](figures/StackTwo-fixed-pp-goals-v0.gif) |
| **StackTwo-v0**                | achieved_goal: (6,)<br>desired_goal: (6,)<br>observation: (40,)                |                                 | ![](figures/StackTwo-v0.gif)                |

## Details of Each Task

```python
box_envs = [
    "fetch:StackTwo-train-v0",
    "fetch:StackTwo-fixed-v0",
    "fetch:StackTwo-fixed-pp-goals-v0",
    "fetch:StackTwo-v0",
]
```
| **StackTwo-train-v0** | **distribution** |   |
|:---------------------:|:----------------:|:-:|
| ![figures/StackTwo-train-v0_init.png?ts=989642](figures/StackTwo-train-v0_init.png?ts=989642) | ![figures/StackTwo-train-v0_reset.png?ts=089008](figures/StackTwo-train-v0_reset.png?ts=089008) | ![figures/StackTwo-train-v0.gif?ts=652658](figures/StackTwo-train-v0.gif?ts=652658) |
| **StackTwo-fixed-v0** | **distribution** |   |
| ![figures/StackTwo-fixed-v0_init.png?ts=252235](figures/StackTwo-fixed-v0_init.png?ts=252235) | ![figures/StackTwo-fixed-v0_reset.png?ts=308391](figures/StackTwo-fixed-v0_reset.png?ts=308391) | ![figures/StackTwo-fixed-v0.gif?ts=048735](figures/StackTwo-fixed-v0.gif?ts=048735) |
| **StackTwo-v0** | **distribution** |   |
| ![figures/StackTwo-v0_init.png?ts=628558](figures/StackTwo-v0_init.png?ts=628558) | ![figures/StackTwo-v0_reset.png?ts=723506](figures/StackTwo-v0_reset.png?ts=723506) | ![figures/StackTwo-v0.gif?ts=377167](figures/StackTwo-v0.gif?ts=377167) |
