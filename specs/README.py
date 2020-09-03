from cmx import doc
import gym
from cmx.backends.components import Image

doc @ """
# Extended Taskset for the Fetch Robot

## Lsit of environments

Existing Fetch environments from gym
"""


def render(env_id):
    env = gym.make(env_id)
    env.reset()
    img = env.render('rgb_array', width=120, height=80)
    fname = f"figures/{env_id}.png"
    doc.logger.save_image(img, fname)
    md = Image(src=fname)._md.rstrip()
    return md


doc @ f"""
  Name         | Render
-------------- | -------------------------
  Reach-v2     | {render('FetchReach-v1')}
  Push-v2      | {render('FetchPush-v1')}
  PickPlace-v2 | {render('FetchPickAndPlace-v1')}     
  Slide-v2     | {render('FetchSlide-v1')}          
"""

doc @ f"""
New environments we want to build

 Name            | Render
---------------- | -------------------------
 Bin-picking-v2  | 📈 In Progress
 Box-open-v2     | 
 Box-close-v2    | 
 Drawer-open-v2  | 
 Drawer-close-v2 | 
"""

doc.flush()
