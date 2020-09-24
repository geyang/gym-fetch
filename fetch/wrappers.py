from copy import deepcopy

import numpy as np
import gym.spaces as spaces
from gym import ObservationWrapper, Wrapper
from gym.spaces import Dict, Box


class FlatEnv(ObservationWrapper):
    r"""Observation wrapper that flattens the observation."""

    def __init__(self, env, keys=None):
        super().__init__(env)

        # todo: allow selecting subsets using keys
        dim = spaces.flatdim(env.observation_space)
        self.observation_space = spaces.Box(low=-float('inf'), high=float('inf'), shape=(dim,), dtype=np.float32)

    def observation(self, observation):
        return spaces.flatten(self.env.observation_space, observation)


def recover_goal(goal_vec):
    if len(goal_vec.shape) == 1:
        return {
            "object0": goal_vec[:3],
            "lid": goal_vec[3:6],
        }
    elif len(goal_vec.shape) == 2:
        return {
            "object0": goal_vec[:, :3],
            "lid": goal_vec[:, 3:6],
        }


class HERVecGoal(Wrapper):
    """Flattens the dictionary goals into a flat, goal vector.

    """

    def __init__(self, env, goal_keys=("object0", "lid")):
        super().__init__(env)

        obs_space = env.observation_space
        goal_space = obs_space.spaces['desired_goal']

        self.goal_keys = goal_keys or env.goal_key
        self.goal_dims = [goal_space[k].shape for k in self.goal_keys]
        low = np.concatenate([goal_space[k].low for k in self.goal_keys])
        high = np.concatenate([goal_space[k].high for k in self.goal_keys])

        self.observation_space = deepcopy(obs_space)
        self.observation_space.spaces['desired_goal'] = Box(low=low, high=high)
        self.observation_space.spaces['achieved_goal'] = Box(low=low, high=high)

    def compute_reward(self, achieved_goal, desired_goal, info):
        achieved_goal = recover_goal(achieved_goal)
        desired_goal = recover_goal(desired_goal)
        return self.env.compute_reward(achieved_goal, desired_goal, info)

    def step(self, action):
        obs, reward, done, info = self.env.step(action)
        obs['achieved_goal'] = np.concatenate([obs['achieved_goal'][k] for k in self.goal_keys])
        obs['desired_goal'] = np.concatenate([obs['desired_goal'][k] for k in self.goal_keys])
        return obs, reward, done, info

    def reset(self):
        obs = self.env.reset()
        obs['achieved_goal'] = np.concatenate([obs['achieved_goal'][k] for k in self.goal_keys])
        obs['desired_goal'] = np.concatenate([obs['desired_goal'][k] for k in self.goal_keys])
        return obs
