
write_protected: true
---

## Bin Diagnostic Tasks

Name              | Observation Spec                | Goal Init/Comment | 
----------------- | ----------------                | -------           | ------
**Bin-aside-v0** | achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (28,) | pick up the block | ![](figures/Bin-aside-v0.gif)
**Bin-fixed-v0** | achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (28,) | pick up the block | ![](figures/Bin-fixed-v0.gif)

## Bin Primitive Tasks

Name                     | Observation Spec               | Goal Init/Comment                        | 
-----------------        | ----------------               | -------                                  | ------
**Bin-pick-v0**          | achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (28,)  | pick up the block                        | ![](figures/Bin-pick-v0.gif)
**Bin-place-v0**         | achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (28,) | 10% on the bin, rest of the time in-air  | ![](figures/Bin-place-v0.gif)

## Other Debugging Tasks

```python
debug_envs = [
    'fetch:Bin-no-bin-v0',
    'fetch:Bin-pp-xml-v0',
    'fetch:Bin-no-init-v0',
    'fetch:Bin-aside-hidden-v0',
    'fetch:Bin-aside-v0',
]
```

## Details of Each Task

| **Bin-pick-v0** | **distribution** |   |   |
|:---------------:|:----------------:|:-:|:-:|
| ![figures/Bin-pick-v0_init.png?ts=082199](figures/Bin-pick-v0_init.png?ts=082199) | ![figures/Bin-pick-v0_reset.png?ts=192014](figures/Bin-pick-v0_reset.png?ts=192014) | ![figures/Bin-pick-v0.gif?ts=852221](figures/Bin-pick-v0.gif?ts=852221) | **Action Type**<br>`pick`<br>**Observation Spec**<br>achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (28,) |
| **Bin-place-v0** | **distribution** |   |   |
| ![figures/Bin-place-v0_init.png?ts=447086](figures/Bin-place-v0_init.png?ts=447086) | ![figures/Bin-place-v0_reset.png?ts=545401](figures/Bin-place-v0_reset.png?ts=545401) | ![figures/Bin-place-v0.gif?ts=103351](figures/Bin-place-v0.gif?ts=103351) | **Action Type**<br>`place+air`<br>**Observation Spec**<br>achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (28,) |
| **Bin-fixed-v0** | **distribution** |   |   |
| ![figures/Bin-fixed-v0_init.png?ts=066032](figures/Bin-fixed-v0_init.png?ts=066032) | ![figures/Bin-fixed-v0_reset.png?ts=134141](figures/Bin-fixed-v0_reset.png?ts=134141) | ![figures/Bin-fixed-v0.gif?ts=050894](figures/Bin-fixed-v0.gif?ts=050894) | **Action Type**<br>`bin-fixed`<br>**Observation Spec**<br>achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (28,) |
