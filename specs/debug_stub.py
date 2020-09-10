import gym
import numpy as np
from cmx import doc
from cmx.backends.components import Image

doc @ """
# Fetch Environment
"""

scale = 7


def get_obs_spec(env_id):
    env = gym.make(env_id)
    buffer = []
    for k, v in env.observation_space.spaces.items():
        buffer += [f"{k}: {v.shape}"]
    return "<br>".join(buffer)


def render_initial(env_id, doc):
    env = gym.make(env_id)
    img = env.render('rgb_array', width=100 * scale, height=120 * scale)
    doc.image(img, caption="Initial")

    frames = []
    for i in range(10):
        env.reset()
        frames.append(env.render('rgb_array', width=100 * scale, height=120 * scale))

    doc.image(np.array(frames).min(axis=0), caption="After Reset")


def render_video(env_id, n, doc):
    env = gym.make(env_id)
    img = env.render('rgb_array', width=100 * scale, height=120 * scale)
    doc.image(img, caption="Initial")

    frames = []
    for ep in range(n):
        env.reset()
        for i in range(10):
            act = env.action_space.sample()
            ts = env.step(act)
            frames.append(env.render('rgb_array', width=100 * scale, height=120 * scale))

    doc.video(np.array(frames), f"videos/{env_id}.gif", caption="After Reset")


if __name__ == '__main__':
    with doc, doc.row() as row:
        render_initial('FetchPickAndPlace-v1', row)

    doc @ f"""
    Name             | Observation Spec                     | Info
    ---------------- | ----------------                     | -------
    **Bin-debug-v0** | {get_obs_spec('fetch:Bin-debug-v0')} | {{is_success, dist}}
    **Bin-v0**       | {get_obs_spec('fetch:Bin-v0')}       | {{is_success, dist}}
    **Bin-pick-v0**  | {get_obs_spec('fetch:Bin-pick-v0')}  | {{is_success, dist}}
    **Bin-place-v0** | {get_obs_spec('fetch:Bin-place-v0')} | {{is_success, dist}}
    """
    with doc, doc.row() as row:
        render_initial('fetch:Bin-v0', row)

    with doc, doc.row() as row:
        render_initial('fetch:Bin-pick-v0', row)

    with doc, doc.row() as row:
        render_initial('fetch:Bin-place-v0', row)

    doc @ f"""
    > **Potential Caveat:**
    > the bin might get pushed around, need to synchronize
    > the target against new bin location. Do so in _step_callback
    """
    with doc, doc.row() as row:
        render_video('fetch:Bin-debug-v0', 5, row)

    with doc, doc.row() as row:
        render_video('fetch:Bin-v0', 5, row)

    with doc, doc.row() as row:
        render_video('fetch:Bin-pick-v0', 5, row)

    with doc, doc.row() as row:
        render_video('fetch:Bin-place-v0', 5, row)
    doc.flush()
