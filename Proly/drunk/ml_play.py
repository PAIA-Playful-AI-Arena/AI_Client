"""
create_by       : test_process
create_at       : 2026-05-27 14:31:53
create_at_utc   : 2026-05-27T06:31:53Z
PAIA-Desktop    : 3.3.2
MLGame          : 0.8.0
game            : Proly
game_version    : 1.4.1
"""

import os
import time
from stable_baselines3 import PPO
import numpy as np
import gymnasium as gym
from gymnasium import spaces

class MLPlayArgsSaver:
    def __init__(self):
        self.name = None
        self.init_kwargs = None
        self.observations = None
        self.keyboard = None

mlplayArgs = MLPlayArgsSaver()

class RlplayRewardCalculator:
    def __init__(self):
        self.prev_observation = None
        self.observation = None

    def update(self, observation):
        self.prev_observation = self.observation
        self.observation = observation

    def reset(self):
        self.prev_observation = None
        self.observation = None

    def calculate_checkpoint_reward(self, weight):
        if self.prev_observation is None or self.observation is None:
            return 0.0
        if self.prev_observation["last_checkpoint_index"] < self.observation["last_checkpoint_index"]:
            return weight * (self.observation["last_checkpoint_index"] - self.prev_observation["last_checkpoint_index"])
        return 0.0

    def calculate_distance_reward(self, close_weight, leave_weight):
        if self.prev_observation is None or self.observation is None:
            return 0.0
        if self.prev_observation["last_checkpoint_index"] != self.observation["last_checkpoint_index"]:
            return 0.0
        prev_distance = np.linalg.norm(np.array([
            self.prev_observation["target_position"][0],
            self.prev_observation["target_position"][1]
        ]))
        current_distance = np.linalg.norm(np.array([
            self.observation["target_position"][0],
            self.observation["target_position"][1]
        ]))
        if current_distance <= prev_distance:
            return close_weight * (prev_distance - current_distance)
        else:
            return leave_weight * (current_distance - prev_distance)

    def calculate_health_reward(self, death_weight, increase_weight, decrease_weight):
        if self.prev_observation is None or self.observation is None:
            return 0.0
        if self.prev_observation["agent_health"] <= 0.0:
            return 0.0
        if self.observation["agent_health"] <= 0.0:
            return death_weight
        if self.observation["agent_health"] >= self.prev_observation["agent_health"]:
            return increase_weight * (self.observation["agent_health"] - self.prev_observation["agent_health"])
        else:
            return decrease_weight * (self.prev_observation["agent_health"] - self.observation["agent_health"])

    def calculate_mud_reward(self, threshold, leave_weight, close_weight):
        if self.prev_observation is None or self.observation is None:
            return 0.0
        prev_nearby_obects = self.prev_observation["nearby_map_objects"]
        nearby_obects = self.observation["nearby_map_objects"]
        prev_muds = [obj for obj in prev_nearby_obects if obj["object_type"] == 1]
        muds = [obj for obj in nearby_obects if obj["object_type"] == 1]
        if not prev_muds or not muds:
            return 0.0
        prev_nearest_mud = min(prev_muds, key=lambda x: np.linalg.norm(np.array(x["relative_position"])))
        nearest_mud = min(muds, key=lambda x: np.linalg.norm(np.array(x["relative_position"])))
        prev_distance = np.linalg.norm(np.array(prev_nearest_mud["relative_position"]))
        distance = np.linalg.norm(np.array(nearest_mud["relative_position"]))
        if prev_distance > threshold or distance > threshold:
            return 0.0
        if distance >= prev_distance:
            return leave_weight * (distance - prev_distance)
        else:
            return close_weight * (prev_distance - distance)

rlplayRewardCalculator = RlplayRewardCalculator()

class ObservationProcessor:
    def __init__(self, observation_structure):
        self.observation_structure = observation_structure
        self.observation_size = self._calculate_observation_size(observation_structure)
        print(f"Observation size calculated: {self.observation_size}")

    def get_size(self):
        return self.observation_size

    def _calculate_observation_size(self, observation_structure):
        total_size = 0

        for item in observation_structure:
            item_type = item.get("type", "")
            item_key = item.get("key", "")

            if item_key == "flattened":
                vector_size = item.get("vector_size", 0)
                return vector_size

            if item_type == "Vector3":
                total_size += 3
            elif item_type == "Vector2":
                total_size += 2
            elif item_type == "float" or item_type == "int" or item_type == "bool":
                total_size += 1
            elif item_type == "Grid":
                grid_size = item.get("grid_size", 0)
                sub_items = item.get("items", [])
                sub_item_size = self._calculate_observation_size(sub_items)
                total_size += sub_item_size * grid_size * grid_size
            elif item_type == "List":
                sub_items = item.get("items", [])
                sub_item_size = self._calculate_observation_size(sub_items)
                sub_item_count = item.get("item_count", 0)

                if sub_item_count > 0:
                    total_size += sub_item_size * sub_item_count
                else:
                    total_size += sub_item_size

        return total_size

class ActionProcessor:
    def __init__(self, action_space_info):
        self.action_space_info = action_space_info

        if action_space_info.is_continuous():
            self.action_type = "continuous"
            self.action_size = action_space_info.continuous_size
        elif action_space_info.is_discrete():
            self.action_type = "discrete"
            self.action_size = sum(action_space_info.discrete_branches)
            self.discrete_branches = action_space_info.discrete_branches
        else:
            self.action_type = "hybrid"
            self.continuous_size = action_space_info.continuous_size
            self.discrete_branches = action_space_info.discrete_branches
            self.discrete_size = sum(action_space_info.discrete_branches)
            self.action_size = self.continuous_size + self.discrete_size

        print(f"Action space detected: {self.action_type}")
        if self.action_type == "continuous":
            print(f"  Continuous size: {self.action_size}")
        elif self.action_type == "discrete":
            print(f"  Discrete branches: {self.discrete_branches}")
        else:
            print(f"  Continuous size: {self.continuous_size}")
            print(f"  Discrete branches: {self.discrete_branches}")
            print(f"  Unified Box space size: {self.action_size}")

    def create_action(self, network_output):
        if self.action_type == "continuous":
            return network_output
        elif self.action_type == "discrete":
            return self._process_discrete_action(network_output)
        else:
            return self._process_hybrid_action(network_output)

    def action_to_network_output(self, action):
        if self.action_type == "continuous":
            return action
        elif self.action_type == "discrete":
            return self._process_discrete_to_network_output(action)
        else:
            return self._process_hybrid_to_network_output(action)

    def get_size(self):
        return self.action_size

    def get_gym_action_space(self):
        if self.action_type == "continuous":
            return spaces.Box(low=-1.0, high=1.0, shape=(self.action_size,), dtype=np.float32)
        elif self.action_type == "discrete":
            if len(self.discrete_branches) == 1:
                return spaces.Discrete(self.discrete_branches[0])
            else:
                return spaces.MultiDiscrete(self.discrete_branches)
        else:
            return spaces.Box(low=-1.0, high=1.0, shape=(self.action_size,), dtype=np.float32)

    def _process_discrete_action(self, network_output):
        if isinstance(network_output, np.ndarray):
            if len(self.discrete_branches) == 1:
                return np.array([network_output], dtype=np.int32)
            else:
                return network_output.astype(np.int32)
        else:
            return np.array([network_output], dtype=np.int32)

    def _process_hybrid_action(self, network_output):
        continuous_part = network_output[:self.continuous_size]
        discrete_part = network_output[self.continuous_size:]

        continuous_action = continuous_part
        discrete_action = self._continuous_to_discrete(discrete_part)

        return (continuous_action, discrete_action)

    def _continuous_to_discrete(self, continuous_values):
        discrete_actions = []
        value_idx = 0

        for branch_size in self.discrete_branches:
                discrete_action = 0
                max_continuous_val = float("-inf")
                for i in range(branch_size):
                        if value_idx + i < len(continuous_values):
                                continuous_val = continuous_values[value_idx + i]
                                if continuous_val > max_continuous_val:
                                        discrete_action = i
                                        max_continuous_val = continuous_val
                discrete_actions.append(discrete_action)
                value_idx += branch_size

        return np.array(discrete_actions, dtype=np.int32)

    def _process_discrete_to_network_output(self, action):
        if isinstance(action, np.ndarray) and len(self.discrete_branches) == 1 and len(action) == 1:
            return action[0]
        return action

    def _process_hybrid_to_network_output(self, action):
        continuous_action, discrete_action = action
        discrete_continuous = self._discrete_to_continuous(discrete_action)
        return np.concatenate([continuous_action, discrete_continuous])

    def _discrete_to_continuous(self, discrete_values):
        continuous_actions = []
        value_idx = 0

        for branch_size in self.discrete_branches:
            if value_idx < len(discrete_values):
                discrete_val = discrete_values[value_idx]
                for i in range(branch_size):
                    if i == discrete_val:
                        continuous_actions.append(1.0)
                    else:
                        continuous_actions.append(-1.0)
            value_idx += 1

        return np.array(continuous_actions, dtype=np.float32)

class EnvWrapper(gym.Env):
    def __init__(self, observation_structure, action_space_info):
        super().__init__()
        self.observation_processor = ObservationProcessor(observation_structure)
        self.action_processor = ActionProcessor(action_space_info)

        obs_size = self.observation_processor.get_size()
        self.observation_space = spaces.Box(
            low=-np.inf, high=np.inf, shape=(obs_size,), dtype=np.float32
        )
        self.action_space = self.action_processor.get_gym_action_space()
        self.step_count = 0

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.step_count = 0
        dummy_obs = np.zeros(self.observation_space.shape, dtype=np.float32)
        return dummy_obs, {}

    def step(self, action):
        self.step_count += 1
        dummy_obs = np.zeros(self.observation_space.shape, dtype=np.float32)
        reward = 0.0
        terminated = False
        truncated = False
        info = {}
        return dummy_obs, reward, terminated, truncated, info

class MLPlay:
    def __init__(self, observation_structure, action_space_info, name, *args, **kwargs):
        mlplayArgs.name = name
        mlplayArgs.init_kwargs = kwargs

        rlplayRewardCalculator.reset()
        self.RLPlay = RLPlay()

        self.env_wrapper = EnvWrapper(observation_structure, action_space_info)
        self.config = {
            "tensorboard_log": os.path.join(os.path.dirname(__file__), "tensorboard"),
        }
        self.prev_observation = None
        self.episode_rewards = []
        self.total_steps = 0
        self.episode_count = 1
        self.start_time = time.strftime("%Y%m%d_%H%M%S")
        self.model_path = os.path.join(os.path.dirname(__file__), 'drunk-model' + ".zip")

        self._initialize_model()

        print(f"PPO initialized in testing mode")

    def reset(self):
        if self.episode_rewards:
                total_reward = sum(self.episode_rewards)
                print(f"Episode {self.episode_count}: Total Reward = {total_reward:.2f}, Steps = {len(self.episode_rewards)}")
                self.model.logger.record("test/episode_reward", total_reward)
                self.episode_rewards = []

        self.prev_observation = None
        self.episode_count += 1
        self.model._dump_logs(self.episode_count)

        rlplayRewardCalculator.reset()
        self.RLPlay.reset()

    def update(self, observations, done, info, keyboard=set(), *args, **kwargs):
        mlplayArgs.observations = observations
        mlplayArgs.keyboard = keyboard
        rlplayRewardCalculator.update(observations)
        observation = observations["flattened"]

        reward = self.RLPlay.update()
        action, _ = self.model.predict(observation, deterministic=False)

        if self.prev_observation is not None:
            self.episode_rewards.append(reward)

        self.prev_observation = observation
        self.total_steps += 1

        return self.env_wrapper.action_processor.create_action(action)

    def _initialize_model(self):
        print(f"Initializing PPO model...")
        if os.path.exists(self.model_path):
            self.model = PPO.load(self.model_path, env=self.env_wrapper, **self.config, verbose=1)
            print(f"Model loaded from {self.model_path}")
        else:
            raise FileNotFoundError(f"No pre-trained model found at {self.model_path}.")
        self.model.learn(total_timesteps=0, tb_log_name=f"PPO_{self.start_time}")


class RLPlay:
    def __init__(self):
        pass
    def update(self):
        return 0
    def reset(self):
        pass
