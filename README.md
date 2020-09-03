
# Extended Taskset for the Fetch Robot

[![PyPI version](https://badge.fury.io/py/gym-fetch.svg)](https://badge.fury.io/py/gym-fetch)

## Installation

you can do: 

```bash
pip install gym-fetch
```

Alternatively, you can clone this repo and install under development 
mode:
```
git clone <this repo>
cd <this repo>
pip install -e .
```

## Environments

We extend existing Fetch environments from gym, with 7 new manipulation
tasks. The `gym.Fetch` environment are much better engineered than the
sawyer environments that `metaworld` uses. They are faster to initialize,
and have a small (50 step) maximum episode length, making these environments
faster to train on.

> We might or might not need to extend the `max_episode_steps` on more 
> complex tasks.


Reach-v2    | Push-v2    | PickPlace-v2 | Slide-v2    
:----------:|:----------:|:------------:|:--------:
<img style="align-self:center;" src="figures/FetchReach-v1.png" /> | <img style="align-self:center;" src="figures/FetchPush-v1.png" /> | <img style="align-self:center;" src="figures/FetchPickAndPlace-v1.png" />     | <img style="align-self:center;" src="figures/FetchSlide-v1.png" /> 


# Single Task Environments for Primitives

 Name            | Status
---------------- | -------------------------
 Bin-picking-v2  | ✅ done
 Box-open-v2     | ✅ done
 Box-close-v2    | ✅ done
 Drawer-open-v2  | ✅ done
 Drawer-close-v2 | ✅ done

The environments look like the following:

 Box-open-v0 | Box-close-v0 | Bin-picking-v0 
 :---------: | :----------: | :------------:
 <img style="align-self:center;" src="figures/Box-open-v0.png" /> | <img style="align-self:center;" src="figures/Box-close-v0.png" /> | <img style="align-self:center;" src="figures/Bin-picking-v0.png" />
 **Drawer-open-v0** | **Drawer-close-v0** | 
 <img style="align-self:center;" src="figures/Drawer-open-v0.png" /> | <img style="align-self:center;" src="figures/Drawer-close-v0.png" /> |

# Multi-task Environments

These environments require significantly more memory due
to the increasing complexity of contact detection and 
collision dynamics. These are also slower to run.


  Name            |  Render
 ---------------- | :---------------:
  BoxBin-v2       |  ✅ done
  DrawerBin-v2    |  ✅ done
  BoxBinDrawer-v2 |  ✅ done


  BoxBin-v0        | DrawerBin-v0     | BoxBinDrawer-v0   
:----------------: | :--------------: | :---------------:
<img style="align-self:center;" src="figures/BoxBin-v0.png" /> | <img style="align-self:center;" src="figures/DrawerBin-v0.png" /> | <img style="align-self:center;" src="figures/BoxBinDrawer-v0.png" />

