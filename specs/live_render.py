import time
import gym


def live_render(env_id):
    env = gym.make(env_id)
    env.reset()
    while True:
        action = env.action_space.sample()
        timestep = env.step(action)
        env.render()
        time.sleep(0.1)

if __name__ == '__main__':
    live_render('FetchReach-v1')