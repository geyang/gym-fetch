
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
| ![figures/Reach-v0_init.png?ts=894257](figures/Reach-v0_init.png?ts=894257) | ![figures/Reach-v0_reset.png?ts=983500](figures/Reach-v0_reset.png?ts=983500) | ![figures/Reach-v0.gif?ts=615136](figures/Reach-v0.gif?ts=615136) |
```python
render_initial('fetch:Push-v0', row)
render_video('fetch:Push-v0', 5, row)
```

| **Push-v0** | **distribution** |   |
|:-----------:|:----------------:|:-:|
| ![figures/Push-v0_init.png?ts=716147](figures/Push-v0_init.png?ts=716147) | ![figures/Push-v0_reset.png?ts=778892](figures/Push-v0_reset.png?ts=778892) | ![figures/Push-v0.gif?ts=505363](figures/Push-v0.gif?ts=505363) |
```python
render_initial('fetch:PickPlace-v0', row)
render_video('fetch:PickPlace-v0', 5, row)
```

| **PickPlace-v0** | **distribution** |   |
|:----------------:|:----------------:|:-:|
| ![figures/PickPlace-v0_init.png?ts=731710](figures/PickPlace-v0_init.png?ts=731710) | ![figures/PickPlace-v0_reset.png?ts=800719](figures/PickPlace-v0_reset.png?ts=800719) | ![figures/PickPlace-v0.gif?ts=406236](figures/PickPlace-v0.gif?ts=406236) |
```python
render_initial('fetch:Slide-v0', row)
render_video('fetch:Slide-v0', 5, row)
```

| **Slide-v0** | **distribution** |   |
|:------------:|:----------------:|:-:|
| ![figures/Slide-v0_init.png?ts=403957](figures/Slide-v0_init.png?ts=403957) | ![figures/Slide-v0_reset.png?ts=494878](figures/Slide-v0_reset.png?ts=494878) | ![figures/Slide-v0.gif?ts=217667](figures/Slide-v0.gif?ts=217667) |
