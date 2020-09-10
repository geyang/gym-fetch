from cmx import doc
import gym
from cmx.backends.components import Image



def obs_spec(env_id):
    env = gym.make(env_id)
    env.reset()
    spec = env.observation_space.spaces
    return "<br>".join([f"{k}: {v}" for k, v in spec.items()])


def render(env_id, crop=0.4, width=300, height=100):
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
# Details on the observation spaces

## Original Fetch Environments

 Env          | Obs Spec                           | Render
------------- |:----------------------------       | ----------------------
 Reach-v2     | {obs_spec('FetchReach-v1')}        | {render('FetchReach-v1')}
 Push-v2      | {obs_spec('FetchPush-v1')}         | {render('FetchPush-v1')}
 PickPlace-v2 | {obs_spec('FetchPickAndPlace-v1')} | {render('FetchPickAndPlace-v1')}
 Slide-v2     | {obs_spec('FetchSlide-v1')}        | {render('FetchSlide-v1')} 

## Single Task Primitives

- [ ] `compute_reward`
- [ ] `obs_space`
- [ ] `initial_pos`

 Env             | Obs Spec                              | Render
---------------- |:----------                            |:----------
 Box-open-v0     | {obs_spec('fetch:Box-open-v0')}       | {render('fetch:Box-open-v0')}
 Box-close-v0    | {obs_spec('fetch:Box-close-v0')}      | {render('fetch:Box-close-v0')}  
 Bin-pick-v0     | {obs_spec('fetch:Bin-pick-v0')}       | {render('fetch:Bin-pick-v0')} 
 Bin-place-v0    | {obs_spec('fetch:Bin-place-v0')}      | {render('fetch:Bin-place-v0')}
 Drawer-open-v0  | {obs_spec('fetch:Drawer-open-v0')}    | {render('fetch:Drawer-open-v0')} 
 Drawer-close-v0 | {obs_spec('fetch:Drawer-close-v0')}   | {render('fetch:Drawer-close-v0')} 

## Intermediate Task

These tasks additionally require placing the object
inside an open drawer or box. We include the `Bin-picking` 
environment for completeness.

 Name            | Obs Spec                              | Render
---------------- | :-------------                        | :-------------
 Bin-pick-v0     | {obs_spec('fetch:Bin-pick-v0')}       | {render('fetch:Bin-pick-v0')}  
 Bin-place-v0    | {obs_spec('fetch:Bin-place-v0')}      | {render('fetch:Bin-place-v0')}     
 Box-place-v0    | {obs_spec('fetch:Box-pick-v0')}       | {render('fetch:Box-pick-v0')}  
 Box-pick-v0     | {obs_spec('fetch:Box-place-v0')}      | {render('fetch:Box-place-v0')} 
 Drawer-place-v0 | {obs_spec('fetch:Drawer-pick-v0')}    | {render('fetch:Drawer-pick-v0')}   
 Drawer-pick-v0  | {obs_spec('fetch:Drawer-place-v0')}   | {render('fetch:Drawer-place-v0')} 

## Multi-task Environments

These environments require significantly more memory due
to the increasing complexity of contact detection and 
collision dynamics. These are also slower to run.

 Name            | Obs Spec                               | Render
---------------- | :---------------                       | :---------------
 BoxBin-v0       | {obs_spec('fetch:BoxBin-v0')}          | {render('fetch:BoxBin-v0')} 
 DrawerBin-v0    | {obs_spec('fetch:DrawerBin-v0')}       | {render('fetch:DrawerBin-v0')}
 BoxBinDrawer-v0 | {obs_spec('fetch:BoxBinDrawer-v0')}    | {render('fetch:BoxBinDrawer-v0')}

"""

if __name__ == '__main__':
    doc.flush()
