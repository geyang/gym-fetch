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
 {render('fetch:Box-open-v0', 0.7)} | {render('fetch:Box-close-v0')} | {render('fetch:Bin-picking-v0', 0.7)}
 **Drawer-open-v0** | **Drawer-close-v0** | 
 {render('fetch:Drawer-open-v0')} | {render('fetch:Drawer-close-v0')} |

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
