
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
    'fetch:Clean-v0'
]
```
| **Clean-i-v0** | **distribution** |   |
|:--------------:|:----------------:|:-:|
| ![figures/Clean-i-v0_init.png?ts=294528](figures/Clean-i-v0_init.png?ts=294528) | ![figures/Clean-i-v0_reset.png?ts=417121](figures/Clean-i-v0_reset.png?ts=417121) | ![figures/Clean-i-v0.gif?ts=179419](figures/Clean-i-v0.gif?ts=179419) |
| **Clean-ii-v0** | **distribution** |   |
| ![figures/Clean-ii-v0_init.png?ts=864703](figures/Clean-ii-v0_init.png?ts=864703) | ![figures/Clean-ii-v0_reset.png?ts=917603](figures/Clean-ii-v0_reset.png?ts=917603) | ![figures/Clean-ii-v0.gif?ts=726306](figures/Clean-ii-v0.gif?ts=726306) |
| **Clean-train-v0** | **distribution** |   |
| ![figures/Clean-train-v0_init.png?ts=629332](figures/Clean-train-v0_init.png?ts=629332) | ![figures/Clean-train-v0_reset.png?ts=794904](figures/Clean-train-v0_reset.png?ts=794904) | ![figures/Clean-train-v0.gif?ts=845322](figures/Clean-train-v0.gif?ts=845322) |
| **Clean-v0** | **distribution** |   |
| ![figures/Clean-v0_init.png?ts=499010](figures/Clean-v0_init.png?ts=499010) | ![figures/Clean-v0_reset.png?ts=603128](figures/Clean-v0_reset.png?ts=603128) | ![figures/Clean-v0.gif?ts=464708](figures/Clean-v0.gif?ts=464708) |
