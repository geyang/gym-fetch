
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
| ![figures/Stack2-table-top.gif?ts=479858](figures/Stack2-table-top.gif?ts=479858) | ![figures/Stack2-in-hand.gif?ts=514154](figures/Stack2-in-hand.gif?ts=514154) | ![figures/Stack2-obj1-in-hand.gif?ts=501400](figures/Stack2-obj1-in-hand.gif?ts=501400) | ![figures/Stack2-train.gif?ts=389946](figures/Stack2-train.gif?ts=389946) |

## Box Diagnostic Tasks

| Name                   | Observation Spec                     | Goal Init/Comment  |  |
| -----------------      | ----------------                     | -------            | ------ |
| **StackTwo-train-v0**  | achieved_goal: (6,)<br>desired_goal: (6,)<br>observation: (40,)  | Three parts<br>- table-top<br>- in-hand<br>- obj1-in-hand  | ![](figures/StackTwo-train-v0.gif) |
| **StackTwo-fixed-v0**  | achieved_goal: (6,)<br>desired_goal: (6,)<br>observation: (40,)  | object 0 welded in-place | ![](figures/StackTwo-fixed-v0.gif) |
| **StackTwo-v0**        | achieved_goal: (6,)<br>desired_goal: (6,)<br>observation: (40,)        |                    | ![](figures/StackTwo-v0.gif) |

## Details of Each Task

```python
box_envs = [
    "fetch:StackTwo-train-v0",
    "fetch:StackTwo-fixed-v0",
    "fetch:StackTwo-v0",
]
```
| **StackTwo-train-v0** | **distribution** |   |
|:---------------------:|:----------------:|:-:|
| ![figures/StackTwo-train-v0_init.png?ts=500745](figures/StackTwo-train-v0_init.png?ts=500745) | ![figures/StackTwo-train-v0_reset.png?ts=587610](figures/StackTwo-train-v0_reset.png?ts=587610) | ![figures/StackTwo-train-v0.gif?ts=388590](figures/StackTwo-train-v0.gif?ts=388590) |
| **StackTwo-fixed-v0** | **distribution** |   |
| ![figures/StackTwo-fixed-v0_init.png?ts=233963](figures/StackTwo-fixed-v0_init.png?ts=233963) | ![figures/StackTwo-fixed-v0_reset.png?ts=379702](figures/StackTwo-fixed-v0_reset.png?ts=379702) | ![figures/StackTwo-fixed-v0.gif?ts=065258](figures/StackTwo-fixed-v0.gif?ts=065258) |
| **StackTwo-v0** | **distribution** |   |
| ![figures/StackTwo-v0_init.png?ts=641185](figures/StackTwo-v0_init.png?ts=641185) | ![figures/StackTwo-v0_reset.png?ts=730559](figures/StackTwo-v0_reset.png?ts=730559) | ![figures/StackTwo-v0.gif?ts=391736](figures/StackTwo-v0.gif?ts=391736) |
