
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
| ![figures/Clean-i-v0_init.png?ts=511920](figures/Clean-i-v0_init.png?ts=511920) | ![figures/Clean-i-v0_reset.png?ts=662350](figures/Clean-i-v0_reset.png?ts=662350) | ![figures/Clean-i-v0.gif?ts=550842](figures/Clean-i-v0.gif?ts=550842) |
| **Clean-ii-v0** | **distribution** |   |
| ![figures/Clean-ii-v0_init.png?ts=230667](figures/Clean-ii-v0_init.png?ts=230667) | ![figures/Clean-ii-v0_reset.png?ts=328788](figures/Clean-ii-v0_reset.png?ts=328788) | ![figures/Clean-ii-v0.gif?ts=276853](figures/Clean-ii-v0.gif?ts=276853) |
| **Clean-train-v0** | **distribution** |   |
| ![figures/Clean-train-v0_init.png?ts=083586](figures/Clean-train-v0_init.png?ts=083586) | ![figures/Clean-train-v0_reset.png?ts=260712](figures/Clean-train-v0_reset.png?ts=260712) | ![figures/Clean-train-v0.gif?ts=392835](figures/Clean-train-v0.gif?ts=392835) |
| **Clean-v0** | **distribution** |   |
| ![figures/Clean-v0_init.png?ts=165417](figures/Clean-v0_init.png?ts=165417) | ![figures/Clean-v0_reset.png?ts=264129](figures/Clean-v0_reset.png?ts=264129) | ![figures/Clean-v0.gif?ts=193331](figures/Clean-v0.gif?ts=193331) |
| **Clean-aside-i-v0** | **distribution** |   |
| ![figures/Clean-aside-i-v0_init.png?ts=929441](figures/Clean-aside-i-v0_init.png?ts=929441) | ![figures/Clean-aside-i-v0_reset.png?ts=026328](figures/Clean-aside-i-v0_reset.png?ts=026328) | ![figures/Clean-aside-i-v0.gif?ts=821052](figures/Clean-aside-i-v0.gif?ts=821052) |
| **Clean-aside-ii-v0** | **distribution** |   |
| ![figures/Clean-aside-ii-v0_init.png?ts=583657](figures/Clean-aside-ii-v0_init.png?ts=583657) | ![figures/Clean-aside-ii-v0_reset.png?ts=678971](figures/Clean-aside-ii-v0_reset.png?ts=678971) | ![figures/Clean-aside-ii-v0.gif?ts=530760](figures/Clean-aside-ii-v0.gif?ts=530760) |
| **Clean-aside-train-v0** | **distribution** |   |
| ![figures/Clean-aside-train-v0_init.png?ts=648270](figures/Clean-aside-train-v0_init.png?ts=648270) | ![figures/Clean-aside-train-v0_reset.png?ts=826200](figures/Clean-aside-train-v0_reset.png?ts=826200) | ![figures/Clean-aside-train-v0.gif?ts=969260](figures/Clean-aside-train-v0.gif?ts=969260) |
| **Clean-aside-v0** | **distribution** |   |
| ![figures/Clean-aside-v0_init.png?ts=783935](figures/Clean-aside-v0_init.png?ts=783935) | ![figures/Clean-aside-v0_reset.png?ts=885287](figures/Clean-aside-v0_reset.png?ts=885287) | ![figures/Clean-aside-v0.gif?ts=693937](figures/Clean-aside-v0.gif?ts=693937) |
