
# Extended Taskset for the Fetch Robot

[![PyPI version](https://badge.fury.io/py/gym-fetch.svg)](https://badge.fury.io/py/gym-fetch)

## Installation (from PyPI)

you can install the newest version via

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

## Cloning and Installing A Specific Version

**For those who do not use pip**, you can pull/checkout specific versions of the repository using a git `tag`. Github integrates with git, such that it shows tagged versions under the `<project-repo>/releases` URL. You can check out the releases for this repo at https://github.com/geyang/gym-fetch/releases. To pull a specific version, just run: 

```
git checkout v0.1.0-rc5
```

After git clone, the structure of the project is

```bash
$ tree . -L 1
gym-fetch
├── fetch
└── specs
```

To install, you can use pip

```bash
pip install -e .
```

Alternatively, you can include the [./gym-fetch](./) directory as part of your `PYTHONPATH`.

## Environments for Latent-Planning

- `Box`





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
<img style="align-self:center;" src="figures/Reach-v0.png" /> | <img style="align-self:center;" src="figures/Push-v0.png" /> | <img style="align-self:center;" src="figures/PickPlace-v0.png" />     | <img style="align-self:center;" src="figures/Slide-v0.png" /> 

## For Up-To-Date Environment Documentation

All documentations are maintained in the [./specs](specs) folder, where each task set is one markdown file.

- **original gym fetch tasks**: [./specs/gym_fetch.md](./specs/gym_fetch.md)
- **`bin` tasks**: [./specs/bin.md](./specs/bin.md)
- **`bin_debug` tasks**: [./specs/bin_debug.md](./specs/bin_debug.md)
- **`box` tasks**: [./specs/box.md](./specs/box.md)
- **`drawer` tasks**: [./specs/drawer.md](./specs/drawer.md)

The multi-task environments are still under development. They are located under

```bash
 fetch
 ├── tasksets
     ├── box_block.md
     ├── box_block.py
```



## Primitive Single Task Environments

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
 <img style="align-self:center;" src="figures/Box-open-v0.png" /> | <img style="align-self:center;" src="figures/Box-close-v0.png" /> | <img style="align-self:center;" src="figures/Bin-pick-v0.png" /> | <img style="align-self:center;" src="figures/Bin-place-v0.png" />
 **Drawer-open-v0** | **Drawer-close-v0** | 
 <img style="align-self:center;" src="figures/Drawer-open-v0.png" /> | <img style="align-self:center;" src="figures/Drawer-close-v0.png" /> |

## Intermediate Task

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
 <img style="align-self:center;" src="figures/Bin-pick-v0.png" /> | <img style="align-self:center;" src="figures/Bin-place-v0.png" /> | <img style="align-self:center;" src="figures/Box-pick-v0.png" /> | <img style="align-self:center;" src="figures/Box-place-v0.png" />
 **Drawer-pick-v0** | **Drawer-place-v0 ** |
 <img style="align-self:center;" src="figures/Drawer-pick-v0.png" /> | <img style="align-self:center;" src="figures/Drawer-place-v0.png" /> |

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

