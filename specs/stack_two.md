
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
| ![figures/Stack2-table-top.gif?ts=122700](figures/Stack2-table-top.gif?ts=122700) | ![figures/Stack2-in-hand.gif?ts=064586](figures/Stack2-in-hand.gif?ts=064586) | ![figures/Stack2-obj1-in-hand.gif?ts=103504](figures/Stack2-obj1-in-hand.gif?ts=103504) | ![figures/Stack2-train.gif?ts=954536](figures/Stack2-train.gif?ts=954536) |

## Box Diagnostic Tasks

| Name                   | Observation Spec                     | Goal Init/Comment  |  |
| -----------------      | ----------------                     | -------            | ------ |
| **StackTwo-train-v0**  | {get_obs_spec('StackTwo-train-v0')}  | Four parts<br>- table-top<br>- | in-hand<br>- obj0-at-target<br>- obj1-in-hand  | ![](figures/StackTwo-train-v0.gif) |
| **StackTwo-v0**        | {get_obs_spec('StackTwo-v0')}        |                    | ![](figures/StackTwo-v0.gif) |

## Details of Each Task

```python
box_envs = [
    "fetch:StackTwo-train-v0",
    "fetch:StackTwo-v0",
]
```
| **StackTwo-train-v0** | **distribution** |   |
|:---------------------:|:----------------:|:-:|
| ![figures/StackTwo-train-v0_init.png?ts=420113](figures/StackTwo-train-v0_init.png?ts=420113) | ![figures/StackTwo-train-v0_reset.png?ts=523333](figures/StackTwo-train-v0_reset.png?ts=523333) | ![figures/StackTwo-train-v0.gif?ts=092798](figures/StackTwo-train-v0.gif?ts=092798) |
| **StackTwo-v0** | **distribution** |   |
| ![figures/StackTwo-v0_init.png?ts=659495](figures/StackTwo-v0_init.png?ts=659495) | ![figures/StackTwo-v0_reset.png?ts=760393](figures/StackTwo-v0_reset.png?ts=760393) | ![figures/StackTwo-v0.gif?ts=443791](figures/StackTwo-v0.gif?ts=443791) |
