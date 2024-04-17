"""
created_at_utc  : 2024-03-14T03:29:37Z
created_at_w3c  : 2024-03-14T11:29:37+08:00
PAIA-Desktop    : 2.6.0
MLGame          : 10.3.2
game            : swimming-squid
game_version    :   1.0.6
"""

from mushroom_rl.algorithms.value.td import QLearning
from mushroom_rl.core.environment import MDPInfo
from mushroom_rl.utils.spaces import Discrete
from mushroom_rl.policy.td_policy import EpsGreedy
from mushroom_rl.utils.parameters import Parameter
import os
import pickle
import numpy as np
import sys
import io
from mushroom_rl.utils.dataset import arrays_as_dataset
import math

point_list = None
ball_x = None
ball_y = None
model = None
state = None
nearest_positive_point = None
prev_state = None
reward = None
nearest_positive_distance = None
prev_action = None
nearest_negative_point = None
prev_score = None
action = None
i = None
nearest_negative_distance = None
states = None
model_name = None
point = None
actions = None
x = None
positive_state = None
next_states = None
y = None
negative_state = None
distance = None
right_back = None
right_front = None

if sys.stdout == sys.__stdout__:
    sys.stdout = io.TextIOWrapper(open(sys.stdout.fileno(), 'wb', 0), encoding='utf-8', write_through=True)

def upRange(start, stop, step):
    while start <= stop:
        yield start
        start += abs(step)

def downRange(start, stop, step):
    while start >= stop:
        yield start
        start -= abs(step)

# 描述此函式...
def get_state(point_list, ball_x, ball_y):
    global model, state, nearest_positive_point, prev_state, reward, nearest_positive_distance, prev_action, nearest_negative_point, prev_score, action, i, nearest_negative_distance, states, model_name, point, actions, x, positive_state, next_states, y, negative_state, distance, right_back, right_front
    nearest_positive_point = None
    nearest_positive_distance = -1
    nearest_negative_point = None
    nearest_negative_distance = -1
    for point in point_list:
        x = point['x']
        y = point['y']
        distance = math.fabs(ball_x - x) + math.fabs(ball_y - y)
        if point['score'] > 0:
            if nearest_positive_distance == -1 or nearest_positive_distance > distance:
                nearest_positive_point = point
                nearest_positive_distance = distance
        elif point['score'] < 0:
            if nearest_negative_distance == -1 or nearest_negative_distance > distance:
                nearest_negative_point = point
                nearest_negative_distance = distance
    positive_state = 0
    negative_state = 0
    if nearest_positive_distance != -1:
        x = nearest_positive_point['x']
        y = nearest_positive_point['y']
        right_back = x + y > ball_x + ball_y
        right_front = x - y > ball_x - ball_y
        if right_front and not right_back:
            positive_state = 1
        elif not right_front and not right_back:
            positive_state = 2
        elif not right_front and right_back:
            positive_state = 3
        elif right_front and right_back:
            positive_state = 4
    if nearest_negative_distance != -1:
        x = nearest_negative_point['x']
        y = nearest_negative_point['y']
        right_back = x + y > ball_x + ball_y
        right_front = x - y > ball_x - ball_y
        if right_front and not right_back:
            negative_state = 1
        elif not right_front and not right_back:
            negative_state = 2
        elif not right_front and right_back:
            negative_state = 3
        elif right_front and right_back:
            negative_state = 4
    state = positive_state * 5 + negative_state
    return state


class MLPlay:
    def __init__(self, ai_name, *args, **kwargs):
        global point_list, ball_x, ball_y, model, state, nearest_positive_point, prev_state, reward, nearest_positive_distance, prev_action, nearest_negative_point, prev_score, action, i, nearest_negative_distance, states, model_name, point, actions, x, positive_state, next_states, y, negative_state, distance, right_back, right_front
        model = QLearning(
            MDPInfo(Discrete(25), Discrete(5), 0.9, 1),
            EpsGreedy(0.5),
            Parameter(0.01),
        )
        prev_state = 0
        prev_action = 0
        prev_score = 0
        prev_state = 0
        states = []
        actions = []
        next_states = []
        model_name = 'model'
        if os.path.exists(os.path.join(os.path.dirname(__file__), str(model_name) + '.pickle')):
            with open(os.path.join(os.path.dirname(__file__), model_name + '.pickle'), 'rb') as f:
                model = pickle.load(f)
    def update(self, scene_info, keyboard=[], *args, **kwargs):
        global point_list, ball_x, ball_y, model, state, nearest_positive_point, prev_state, reward, nearest_positive_distance, prev_action, nearest_negative_point, prev_score, action, i, nearest_negative_distance, states, model_name, point, actions, x, positive_state, next_states, y, negative_state, distance, right_back, right_front
        state = get_state(scene_info['foods'], scene_info['frame'], scene_info['frame'])
        reward = scene_info['score'] - prev_score
        if reward != 0:
            states.append(prev_state)
            actions.append(prev_action)
            next_states.append(state)
        action = model.draw_action(np.array(state, ndmin=2))
        prev_state = state
        prev_action = action
        prev_score = scene_info['score']
        if action == 1:
            return ['UP']
        elif action == 2:
            return ['LEFT']
        elif action == 3:
            return ['DOWN']
        elif action == 4:
            return ['RIGHT']
        return ['NONE']
    def reset(self):
        global point_list, ball_x, ball_y, model, state, nearest_positive_point, prev_state, reward, nearest_positive_distance, prev_action, nearest_negative_point, prev_score, action, i, nearest_negative_distance, states, model_name, point, actions, x, positive_state, next_states, y, negative_state, distance, right_back, right_front
        print('----------')
        if len(states) > 0:
            reward = prev_score / len(states)
            i_end = len(states)
            for i in (1 <= i_end) and upRange(1, i_end, 1) or downRange(1, i_end, 1):
                model.fit(arrays_as_dataset(np.array([[states[int(i - 1)]]]), np.array([[actions[int(i - 1)]]]), np.array([[reward]]), np.array([[actions[int(i - 1)]]]), np.array([[False]]), np.array([[False]])))
                state = states[int(i - 1)]
                print(''.join([str(x2) for x2 in ['state: ', math.floor(state / 5), ', ', state % 5, ' | action: ', actions[int(i - 1)][0], ' | reward: ', reward]]))
        print('----------')
        with open(os.path.join(os.path.dirname(__file__), model_name + '.pickle'), 'wb') as f:
            pickle.dump(model, f)
        prev_state = 0
        prev_action = 0
        prev_score = 0
        states = []
        actions = []
        next_states = []
