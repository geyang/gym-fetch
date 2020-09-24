import gym
import numpy as np
from tqdm import trange

scale = 3
src_prefix = "figures"


def get_obs_spec(env_id):
    env = gym.make("fetch:" + env_id)
    buffer = []
    for k, v in env.observation_space.spaces.items():
        if hasattr(v, "spaces"):
            buffer += [f"{k}:"]
            for k, v in v.spaces.items():
                buffer += [f"&nbsp;&nbsp;&nbsp;&nbsp;{k}: {v.shape}"]
        else:
            buffer += [f"{k}: {v.shape}"]
    return "<br>".join(buffer)


def render_initial(env_id, doc):
    env = gym.make(env_id)

    env_id = env_id.split(':')[-1]

    img = env.render('rgb_array', width=150 * scale, height=120 * scale)
    doc.figure(img, src=f"{src_prefix}/{env_id}_init.png?ts={doc.now('%f')}", title=env_id)

    frames = []
    for i in range(10):
        env.reset()
        frames.append(env.render('rgb_array', width=100 * scale, height=120 * scale))
    doc.figure(np.array(frames).min(axis=0), src=f"{src_prefix}/{env_id}_reset.png?ts={doc.now('%f')}",
               title="distribution")
    return env


def render_video(env_id, n, doc):
    env = gym.make(env_id)
    env_id = env_id.split(':')[-1]
    frames = []
    for ep in trange(n):
        env.reset()
        for i in range(10):
            act = env.action_space.sample()
            ts = env.step(act)
            frames.append(env.render('rgb_array', width=100 * scale, height=120 * scale))

    doc.video(np.array(frames), src=f"{src_prefix}/{env_id}.gif?ts={doc.now('%f')}")
