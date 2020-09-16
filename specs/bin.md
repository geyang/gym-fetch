
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
| ![figures/Bin-pick-v0_init.png?ts=130087](figures/Bin-pick-v0_init.png?ts=130087) | ![figures/Bin-pick-v0_reset.png?ts=225915](figures/Bin-pick-v0_reset.png?ts=225915) | ![figures/Bin-pick-v0.gif?ts=854656](figures/Bin-pick-v0.gif?ts=854656) | **Action Type**<br>`pick`<br>**Observation Spec**<br>achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (28,) |
| **Bin-place-v0** | **distribution** |   |   |
| ![figures/Bin-place-v0_init.png?ts=349199](figures/Bin-place-v0_init.png?ts=349199) | ![figures/Bin-place-v0_reset.png?ts=440322](figures/Bin-place-v0_reset.png?ts=440322) | ![figures/Bin-place-v0.gif?ts=055376](figures/Bin-place-v0.gif?ts=055376) | **Action Type**<br>`place+air`<br>**Observation Spec**<br>achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (28,) |
| **Bin-fixed-v0** | **distribution** |   |   |
| ![figures/Bin-fixed-v0_init.png?ts=480324](figures/Bin-fixed-v0_init.png?ts=480324) | ![figures/Bin-fixed-v0_reset.png?ts=574952](figures/Bin-fixed-v0_reset.png?ts=574952) | ![figures/Bin-fixed-v0.gif?ts=257580](figures/Bin-fixed-v0.gif?ts=257580) | **Action Type**<br>`bin-fixed`<br>**Observation Spec**<br>achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (28,) |
