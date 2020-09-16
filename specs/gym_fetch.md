
# Original Gym Fetch Tasks

This set reproduces the original gym Fetch robot tasks.

Name             | Observation Spec               | Info
---------------- | ----------------               | -------
**Reach-v0**     | achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (10,)     | ![](figures/Reach-v0.gif)
**Push-v0**      | achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (25,)      | ![](figures/Push-v0.gif)
**PickPlace-v0** | achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (25,) | ![](figures/PickPlace-v0.gif)
**Slide-v0**     | achieved_goal: (3,)<br>desired_goal: (3,)<br>observation: (25,)     | ![](figures/Slide-v0.gif)


```python
render_initial('fetch:Reach-v0', row)
render_video('fetch:Reach-v0', 5, row)
```

| **Reach-v0** | **distribution** |   |
|:------------:|:----------------:|:-:|
| ![figures/Reach-v0_init.png?ts=702379](figures/Reach-v0_init.png?ts=702379) | ![figures/Reach-v0_reset.png?ts=831980](figures/Reach-v0_reset.png?ts=831980) | ![figures/Reach-v0.gif?ts=496650](figures/Reach-v0.gif?ts=496650) |
```python
render_initial('fetch:Push-v0', row)
render_video('fetch:Push-v0', 5, row)
```

| **Push-v0** | **distribution** |   |
|:-----------:|:----------------:|:-:|
| ![figures/Push-v0_init.png?ts=821917](figures/Push-v0_init.png?ts=821917) | ![figures/Push-v0_reset.png?ts=928564](figures/Push-v0_reset.png?ts=928564) | ![figures/Push-v0.gif?ts=664486](figures/Push-v0.gif?ts=664486) |
```python
render_initial('fetch:PickPlace-v0', row)
render_video('fetch:PickPlace-v0', 5, row)
```

| **PickPlace-v0** | **distribution** |   |
|:----------------:|:----------------:|:-:|
| ![figures/PickPlace-v0_init.png?ts=938748](figures/PickPlace-v0_init.png?ts=938748) | ![figures/PickPlace-v0_reset.png?ts=046546](figures/PickPlace-v0_reset.png?ts=046546) | ![figures/PickPlace-v0.gif?ts=800919](figures/PickPlace-v0.gif?ts=800919) |
```python
render_initial('fetch:Slide-v0', row)
render_video('fetch:Slide-v0', 5, row)
```

| **Slide-v0** | **distribution** |   |
|:------------:|:----------------:|:-:|
| ![figures/Slide-v0_init.png?ts=323357](figures/Slide-v0_init.png?ts=323357) | ![figures/Slide-v0_reset.png?ts=521716](figures/Slide-v0_reset.png?ts=521716) | ![figures/Slide-v0.gif?ts=520065](figures/Slide-v0.gif?ts=520065) |
