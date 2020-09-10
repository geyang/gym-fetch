
# Details on the observation spaces

## Original Fetch Environments

 Env          | Obs Spec                           | Render
------------- |:----------------------------       | ----------------------
 Reach-v2     | achieved_goal: Box(3,)<br>desired_goal: Box(3,)<br>observation: Box(10,)        | <img style="align-self:center;" src="figures/FetchReach-v1.png" />
 Push-v2      | achieved_goal: Box(3,)<br>desired_goal: Box(3,)<br>observation: Box(25,)         | <img style="align-self:center;" src="figures/FetchPush-v1.png" />
 PickPlace-v2 | achieved_goal: Box(3,)<br>desired_goal: Box(3,)<br>observation: Box(25,) | <img style="align-self:center;" src="figures/FetchPickAndPlace-v1.png" />
 Slide-v2     | achieved_goal: Box(3,)<br>desired_goal: Box(3,)<br>observation: Box(25,)        | <img style="align-self:center;" src="figures/FetchSlide-v1.png" /> 

## Primitives Single Task Environments



- [ ] `compute_reward`
- [ ] `obs_space`
- [ ] `initial_pos`

 Env             | Obs Spec                              | Render
---------------- |:----------                            |:----------
 Box-open-v0     | achieved_goal: Box(3,)<br>desired_goal: Box(3,)<br>observation: Box(10,)       | <img style="align-self:center;" src="figures/Box-open-v0.png" />
 Box-close-v0    | achieved_goal: Box(3,)<br>desired_goal: Box(3,)<br>observation: Box(10,)      | <img style="align-self:center;" src="figures/Box-close-v0.png" />  
 Bin-pick-v0     | achieved_goal: Box(3,)<br>desired_goal: Box(3,)<br>observation: Box(25,)       | <img style="align-self:center;" src="figures/Bin-pick-v0.png" /> 
 Bin-place-v0    | achieved_goal: Box(3,)<br>desired_goal: Box(3,)<br>observation: Box(25,)      | <img style="align-self:center;" src="figures/Bin-place-v0.png" />
 Drawer-open-v0  | achieved_goal: Box(3,)<br>desired_goal: Box(3,)<br>observation: Box(10,)    | <img style="align-self:center;" src="figures/Drawer-open-v0.png" /> 
 Drawer-close-v0 | achieved_goal: Box(3,)<br>desired_goal: Box(3,)<br>observation: Box(10,)   | <img style="align-self:center;" src="figures/Drawer-close-v0.png" /> 

## Intermediate Task

These tasks additionally require placing the object
inside an open drawer or box. We include the `Bin-picking` 
environment for completeness.

 Name            | Obs Spec                              | Render
---------------- | :-------------                        | :-------------
 Bin-pick-v0     | achieved_goal: Box(3,)<br>desired_goal: Box(3,)<br>observation: Box(25,)       | <img style="align-self:center;" src="figures/Bin-pick-v0.png" />  
 Bin-place-v0    | achieved_goal: Box(3,)<br>desired_goal: Box(3,)<br>observation: Box(25,)      | <img style="align-self:center;" src="figures/Bin-place-v0.png" />     
 Box-place-v0    | achieved_goal: Box(3,)<br>desired_goal: Box(3,)<br>observation: Box(25,)       | <img style="align-self:center;" src="figures/Box-pick-v0.png" />  
 Box-pick-v0     | achieved_goal: Box(3,)<br>desired_goal: Box(3,)<br>observation: Box(25,)      | <img style="align-self:center;" src="figures/Box-place-v0.png" /> 
 Drawer-place-v0 | achieved_goal: Box(3,)<br>desired_goal: Box(3,)<br>observation: Box(25,)    | <img style="align-self:center;" src="figures/Drawer-pick-v0.png" />   
 Drawer-pick-v0  | achieved_goal: Box(3,)<br>desired_goal: Box(3,)<br>observation: Box(25,)   | <img style="align-self:center;" src="figures/Drawer-place-v0.png" /> 

## Multi-task Environments

These environments require significantly more memory due
to the increasing complexity of contact detection and 
collision dynamics. These are also slower to run.

 Name            | Obs Spec                               | Render
---------------- | :---------------                       | :---------------
 BoxBin-v0       | achieved_goal: Box(3,)<br>desired_goal: Box(3,)<br>observation: Box(25,)          | <img style="align-self:center;" src="figures/BoxBin-v0.png" /> 
 DrawerBin-v0    | achieved_goal: Box(3,)<br>desired_goal: Box(3,)<br>observation: Box(25,)       | <img style="align-self:center;" src="figures/DrawerBin-v0.png" />
 BoxBinDrawer-v0 | achieved_goal: Box(3,)<br>desired_goal: Box(3,)<br>observation: Box(25,)    | <img style="align-self:center;" src="figures/BoxBinDrawer-v0.png" />


