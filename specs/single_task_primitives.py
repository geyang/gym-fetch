from cmx import doc
import gym
from cmx.backends.components import Image

doc @ """
# Benchmarking on Extended Tasksets

First we make sure that the single task environments are okay.

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
 {render('fetch:Box-open-v0', 0.7)} | {render('fetch:Box-close-v0')} | {render('fetch:Bin-pick-v0', 0.7)} | {render('fetch:Bin-place-v0', 0.7)}
 **Drawer-open-v0** | **Drawer-close-v0** | 
 {render('fetch:Drawer-open-v0')} | {render('fetch:Drawer-close-v0')} |
"""

if __name__ == '__main__':
    doc.flush()
