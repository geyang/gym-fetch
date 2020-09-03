import gym
from cmx import doc
from cmx.backends.components import Image


def render(env_id):
    env = gym.make(env_id)
    env.reset()
    img = env.render('rgb_array', width=120, height=80)
    fname = f"figures/{env_id}.png"
    doc.logger.save_image(img, fname)
    md = Image(src=fname)._md.rstrip()
    return md


doc @ f"""
Box-open-v0 | Box-close-v0 | Bin-picking-v0 
----------- | ------------ | --------------
{render('fetch:Box-open-v0')} | {render('fetch:Box-close-v0')} | {render('fetch:Bin-picking-v0')}
**Drawer-open-v0** | **Drawer-close-v0** | 
{render('fetch:Drawer-open-v0')} | {render('fetch:Drawer-close-v0')} |
"""

doc.flush()
