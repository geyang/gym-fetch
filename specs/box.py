import gym
from cmx import doc
from cmx.backends.components import Image


def render(env_id, width=240, height=160):
    env = gym.make(env_id)
    env.reset()
    img = env.render('rgb_array', width=width, height=height or width)
    fname = f"{__file__[:-3]}/{env_id.split(':')[-1]}.png"
    doc.logger.save_image(img.copy(), fname)
    md = Image(src=fname)._md.rstrip()
    env.close()
    return md


doc @ f"""
| Box-open-v0 |
|:-----------:|
|{render('fetch:Bin-picking-v0', width=960, height=640)}|
"""

import numpy as np
doc.print(np.array([128, 176, 255, 255]) / 255)


if __name__ == '__main__':
    doc.flush()
