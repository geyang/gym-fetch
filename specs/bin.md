
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
| ![figures/Bin-pick-v0_init.png?ts=716853](figures/Bin-pick-v0_init.png?ts=716853) | ![figures/Bin-pick-v0_reset.png?ts=835836](figures/Bin-pick-v0_reset.png?ts=835836) | ![figures/Bin-pick-v0.gif?ts=375946](figures/Bin-pick-v0.gif?ts=375946) | **Action Type**<br>`pick`<br>**Observation Spec**<br>achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (28,) |
| **Bin-place-v0** | **distribution** |   |   |
| ![figures/Bin-place-v0_init.png?ts=241094](figures/Bin-place-v0_init.png?ts=241094) | ![figures/Bin-place-v0_reset.png?ts=361204](figures/Bin-place-v0_reset.png?ts=361204) | ![figures/Bin-place-v0.gif?ts=045073](figures/Bin-place-v0.gif?ts=045073) | **Action Type**<br>`place+air`<br>**Observation Spec**<br>achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (28,) |
| **Bin-fixed-v0** | **distribution** |   |   |
| ![figures/Bin-fixed-v0_init.png?ts=458766](figures/Bin-fixed-v0_init.png?ts=458766) | ![figures/Bin-fixed-v0_reset.png?ts=511724](figures/Bin-fixed-v0_reset.png?ts=511724) | ![figures/Bin-fixed-v0.gif?ts=967211](figures/Bin-fixed-v0.gif?ts=967211) | **Action Type**<br>`bin-fixed`<br>**Observation Spec**<br>achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (28,) |
