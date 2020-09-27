
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
| ![figures/Stack2-table-top.gif?ts=225858](figures/Stack2-table-top.gif?ts=225858) | ![figures/Stack2-in-hand.gif?ts=977857](figures/Stack2-in-hand.gif?ts=977857) | ![figures/Stack2-obj1-in-hand.gif?ts=729874](figures/Stack2-obj1-in-hand.gif?ts=729874) | ![figures/Stack2-train.gif?ts=524380](figures/Stack2-train.gif?ts=524380) |

## Box Diagnostic Tasks
Name                   | Observation Spec                     | Goal Init/Comment  | 
-----------------      | ----------------                     | -------            | ------
**StackTwo-train-v0**  | {get_obs_spec('StackTwo-train-v0')}  | Four parts<br>- table-top<br>- in-hand<br>- obj0-at-target<br>- obj1-in-hand  | ![](figures/StackTwo-train-v0.gif)
**StackTwo-v0**        | {get_obs_spec('StackTwo-v0')}        |                    | ![](figures/StackTwo-v0.gif)

## Details of Each Task

```python
box_envs = [
    "fetch:StackTwo-train-v0",
    "fetch:StackTwo-v0",
]
```
| **StackTwo-train-v0** | **distribution** |   |
|:---------------------:|:----------------:|:-:|
| ![figures/StackTwo-train-v0_init.png?ts=966280](figures/StackTwo-train-v0_init.png?ts=966280) | ![figures/StackTwo-train-v0_reset.png?ts=038967](figures/StackTwo-train-v0_reset.png?ts=038967) | ![figures/StackTwo-train-v0.gif?ts=577267](figures/StackTwo-train-v0.gif?ts=577267) |
| **StackTwo-v0** | **distribution** |   |
| ![figures/StackTwo-v0_init.png?ts=996927](figures/StackTwo-v0_init.png?ts=996927) | ![figures/StackTwo-v0_reset.png?ts=059601](figures/StackTwo-v0_reset.png?ts=059601) | ![figures/StackTwo-v0.gif?ts=564203](figures/StackTwo-v0.gif?ts=564203) |
