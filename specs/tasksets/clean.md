
## Task: Cleaning Table

**Primitives**
1. place A into box, both on table.
2. place B into box, with A already inside the box.

**Training Mixture**: 1 + 2, 50:50.

**Test**: Both A and B on table, and place both into the box. (edited) 

Name               | Observation Spec                 | Goal Init/Comment                        | 
-----------------  | ----------------                 | -------                                  | ------
**Clean-i-v0**     | achieved_goal: (6,)<br>desired_goal: (6,)<br>observation: (43,)     | place the first object<br>into the box | ![](figures/Clean-i-v0.gif)
**Clean-ii-v0**    | achieved_goal: (6,)<br>desired_goal: (6,)<br>observation: (43,)    | place the second object<br>into the box while the<br>first one is already in there. | ![](figures/Clean-ii-v0.gif)
**Clean-train-v0** | achieved_goal: (6,)<br>desired_goal: (6,)<br>observation: (43,) | 50/50 mixture of both | ![](figures/Clean-train-v0.gif)
**Clean-v0**       | achieved_goal: (6,)<br>desired_goal: (6,)<br>observation: (43,)       | Start with both on the<br>table, place both into<br>the box. | ![](figures/Clean-v0.gif)

```python
twin_box_envs = [
    'fetch:Clean-i-v0',
    'fetch:Clean-ii-v0',
    'fetch:Clean-train-v0',
    'fetch:Clean-v0',
    'fetch:Clean-aside-i-v0',
    'fetch:Clean-aside-ii-v0',
    'fetch:Clean-aside-train-v0',
    'fetch:Clean-aside-v0',
]
```
| **Clean-i-v0** | **distribution** |   |
|:--------------:|:----------------:|:-:|
| ![figures/Clean-i-v0_init.png?ts=893891](figures/Clean-i-v0_init.png?ts=893891) | ![figures/Clean-i-v0_reset.png?ts=020709](figures/Clean-i-v0_reset.png?ts=020709) | ![figures/Clean-i-v0.gif?ts=933636](figures/Clean-i-v0.gif?ts=933636) |
| **Clean-ii-v0** | **distribution** |   |
| ![figures/Clean-ii-v0_init.png?ts=583763](figures/Clean-ii-v0_init.png?ts=583763) | ![figures/Clean-ii-v0_reset.png?ts=661571](figures/Clean-ii-v0_reset.png?ts=661571) | ![figures/Clean-ii-v0.gif?ts=472119](figures/Clean-ii-v0.gif?ts=472119) |
| **Clean-train-v0** | **distribution** |   |
| ![figures/Clean-train-v0_init.png?ts=215769](figures/Clean-train-v0_init.png?ts=215769) | ![figures/Clean-train-v0_reset.png?ts=394996](figures/Clean-train-v0_reset.png?ts=394996) | ![figures/Clean-train-v0.gif?ts=426037](figures/Clean-train-v0.gif?ts=426037) |
| **Clean-v0** | **distribution** |   |
| ![figures/Clean-v0_init.png?ts=114485](figures/Clean-v0_init.png?ts=114485) | ![figures/Clean-v0_reset.png?ts=169328](figures/Clean-v0_reset.png?ts=169328) | ![figures/Clean-v0.gif?ts=051694](figures/Clean-v0.gif?ts=051694) |
| **Clean-aside-i-v0** | **distribution** |   |
| ![figures/Clean-aside-i-v0_init.png?ts=782709](figures/Clean-aside-i-v0_init.png?ts=782709) | ![figures/Clean-aside-i-v0_reset.png?ts=881644](figures/Clean-aside-i-v0_reset.png?ts=881644) | ![figures/Clean-aside-i-v0.gif?ts=674909](figures/Clean-aside-i-v0.gif?ts=674909) |
| **Clean-aside-ii-v0** | **distribution** |   |
| ![figures/Clean-aside-ii-v0_init.png?ts=421882](figures/Clean-aside-ii-v0_init.png?ts=421882) | ![figures/Clean-aside-ii-v0_reset.png?ts=523422](figures/Clean-aside-ii-v0_reset.png?ts=523422) | ![figures/Clean-aside-ii-v0.gif?ts=303254](figures/Clean-aside-ii-v0.gif?ts=303254) |
| **Clean-aside-train-v0** | **distribution** |   |
| ![figures/Clean-aside-train-v0_init.png?ts=385627](figures/Clean-aside-train-v0_init.png?ts=385627) | ![figures/Clean-aside-train-v0_reset.png?ts=563027](figures/Clean-aside-train-v0_reset.png?ts=563027) | ![figures/Clean-aside-train-v0.gif?ts=678045](figures/Clean-aside-train-v0.gif?ts=678045) |
| **Clean-aside-v0** | **distribution** |   |
| ![figures/Clean-aside-v0_init.png?ts=449968](figures/Clean-aside-v0_init.png?ts=449968) | ![figures/Clean-aside-v0_reset.png?ts=541597](figures/Clean-aside-v0_reset.png?ts=541597) | ![figures/Clean-aside-v0.gif?ts=397963](figures/Clean-aside-v0.gif?ts=397963) |
