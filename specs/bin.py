import gym
from cmx import doc
from cmx.backends.components import Image


def render(env_id, width=240, height=160):
    env = gym.make(env_id)
    env.reset()
    img = env.render('rgb_array', width=width, height=height or width)
    fname = f"figures/{env_id.split(':')[-1]}.png"
    doc.logger.save_image(img.copy(), fname)
    md = Image(src=fname)._md.rstrip()
    env.close()
    return md


doc @ f"""
Box-open-v0 | Box-close-v0 | Bin-picking-v0 
----------- | ------------ | --------------
{render('fetch:Box-open-v0')} | {render('fetch:Box-close-v0')} | {render('fetch:Bin-picking-v0')}
**Drawer-open-v0** | **Drawer-close-v0** | 
{render('fetch:Drawer-open-v0')} | {render('fetch:Drawer-close-v0')} |
"""

import numpy as np

doc.print(np.array([255, 84, 152, 255]) / 255)

doc.flush()
