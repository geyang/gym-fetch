from cmx import doc
from specs.__init__ import render_initial, render_video, get_obs_spec

if __name__ == '__main__':
    doc @ f"""
    # Original Gym Fetch Tasks

    This set reproduces the original gym Fetch robot tasks.

    Name             | Observation Spec               | Info
    ---------------- | ----------------               | -------
    **Reach-v0**     | {get_obs_spec('Reach-v0')}     | ![](figures/Reach-v0.gif)
    **Push-v0**      | {get_obs_spec('Push-v0')}      | ![](figures/Push-v0.gif)
    **PickPlace-v0** | {get_obs_spec('PickPlace-v0')} | ![](figures/PickPlace-v0.gif)
    **Slide-v0**     | {get_obs_spec('Slide-v0')}     | ![](figures/Slide-v0.gif)
    """
    with doc, doc.table().figure_row() as row:
        render_initial('fetch:Reach-v0', row)
        render_video('fetch:Reach-v0', 5, row)

    with doc, doc.table().figure_row() as row:
        render_initial('fetch:Push-v0', row)
        render_video('fetch:Push-v0', 5, row)

    with doc, doc.table().figure_row() as row:
        render_initial('fetch:PickPlace-v0', row)
        render_video('fetch:PickPlace-v0', 5, row)

    with doc, doc.table().figure_row() as row:
        render_initial('fetch:Slide-v0', row)
        render_video('fetch:Slide-v0', 5, row)

    doc.flush()
