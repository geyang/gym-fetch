from cmx import doc
import gym

from specs.__init__ import get_obs_spec, render_initial, render_video

if __name__ == '__main__':
    doc @ f"""
    write_protected: true
    ---

    # Stack-2 Environment

    """
    with doc, doc.table().figure_row() as row:
        initial_types = [
            'table-top',
            'in-hand',
            'obj1-in-hand',
            "train"
        ]

        for init_type in initial_types:
            env = gym.make("fetch:StackTwo-v0", action=init_type)
            render_video(f"StackTwo-{initial_types}", 15, row, env=env, title=init_type,
                         filename=f"Stack2-{init_type}.gif")

    doc @ """
    ## Box Diagnostic Tasks
    Name                   | Observation Spec                     | Goal Init/Comment  | 
    -----------------      | ----------------                     | -------            | ------
    **StackTwo-train-v0**  | {get_obs_spec('StackTwo-train-v0')}  | Four parts<br>- table-top<br>- in-hand<br>- obj0-at-target<br>- obj1-in-hand  | ![](figures/StackTwo-train-v0.gif)
    **StackTwo-v0**        | {get_obs_spec('StackTwo-v0')}        |                    | ![](figures/StackTwo-v0.gif)

    ## Details of Each Task
    """
    with doc:
        box_envs = [
            "fetch:StackTwo-train-v0",
            "fetch:StackTwo-v0",
        ]
    table = doc.table()
    for env_id in box_envs:
        with table.figure_row() as row:
            render_initial(env_id, row)
            render_video(env_id, 15, row)

    doc.flush()
