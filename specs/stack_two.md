
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
| ![figures/Stack2-table-top.gif?ts=601239](figures/Stack2-table-top.gif?ts=601239) | ![figures/Stack2-in-hand.gif?ts=397607](figures/Stack2-in-hand.gif?ts=397607) | ![figures/Stack2-obj1-in-hand.gif?ts=117524](figures/Stack2-obj1-in-hand.gif?ts=117524) | ![figures/Stack2-train.gif?ts=915199](figures/Stack2-train.gif?ts=915199) |

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
| ![figures/StackTwo-train-v0_init.png?ts=942631](figures/StackTwo-train-v0_init.png?ts=942631) | ![figures/StackTwo-train-v0_reset.png?ts=015388](figures/StackTwo-train-v0_reset.png?ts=015388) | ![figures/StackTwo-train-v0.gif?ts=666079](figures/StackTwo-train-v0.gif?ts=666079) |
| **StackTwo-fixed-v0** | **distribution** |   |
| ![figures/StackTwo-fixed-v0_init.png?ts=315603](figures/StackTwo-fixed-v0_init.png?ts=315603) | ![figures/StackTwo-fixed-v0_reset.png?ts=390113](figures/StackTwo-fixed-v0_reset.png?ts=390113) | ![figures/StackTwo-fixed-v0.gif?ts=746983](figures/StackTwo-fixed-v0.gif?ts=746983) |
| **StackTwo-fixed-pp-goals-v0** | **distribution** |   |
| ![figures/StackTwo-fixed-pp-goals-v0_init.png?ts=276419](figures/StackTwo-fixed-pp-goals-v0_init.png?ts=276419) | ![figures/StackTwo-fixed-pp-goals-v0_reset.png?ts=397402](figures/StackTwo-fixed-pp-goals-v0_reset.png?ts=397402) | ![figures/StackTwo-fixed-pp-goals-v0.gif?ts=577279](figures/StackTwo-fixed-pp-goals-v0.gif?ts=577279) |
| **StackTwo-v0** | **distribution** |   |
| ![figures/StackTwo-v0_init.png?ts=436353](figures/StackTwo-v0_init.png?ts=436353) | ![figures/StackTwo-v0_reset.png?ts=537590](figures/StackTwo-v0_reset.png?ts=537590) | ![figures/StackTwo-v0.gif?ts=979377](figures/StackTwo-v0.gif?ts=979377) |
