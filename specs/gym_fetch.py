import gym
import numpy as np
from cmx import doc
from cmx.backends.components import Image

scale = 3


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
    frames = []
    for ep in range(n):
        env.reset()
        for i in range(10):
            act = env.action_space.sample()
            ts = env.step(act)
            frames.append(env.render('rgb_array', width=100 * scale, height=120 * scale))

    doc.video(np.array(frames), f"{__file__[:-3]}/videos/{env_id}.gif", caption="After Reset")


if __name__ == '__main__':
    # with doc, doc.row() as row:
    #     render_initial('FetchPickAndPlace-v1', row)
    #
    doc @ f"""
    # Original Gym Fetch Tasks

    This set reproduces the original gym Fetch robot tasks.

    Name             | Observation Spec                     | Info
    ---------------- | ----------------                     | -------
    **Reach-v0**  | {get_obs_spec('fetch:Reach-v0')}  | {{success, dist}}
    **Push-v0** | {get_obs_spec('fetch:Push-v0')} | {{success, dist}}
    **PickPlace-v0** | {get_obs_spec('fetch:PickPlace-v0')} | {{success, dist}}
    **Slide-v0** | {get_obs_spec('fetch:Slide-v0')} | {{success, dist}}

    """
    with doc, doc.row() as row:
        render_initial('fetch:Reach-v0', row)
        render_video('fetch:Reach-v0', 5, row)

    with doc, doc.row() as row:
        render_initial('fetch:Push-v0', row)
        render_video('fetch:Push-v0', 5, row)

    with doc, doc.row() as row:
        render_initial('fetch:PickPlace-v0', row)
        render_video('fetch:PickPlace-v0', 5, row)

    with doc, doc.row() as row:
        render_initial('fetch:Slide-v0', row)
        render_video('fetch:Slide-v0', 5, row)

    doc.flush()
