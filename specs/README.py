from cmx import doc
import gym
from cmx.backends.components import Image

doc @ """
# Extended Taskset for the Fetch Robot

## Lsit of environments

Existing Fetch environments from gym
"""


def render(env_id, width=240, height=160):
    env = gym.make(env_id)
    env.reset()
    img = env.render('rgb_array', width=width, height=height or width)
    fname = f"figures/{env_id.split(':')[-1]}.png"
    doc.logger.save_image(img, fname)
    md = Image(src=fname)._md.rstrip()
    return md


doc @ f"""
Reach-v2    | Push-v2    | PickPlace-v2 | Slide-v2    
:----------:|:----------:|:------------:|:--------:
{render('FetchReach-v1')} | {render('FetchPush-v1')} | {render('FetchPickAndPlace-v1')}     | {render('FetchSlide-v1')} 
"""
doc @ f"""
Single Task Environments for Primitives

 Name            | Render
---------------- | -------------------------
 Bin-picking-v2  | 📈 In Progress
 Box-open-v2     | 📈 In Progress
 Box-close-v2    | 📈 In Progress
 Drawer-open-v2  | 📈 In Progress
 Drawer-close-v2 | 📈 In Progress

The environments look like the following:

Box-open-v0 | Box-close-v0 | Bin-picking-v0 
----------- | ------------ | --------------
{render('fetch:Box-open-v0')} | {render('fetch:Box-close-v0')} | {render('fetch:Bin-picking-v0')}
**Drawer-open-v0** | **Drawer-close-v0** | 
{render('fetch:Drawer-open-v0')} | {render('fetch:Drawer-close-v0')} |
"""

doc.flush()
