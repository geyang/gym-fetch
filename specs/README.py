from cmx import doc
import gym
from cmx.backends.components import Image

doc @ """
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
"""


def render(env_id, crop=0.4, width=960, height=640):
    env = gym.make(env_id)
    env.reset()
    width = width / crop
    height = height / crop

    img = env.render('rgb_array', width=width, height=height or width)
    fname = f"figures/{env_id.split(':')[-1]}.png"

    pad = (1 - crop) / 2
    w = slice(int(pad * width), int(-pad * width) or None)
    h = slice(int(pad * height), int(-pad * height) or None)
    doc.logger.save_image(img[h, w], fname)
    md = Image(src=fname)._md.rstrip()
    env.close()
    return md


doc @ f"""
Reach-v2    | Push-v2    | PickPlace-v2 | Slide-v2    
:----------:|:----------:|:------------:|:--------:
{render('FetchReach-v1', 1)} | {render('FetchPush-v1', 1)} | {render('FetchPickAndPlace-v1', 1)}     | {render('FetchSlide-v1', 1)} 
"""
doc @ f"""
# Primitive Single Task Environments

The tasks involve a single primitive action such as
open/closing a box, or a drawer. They do not additionally
involve placing an object into the opened drawer or box.
We include bin picking and placing because the bin does
not require additional actions to open.

 Name            | Status           | Details                                             | Reward              | Goal 
---------------- | ---------------- | --------------------------------------------------- | ------------------- | ------
 Bin-pick-v2     | 📈 in progress   | Pick up the object from the bin, and place out side | 𝛅(obj, goal) < ε    | flat cylinder on bin
 Bin-place-v2    | 📈 in progress   | Place the object into the bin                       | 𝛅(obj, goal) < ε    | flat cylinder on table
 Box-open-v2     | 📈 in progress   | Open the lid of the box, place on the side          | 𝛅(lid, goal) < ε    | flat cylinder on table
 Box-close-v2    | 📈 in progress   | Close the box with its lid                          | 𝛅(lid, goal) < ε    | sphere in air above box
 Drawer-open-v2  | 📈 in progress   | open the drawer by pulling it                       | 𝛅(drawer, goal) < ε | sphere in air
 Drawer-close-v2 | 📈 in progress   | close the drawer by pushing it in                   | 𝛅(drawer, goal) < ε | sphere in air

 Box-open-v0 | Box-close-v0 | Bin-pick-v0 | Bin-place-v0
 :---------: | :----------: | :---------: | :----------: 
 {render('fetch:Box-open-v0', 0.7)} | {render('fetch:Box-close-v0')} | {render('fetch:Bin-pick-v0', 0.7)} | {render('fetch:Bin-place-v0', 0.7)}
 **Drawer-open-v0** | **Drawer-close-v0** | 
 {render('fetch:Drawer-open-v0')} | {render('fetch:Drawer-close-v0')} |

# Intermediate Task

These tasks additionally require placing the object
inside an open drawer or box. We include the `Bin-picking` 
environment for completeness.

 Name            | Status
---------------- | --------------
 Bin-pick-v2     | ✅ done
 Bin-place-v2    | ✅ done
 Box-place-v2    | ✅ done
 Box-pick-v2     | ✅ done
 Drawer-place-v2 | ✅ done
 Drawer-pick-v2  | ✅ done

 Bin-pick-v0 | Bin-place-v0 | Box-pick-v0  | Box-place-v0 
 :---------: | :----------: | :----------: | :----------:
 {render('fetch:Bin-pick-v0', 0.7)} | {render('fetch:Bin-place-v0')} | {render('fetch:Box-pick-v0', 0.7)} | {render('fetch:Box-place-v0', 0.7)}
 **Drawer-pick-v0** | **Drawer-place-v0 ** |
 {render('fetch:Drawer-pick-v0')} | {render('fetch:Drawer-place-v0')} |

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
{render('fetch:BoxBin-v0')} | {render('fetch:DrawerBin-v0')} | {render('fetch:BoxBinDrawer-v0')}
"""

render('fetch:Drawer-open-v0')

if __name__ == '__main__':
    doc.flush()
