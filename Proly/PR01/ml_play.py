"""
create_by         : c0266_ur001
create_at         : 2025-11-17 15:49:27
create_at_utc     : 2025-11-17T07:49:27Z
PAIA-Desktop      : 0.2.2
MLGame            : 0.7.2
game            : Proly
game_version    : 1.3.2
"""

import pickle
import os
import math
import sys
import io

_E5_8E_9F_E5_A7_8B_E5_90_91_E9_87_8F = None
_E9_95_B7_E5_BA_A6 = None
_E9_A0_86_E6_99_82_E9_87_9D_E6_97_8B_E8_BD_89 = None
_E6_AA_A2_E6_9F_A5_E9_BB_9E_E5_90_91_E9_87_8F = None
AI_E6_A8_A1_E5_9E_8BPR01 = None
_E7_9B_AE_E6_A8_99_E4_BD_8D_E7_BD_AE = None
_E6_B3_A5_E5_B7_B4_E5_90_91_E9_87_8F = None
x = None
_E6_8E_A8_E8_AB_96_E7_B5_90_E6_9E_9C = None
y = None

class MLPlayArgsSaver:
    def __init__(self):
        self.name = None
        self.init_kwargs = None
        self.observations = None
        self.keyboard = None

mlplayArgs = MLPlayArgsSaver()

if sys.stdout == sys.__stdout__:
    sys.stdout = io.TextIOWrapper(open(sys.stdout.fileno(), 'wb', 0), encoding='utf-8', write_through=True)

# 描述此函式...
def _E6_9C_80_E8_BF_91_E7_9A_84_E6_B3_A5_E5_B7_B4_E8_B7_9D_E9_9B_A2():
    global _E5_8E_9F_E5_A7_8B_E5_90_91_E9_87_8F, _E9_95_B7_E5_BA_A6, _E9_A0_86_E6_99_82_E9_87_9D_E6_97_8B_E8_BD_89, _E6_AA_A2_E6_9F_A5_E9_BB_9E_E5_90_91_E9_87_8F, AI_E6_A8_A1_E5_9E_8BPR01, _E7_9B_AE_E6_A8_99_E4_BD_8D_E7_BD_AE, _E6_B3_A5_E5_B7_B4_E5_90_91_E9_87_8F, x, _E6_8E_A8_E8_AB_96_E7_B5_90_E6_9E_9C, y
    if (mlplayArgs.observations['nearby_map_objects'][0]['object_type'] if mlplayArgs.observations is not None else None) >= 1:
        return ((mlplayArgs.observations['nearby_map_objects'][0]['relative_position'][0] if mlplayArgs.observations is not None else None) ** 2 + (mlplayArgs.observations['nearby_map_objects'][0]['relative_position'][1] if mlplayArgs.observations is not None else None) ** 2) ** 0.5
    return 999

def checkIndex(index, end=False):
    real_index = index + 1 if not end else -index
    if real_index  <= 0:
        print(f"警告：清單中的項數 # 不應小於 1，目前的值是 {real_index}。")
    return index

# 描述此函式...
def _E8_BD_89_E6_8F_9B_E6_88_90_E7_89_B9_E5_AE_9A_E9_95_B7_E5_BA_A6(_E5_8E_9F_E5_A7_8B_E5_90_91_E9_87_8F, _E9_95_B7_E5_BA_A6):
    global _E9_A0_86_E6_99_82_E9_87_9D_E6_97_8B_E8_BD_89, _E6_AA_A2_E6_9F_A5_E9_BB_9E_E5_90_91_E9_87_8F, AI_E6_A8_A1_E5_9E_8BPR01, _E7_9B_AE_E6_A8_99_E4_BD_8D_E7_BD_AE, _E6_B3_A5_E5_B7_B4_E5_90_91_E9_87_8F, x, _E6_8E_A8_E8_AB_96_E7_B5_90_E6_9E_9C, y
    return [(_E5_8E_9F_E5_A7_8B_E5_90_91_E9_87_8F[0] / math.sqrt(_E5_8E_9F_E5_A7_8B_E5_90_91_E9_87_8F[0] ** 2 + _E5_8E_9F_E5_A7_8B_E5_90_91_E9_87_8F[checkIndex(1)] ** 2)) * _E9_95_B7_E5_BA_A6, (_E5_8E_9F_E5_A7_8B_E5_90_91_E9_87_8F[checkIndex(1)] / math.sqrt(_E5_8E_9F_E5_A7_8B_E5_90_91_E9_87_8F[0] ** 2 + _E5_8E_9F_E5_A7_8B_E5_90_91_E9_87_8F[checkIndex(1)] ** 2)) * _E9_95_B7_E5_BA_A6]

# 描述此函式...
def _E6_9C_80_E8_BF_91_E7_9A_84_E6_B3_A5_E5_B7_B4_E5_90_91_E9_87_8F():
    global _E5_8E_9F_E5_A7_8B_E5_90_91_E9_87_8F, _E9_95_B7_E5_BA_A6, _E9_A0_86_E6_99_82_E9_87_9D_E6_97_8B_E8_BD_89, _E6_AA_A2_E6_9F_A5_E9_BB_9E_E5_90_91_E9_87_8F, AI_E6_A8_A1_E5_9E_8BPR01, _E7_9B_AE_E6_A8_99_E4_BD_8D_E7_BD_AE, _E6_B3_A5_E5_B7_B4_E5_90_91_E9_87_8F, x, _E6_8E_A8_E8_AB_96_E7_B5_90_E6_9E_9C, y
    return [(mlplayArgs.observations['nearby_map_objects'][0]['relative_position'][0] if mlplayArgs.observations is not None else None), (mlplayArgs.observations['nearby_map_objects'][0]['relative_position'][1] if mlplayArgs.observations is not None else None)]

# 描述此函式...
def _E6_97_8B_E8_BD_89_E5_90_91_E9_87_8F(_E5_8E_9F_E5_A7_8B_E5_90_91_E9_87_8F, _E9_A0_86_E6_99_82_E9_87_9D_E6_97_8B_E8_BD_89):
    global _E9_95_B7_E5_BA_A6, _E6_AA_A2_E6_9F_A5_E9_BB_9E_E5_90_91_E9_87_8F, AI_E6_A8_A1_E5_9E_8BPR01, _E7_9B_AE_E6_A8_99_E4_BD_8D_E7_BD_AE, _E6_B3_A5_E5_B7_B4_E5_90_91_E9_87_8F, x, _E6_8E_A8_E8_AB_96_E7_B5_90_E6_9E_9C, y
    return [_E5_8E_9F_E5_A7_8B_E5_90_91_E9_87_8F[0] * math.sin(_E9_A0_86_E6_99_82_E9_87_9D_E6_97_8B_E8_BD_89 / 180.0 * math.pi) + _E5_8E_9F_E5_A7_8B_E5_90_91_E9_87_8F[checkIndex(1)] * math.cos(_E9_A0_86_E6_99_82_E9_87_9D_E6_97_8B_E8_BD_89 / 180.0 * math.pi), -(_E5_8E_9F_E5_A7_8B_E5_90_91_E9_87_8F[0] * math.cos(_E9_A0_86_E6_99_82_E9_87_9D_E6_97_8B_E8_BD_89 / 180.0 * math.pi) + _E5_8E_9F_E5_A7_8B_E5_90_91_E9_87_8F[checkIndex(1)] * math.sin(_E9_A0_86_E6_99_82_E9_87_9D_E6_97_8B_E8_BD_89 / 180.0 * math.pi))]


class MLPlay:
    def __init__(self, observation_structure, action_space_info, name, *args, **kwargs):
        global _E5_8E_9F_E5_A7_8B_E5_90_91_E9_87_8F, _E9_95_B7_E5_BA_A6, _E9_A0_86_E6_99_82_E9_87_9D_E6_97_8B_E8_BD_89, _E6_AA_A2_E6_9F_A5_E9_BB_9E_E5_90_91_E9_87_8F, AI_E6_A8_A1_E5_9E_8BPR01, _E7_9B_AE_E6_A8_99_E4_BD_8D_E7_BD_AE, _E6_B3_A5_E5_B7_B4_E5_90_91_E9_87_8F, x, _E6_8E_A8_E8_AB_96_E7_B5_90_E6_9E_9C, y
        mlplayArgs.name = name
        mlplayArgs.init_kwargs = kwargs
        with open(os.path.join(os.path.dirname(__file__), './AI模型PR01' + '.pickle'), 'rb') as f:
            AI_E6_A8_A1_E5_9E_8BPR01 = pickle.load(f)
        _E7_9B_AE_E6_A8_99_E4_BD_8D_E7_BD_AE = []
    def update(self, observations, done, info, keyboard=set(), *args, **kwargs):
        global _E5_8E_9F_E5_A7_8B_E5_90_91_E9_87_8F, _E9_95_B7_E5_BA_A6, _E9_A0_86_E6_99_82_E9_87_9D_E6_97_8B_E8_BD_89, _E6_AA_A2_E6_9F_A5_E9_BB_9E_E5_90_91_E9_87_8F, AI_E6_A8_A1_E5_9E_8BPR01, _E7_9B_AE_E6_A8_99_E4_BD_8D_E7_BD_AE, _E6_B3_A5_E5_B7_B4_E5_90_91_E9_87_8F, x, _E6_8E_A8_E8_AB_96_E7_B5_90_E6_9E_9C, y
        mlplayArgs.observations = observations
        mlplayArgs.keyboard = keyboard
        _E6_AA_A2_E6_9F_A5_E9_BB_9E_E5_90_91_E9_87_8F = [(mlplayArgs.observations['target_position'][0] if mlplayArgs.observations is not None else None), (mlplayArgs.observations['target_position'][1] if mlplayArgs.observations is not None else None)]
        _E6_B3_A5_E5_B7_B4_E5_90_91_E9_87_8F = _E6_9C_80_E8_BF_91_E7_9A_84_E6_B3_A5_E5_B7_B4_E5_90_91_E9_87_8F()
        if _E7_9B_AE_E6_A8_99_E4_BD_8D_E7_BD_AE == []:
            _E6_B3_A5_E5_B7_B4_E5_90_91_E9_87_8F = _E6_9C_80_E8_BF_91_E7_9A_84_E6_B3_A5_E5_B7_B4_E5_90_91_E9_87_8F()
            if (math.degrees(math.acos(max(-1, min(1, ((mlplayArgs.observations['target_position'][0] if mlplayArgs.observations is not None else None) * _E6_B3_A5_E5_B7_B4_E5_90_91_E9_87_8F[0] + (mlplayArgs.observations['target_position'][1] if mlplayArgs.observations is not None else None) * _E6_B3_A5_E5_B7_B4_E5_90_91_E9_87_8F[-1]) / max(1e-10, (((mlplayArgs.observations['target_position'][0] if mlplayArgs.observations is not None else None) ** 2 + (mlplayArgs.observations['target_position'][1] if mlplayArgs.observations is not None else None) ** 2) ** 0.5) * ((_E6_B3_A5_E5_B7_B4_E5_90_91_E9_87_8F[0] ** 2 + _E6_B3_A5_E5_B7_B4_E5_90_91_E9_87_8F[-1] ** 2) ** 0.5))))))) < 18 and _E6_9C_80_E8_BF_91_E7_9A_84_E6_B3_A5_E5_B7_B4_E8_B7_9D_E9_9B_A2() < (_E6_B3_A5_E5_B7_B4_E5_90_91_E9_87_8F[0] ** 2 + _E6_B3_A5_E5_B7_B4_E5_90_91_E9_87_8F[-1] ** 2) ** 0.5:
                print('最近的' + str(_E6_9C_80_E8_BF_91_E7_9A_84_E6_B3_A5_E5_B7_B4_E5_90_91_E9_87_8F()))
                _E7_9B_AE_E6_A8_99_E4_BD_8D_E7_BD_AE = [sum([(mlplayArgs.observations['agent_position'][0] if mlplayArgs.observations is not None else None), _E8_BD_89_E6_8F_9B_E6_88_90_E7_89_B9_E5_AE_9A_E9_95_B7_E5_BA_A6(_E6_97_8B_E8_BD_89_E5_90_91_E9_87_8F(_E6_9C_80_E8_BF_91_E7_9A_84_E6_B3_A5_E5_B7_B4_E5_90_91_E9_87_8F(), 90), 1.5)[0], _E6_B3_A5_E5_B7_B4_E5_90_91_E9_87_8F[0]]), sum([(mlplayArgs.observations['agent_position'][2] if mlplayArgs.observations is not None else None), _E8_BD_89_E6_8F_9B_E6_88_90_E7_89_B9_E5_AE_9A_E9_95_B7_E5_BA_A6(_E6_97_8B_E8_BD_89_E5_90_91_E9_87_8F(_E6_9C_80_E8_BF_91_E7_9A_84_E6_B3_A5_E5_B7_B4_E5_90_91_E9_87_8F(), 90), 1.5)[-1], _E6_B3_A5_E5_B7_B4_E5_90_91_E9_87_8F[-1]])]
            else:
                x = _E6_AA_A2_E6_9F_A5_E9_BB_9E_E5_90_91_E9_87_8F[0]
                y = _E6_AA_A2_E6_9F_A5_E9_BB_9E_E5_90_91_E9_87_8F[-1]
        elif (((mlplayArgs.observations['agent_position'][0] if mlplayArgs.observations is not None else None) - _E7_9B_AE_E6_A8_99_E4_BD_8D_E7_BD_AE[0]) ** 2 + ((mlplayArgs.observations['agent_position'][2] if mlplayArgs.observations is not None else None) - _E7_9B_AE_E6_A8_99_E4_BD_8D_E7_BD_AE[-1]) ** 2) ** 0.5 < 0.3:
            _E7_9B_AE_E6_A8_99_E4_BD_8D_E7_BD_AE = []
            x = _E6_AA_A2_E6_9F_A5_E9_BB_9E_E5_90_91_E9_87_8F[0]
            y = _E6_AA_A2_E6_9F_A5_E9_BB_9E_E5_90_91_E9_87_8F[-1]
        else:
            x = _E7_9B_AE_E6_A8_99_E4_BD_8D_E7_BD_AE[-1] - (mlplayArgs.observations['agent_position'][2] if mlplayArgs.observations is not None else None)
            y = _E7_9B_AE_E6_A8_99_E4_BD_8D_E7_BD_AE[0] - (mlplayArgs.observations['agent_position'][0] if mlplayArgs.observations is not None else None)
        _E6_8E_A8_E8_AB_96_E7_B5_90_E6_9E_9C = AI_E6_A8_A1_E5_9E_8BPR01.predict([[x, y]]).tolist()[0]
        print(_E6_8E_A8_E8_AB_96_E7_B5_90_E6_9E_9C)
        return ([_E6_8E_A8_E8_AB_96_E7_B5_90_E6_9E_9C[0], _E6_8E_A8_E8_AB_96_E7_B5_90_E6_9E_9C[-1]], [0, 0])
    def reset(self):
        global _E5_8E_9F_E5_A7_8B_E5_90_91_E9_87_8F, _E9_95_B7_E5_BA_A6, _E9_A0_86_E6_99_82_E9_87_9D_E6_97_8B_E8_BD_89, _E6_AA_A2_E6_9F_A5_E9_BB_9E_E5_90_91_E9_87_8F, AI_E6_A8_A1_E5_9E_8BPR01, _E7_9B_AE_E6_A8_99_E4_BD_8D_E7_BD_AE, _E6_B3_A5_E5_B7_B4_E5_90_91_E9_87_8F, x, _E6_8E_A8_E8_AB_96_E7_B5_90_E6_9E_9C, y
        pass
