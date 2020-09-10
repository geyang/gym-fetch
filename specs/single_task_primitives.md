
# Benchmarking on Extended Tasksets

First we make sure that the single task environments are okay.



## Single Task Environments for Primitives

The tasks involve a single primitive action such as
open/closing a box, or a drawer. They do not additionally
involve placing an object into the opened drawer or box.
We include bin picking and placing because the bin does
not require additional actions to open.

To keep it simple, we use the <span style="color:red">red marker</span>
to indicate the goal. In the future we might want to use something more
visually indicative, such as a cylinder projected onto the surface
to indicate the goal location.

 Name            | Status         | Details                                             | Reward              | Goal 
---------------- | -------------- | --------------------------------------------------- | ------------------- | ------
 Bin-pick-v2     | 📈 in progress | Pick up the object from the bin, and place out side | 𝛅(obj, goal) < ε    | flat cylinder on bin
 Bin-place-v2    | 📈 in progress | Place the object into the bin                       | 𝛅(obj, goal) < ε    | flat cylinder on table
 Box-open-v2     | 📈 in progress | Open the lid of the box, place on the side          | 𝛅(lid, goal) < ε    | flat cylinder on table
 Box-close-v2    | 📈 in progress | Close the box with its lid                          | 𝛅(lid, goal) < ε    | sphere in air above box
 Drawer-open-v2  | 📈 in progress | open the drawer by pulling it                       | 𝛅(drawer, goal) < ε | sphere in air
 Drawer-close-v2 | 📈 in progress | close the drawer by pushing it in                   | 𝛅(drawer, goal) < ε | sphere in air

 Box-open-v0 | Box-close-v0 | Bin-pick-v0 | Bin-place-v0
 :---------: | :----------: | :---------: | :----------: 
 <img style="align-self:center;" src="figures/Box-open-v0.png" /> | <img style="align-self:center;" src="figures/Box-close-v0.png" /> | <img style="align-self:center;" src="figures/Bin-pick-v0.png" /> | <img style="align-self:center;" src="figures/Bin-place-v0.png" />
 **Drawer-open-v0** | **Drawer-close-v0** | 
 <img style="align-self:center;" src="figures/Drawer-open-v0.png" /> | <img style="align-self:center;" src="figures/Drawer-close-v0.png" /> |

