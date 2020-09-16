from cmx import doc

from specs.__init__ import get_obs_spec, render_initial, render_video

bin_envs = ["fetch:Bin-pick-v0",
            "fetch:Bin-place-v0",
            "fetch:Bin-fixed-v0", ]
if __name__ == '__main__':
    all_envs = bin_envs
    doc @ f"""
write_protected: true
---

## Bin Diagnostic Tasks

Name              | Observation Spec                | Goal Init/Comment | 
----------------- | ----------------                | -------           | ------
**Bin-aside-v0** | {get_obs_spec('Bin-aside-v0')} | pick up the block | ![](figures/Bin-aside-v0.gif)
**Bin-fixed-v0** | {get_obs_spec('Bin-fixed-v0')} | pick up the block | ![](figures/Bin-fixed-v0.gif)

## Bin Primitive Tasks

Name                     | Observation Spec               | Goal Init/Comment                        | 
-----------------        | ----------------               | -------                                  | ------
**Bin-pick-v0**          | {get_obs_spec('Bin-pick-v0')}  | pick up the block                        | ![](figures/Bin-pick-v0.gif)
**Bin-place-v0**         | {get_obs_spec('Bin-place-v0')} | 10% on the bin, rest of the time in-air  | ![](figures/Bin-place-v0.gif)

## Other Debugging Tasks
"""
    with doc:
        debug_envs = [
            'fetch:Bin-no-bin-v0',
            'fetch:Bin-pp-xml-v0',
            'fetch:Bin-no-init-v0',
            'fetch:Bin-aside-hidden-v0',
            'fetch:Bin-aside-v0',
        ]

    doc @"""
    ## Details of Each Task
    """
    table = doc.table()
    for env_id in all_envs:
        with table.figure_row() as row:
            env = render_initial(env_id, row)
            render_video(env_id, 15, row)

            text = f"**Action Type**<br>`{env.action}`<br>"
            text += f"**Observation Spec**<br>"
            text += get_obs_spec(env_id.split(':')[-1])
            row.column(text=text)

    doc.flush()
