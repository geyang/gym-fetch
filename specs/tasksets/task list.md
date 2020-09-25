Environments to build:

1. Box + Block + Lid env. Block uses *pick-and-place initialization distribution*. Lid will use the initialization distribution agent (2) used in the previously sent video. Combine them together in such a way that 50% of the time the goal is to only move one thing, and 50% of the time the goal is to move two things together. The goal returned from the environment should be a 6-dim vector (not a dictionary). The box should be fixed, and this can be done by simply resetting the location of the box to the original location at each simulation step.
2. Drawer + Block env. 50% of the time, the drawer is initialized to be closed; 50% of the time, the drawer is initialized to be open. Basically a mix of agent (3) and agent (4).
3. Two-Boxes + Two-Blocks env. There are a blue box and a red box, a blue block and a red block. The goal vector is the target locations for each block concatenated together. 50% of the time, the goal is to only move one block. Like the Box+Block+Lid env, the locations of the boxes should be fixed as well.

Benchmark standard HER+DDPG on all three environments. Note that, at training time, the horizon is 50; at test time, the horizon is 100. This can be done by making two envs, one for train and one for test.



For each object, there are three things that needs to be specified:

1. initial position
2. target location
3. what happens on each simulation step -- track target/fix object location etc?

We can design a DSL for this purpose:

```python
action = "box@fixed,"
```

or rather we should use:

```python
object:
    init: "uniform"
    on_step: "track", "fix position"
    target: "track"/"uniform"/"avoid box"
lid:
    init: "above@box"
    on_step: "track", "fix position"
    target: "track"/""
```

A single object + target inside a box should work, albiet it takes a little while.