
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
| ![figures/Stack2-table-top.gif?ts=932615](figures/Stack2-table-top.gif?ts=932615) | ![figures/Stack2-in-hand.gif?ts=893635](figures/Stack2-in-hand.gif?ts=893635) | ![figures/Stack2-obj1-in-hand.gif?ts=506292](figures/Stack2-obj1-in-hand.gif?ts=506292) | ![figures/Stack2-train.gif?ts=397742](figures/Stack2-train.gif?ts=397742) |

## Box Diagnostic Tasks

| Name                   | Observation Spec                     | Goal Init/Comment  |  |
| -----------------      | ----------------                     | -------            | ------ |
| **StackTwo-train-v0**  | achieved_goal: (6,)<br>desired_goal: (6,)<br>observation: (40,)  | Three parts<br>- table-top<br>- obj0-at-target<br>- obj1-in-hand | ![](figures/StackTwo-train-v0.gif) |
| **StackTwo-v0**        | achieved_goal: (6,)<br>desired_goal: (6,)<br>observation: (40,)        |                    | ![](figures/StackTwo-v0.gif) |

## Details of Each Task

```python
box_envs = [
    "fetch:StackTwo-train-v0",
    "fetch:StackTwo-v0",
]
```
| **StackTwo-train-v0** | **distribution** |   |
|:---------------------:|:----------------:|:-:|
| ![figures/StackTwo-train-v0_init.png?ts=147765](figures/StackTwo-train-v0_init.png?ts=147765) | ![figures/StackTwo-train-v0_reset.png?ts=218797](figures/StackTwo-train-v0_reset.png?ts=218797) | ![figures/StackTwo-train-v0.gif?ts=630259](figures/StackTwo-train-v0.gif?ts=630259) |
| **StackTwo-v0** | **distribution** |   |
| ![figures/StackTwo-v0_init.png?ts=174984](figures/StackTwo-v0_init.png?ts=174984) | ![figures/StackTwo-v0_reset.png?ts=237400](figures/StackTwo-v0_reset.png?ts=237400) | ![figures/StackTwo-v0.gif?ts=871804](figures/StackTwo-v0.gif?ts=871804) |
