from textwrap import dedent

from cmx import doc

from specs.__init__ import get_obs_spec, render_initial, render_video

if __name__ == '__main__':
    doc @ f"""
    ## Bin Tasks for Debugging
    """
    with doc:
        bin_debug_envs = [
            'fetch:Bin-no-bin-v0',
            'fetch:Bin-pp-xml-v0',
            'fetch:Bin-no-init-v0',
            'fetch:Bin-aside-hidden-v0',
            'fetch:Bin-aside-v0',
        ]
    table = doc.table()
    for env_id in bin_debug_envs:
        with table.figure_row() as row:
            env = render_initial(env_id, row)
            render_video(env_id, 15, row)

            text = f"**Action Type**<br>`{env.action}`<br>"
            text += f"**Observation Spec**<br>"
            text += get_obs_spec(env_id.split(':')[-1])
            row.column(text=text)


    doc.flush()
