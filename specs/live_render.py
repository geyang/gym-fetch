import time
import gym


def live_render(env_id):
    env = gym.make(env_id)
    env.reset()
    while True:
        action = env.action_space.sample()
        timestep = env.step(action)
        env.render()
        print(timestep)
        time.sleep(0.1)


if __name__ == '__main__':
    # live_render('fetch:Bin-picking-v0')
    # live_render('fetch:Box-open-v0')
    live_render('fetch:Drawer-open-v0')
