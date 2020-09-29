
## Twin Box Pick and Place

Name                        | Observation Spec                   | Goal Init/Comment                                             | 
-----------------           | ----------------                   | -------                                                       | ------
**TwinBox-place-single-v0** | achieved_goal:<br>&nbsp;&nbsp;&nbsp;&nbsp;object0: (3,)<br>&nbsp;&nbsp;&nbsp;&nbsp;object1: (3,)<br>desired_goal:<br>&nbsp;&nbsp;&nbsp;&nbsp;object0: (3,)<br>&nbsp;&nbsp;&nbsp;&nbsp;object1: (3,)<br>observation: (70,)  | place a single object at target location              |  
**TwinBox-red-v0**          | achieved_goal:<br>&nbsp;&nbsp;&nbsp;&nbsp;object0: (3,)<br>&nbsp;&nbsp;&nbsp;&nbsp;object1: (3,)<br>desired_goal:<br>&nbsp;&nbsp;&nbsp;&nbsp;object0: (3,)<br>&nbsp;&nbsp;&nbsp;&nbsp;object1: (3,)<br>observation: (70,)   | place <span color="red">red</span> block at target location   | ![](figures/TwinBox-red-v0.gif)
**TwinBox-blue-v0**         | achieved_goal:<br>&nbsp;&nbsp;&nbsp;&nbsp;object0: (3,)<br>&nbsp;&nbsp;&nbsp;&nbsp;object1: (3,)<br>desired_goal:<br>&nbsp;&nbsp;&nbsp;&nbsp;object0: (3,)<br>&nbsp;&nbsp;&nbsp;&nbsp;object1: (3,)<br>observation: (70,)  | place <span color="blue">blue</span> block at target location | ![](figures/TwinBox-blue-v0.gif)
**TwinBox-mixed-v0**        | achieved_goal:<br>&nbsp;&nbsp;&nbsp;&nbsp;object0: (3,)<br>&nbsp;&nbsp;&nbsp;&nbsp;object1: (3,)<br>desired_goal:<br>&nbsp;&nbsp;&nbsp;&nbsp;object0: (3,)<br>&nbsp;&nbsp;&nbsp;&nbsp;object1: (3,)<br>observation: (70,) | place either one to target location                           | ![](figures/TwinBox-mixed-v0.gif)                     
**TwinBox-place-v0**        | achieved_goal:<br>&nbsp;&nbsp;&nbsp;&nbsp;object0: (3,)<br>&nbsp;&nbsp;&nbsp;&nbsp;object1: (3,)<br>desired_goal:<br>&nbsp;&nbsp;&nbsp;&nbsp;object0: (3,)<br>&nbsp;&nbsp;&nbsp;&nbsp;object1: (3,)<br>observation: (70,) | place both objects to target location                         | ![](figures/TwinBox-place-v0.gif)

```python
twin_box_envs = [
    'fetch:TwinBox-v0',
    'fetch:TwinBox-place-red-v0',
    'fetch:TwinBox-place-blue-v0',
    'fetch:TwinBox-place-train-v0',
    'fetch:TwinBox-place-v0',
]
```

So the tasks will be:

**Primitives**

1. place A into box, both on table.
2. place B into box, with A already inside the box.

**Training Mixture**

1 + 2, 50:50.

**Test**

both A and B on table, and place both into the box. (edited) 