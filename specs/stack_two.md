
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
| ![figures/Stack2-table-top.gif?ts=302473](figures/Stack2-table-top.gif?ts=302473) | ![figures/Stack2-in-hand.gif?ts=038555](figures/Stack2-in-hand.gif?ts=038555) | ![figures/Stack2-obj1-in-hand.gif?ts=744472](figures/Stack2-obj1-in-hand.gif?ts=744472) | ![figures/Stack2-train.gif?ts=668926](figures/Stack2-train.gif?ts=668926) |

## Box Diagnostic Tasks

| Name                   | Observation Spec                     | Goal Init/Comment  |  |
| -----------------      | ----------------                     | -------            | ------ |
| **StackTwo-train-v0**  | achieved_goal: (6,)<br>desired_goal: (6,)<br>observation: (40,)  | Four parts<br>- table-top<br>- | in-hand<br>- obj0-at-target<br>- obj1-in-hand  | ![](figures/StackTwo-train-v0.gif) |
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
| ![figures/StackTwo-train-v0_init.png?ts=384025](figures/StackTwo-train-v0_init.png?ts=384025) | ![figures/StackTwo-train-v0_reset.png?ts=444846](figures/StackTwo-train-v0_reset.png?ts=444846) | ![figures/StackTwo-train-v0.gif?ts=974799](figures/StackTwo-train-v0.gif?ts=974799) |
| **StackTwo-v0** | **distribution** |   |
| ![figures/StackTwo-v0_init.png?ts=708338](figures/StackTwo-v0_init.png?ts=708338) | ![figures/StackTwo-v0_reset.png?ts=799202](figures/StackTwo-v0_reset.png?ts=799202) | ![figures/StackTwo-v0.gif?ts=448942](figures/StackTwo-v0.gif?ts=448942) |
