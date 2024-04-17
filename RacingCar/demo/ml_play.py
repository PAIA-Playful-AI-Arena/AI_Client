"""
created_at_utc  : 2023-05-23T06:24:59Z
created_at_w3c  : 2023-05-23T14:24:59+08:00
PAIA-Desktop    : 2.4.3
MLGame          : 10.2.8
game            : racing_car
game_version    : 3.4.1
"""

import pickle
import os
from numbers import Number
import math
import sys
import io

_E6_95_B8_E5_80_BC = None
_E5_88_86_E5_AD_90 = None
_E5_88_86_E6_AF_8D = None
_E9_81_8A_E6_88_B2_E7_8B_80_E6_85_8B = None
_E5_B9_80_E6_95_B8 = None
_E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F = None
_E9_81_8A_E6_88_B2_E6_AC_A1_E6_95_B8 = None
_E7_8E_A9_E5_AE_B6_E7_9A_84x_E5_BA_A7_E6_A8_99 = None
_E9_81_8E_E9_97_9C_E6_AC_A1_E6_95_B8 = None
_E7_8E_A9_E5_AE_B6_E7_9A_84y_E5_BA_A7_E6_A8_99 = None
AI_E6_A8_A1_E5_9E_8B = None
_E7_8E_A9_E5_AE_B6_E8_A1_8C_E5_8B_95 = None
_E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_85_A5 = None
_E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_87_BA = None

# 描述此函式...
def _E5_88_9D_E5_A7_8B_E5_8C_96_E9_81_8A_E6_88_B2_E6_88_90_E7_B8_BE_E8_AE_8A_E6_95_B8():
    global _E6_95_B8_E5_80_BC, _E5_88_86_E5_AD_90, _E5_88_86_E6_AF_8D, _E9_81_8A_E6_88_B2_E7_8B_80_E6_85_8B, _E5_B9_80_E6_95_B8, _E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F, _E9_81_8A_E6_88_B2_E6_AC_A1_E6_95_B8, _E7_8E_A9_E5_AE_B6_E7_9A_84x_E5_BA_A7_E6_A8_99, _E9_81_8E_E9_97_9C_E6_AC_A1_E6_95_B8, _E7_8E_A9_E5_AE_B6_E7_9A_84y_E5_BA_A7_E6_A8_99, AI_E6_A8_A1_E5_9E_8B, _E7_8E_A9_E5_AE_B6_E8_A1_8C_E5_8B_95, _E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_85_A5, _E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_87_BA
    _E9_81_8A_E6_88_B2_E7_8B_80_E6_85_8B = 0
    _E9_81_8A_E6_88_B2_E6_AC_A1_E6_95_B8 = 0
    _E9_81_8E_E9_97_9C_E6_AC_A1_E6_95_B8 = 0
    _E5_B9_80_E6_95_B8 = 0

# 描述此函式...
def _E5_8F_96_E5_88_B0_E5_B0_8F_E6_95_B8_E9_BB_9E_E4_BB_A5_E4_B8_8B4_E4_BD_8D(_E6_95_B8_E5_80_BC):
    global _E5_88_86_E5_AD_90, _E5_88_86_E6_AF_8D, _E9_81_8A_E6_88_B2_E7_8B_80_E6_85_8B, _E5_B9_80_E6_95_B8, _E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F, _E9_81_8A_E6_88_B2_E6_AC_A1_E6_95_B8, _E7_8E_A9_E5_AE_B6_E7_9A_84x_E5_BA_A7_E6_A8_99, _E9_81_8E_E9_97_9C_E6_AC_A1_E6_95_B8, _E7_8E_A9_E5_AE_B6_E7_9A_84y_E5_BA_A7_E6_A8_99, AI_E6_A8_A1_E5_9E_8B, _E7_8E_A9_E5_AE_B6_E8_A1_8C_E5_8B_95, _E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_85_A5, _E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_87_BA
    return round(_E6_95_B8_E5_80_BC * 10000) / 10000

# 取到小數點以下4位
def _E6_AD_A3_E7_A2_BA_E7_8E_87(_E5_88_86_E5_AD_90, _E5_88_86_E6_AF_8D):
    global _E6_95_B8_E5_80_BC, _E9_81_8A_E6_88_B2_E7_8B_80_E6_85_8B, _E5_B9_80_E6_95_B8, _E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F, _E9_81_8A_E6_88_B2_E6_AC_A1_E6_95_B8, _E7_8E_A9_E5_AE_B6_E7_9A_84x_E5_BA_A7_E6_A8_99, _E9_81_8E_E9_97_9C_E6_AC_A1_E6_95_B8, _E7_8E_A9_E5_AE_B6_E7_9A_84y_E5_BA_A7_E6_A8_99, AI_E6_A8_A1_E5_9E_8B, _E7_8E_A9_E5_AE_B6_E8_A1_8C_E5_8B_95, _E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_85_A5, _E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_87_BA
    return ''.join([str(x) for x in ['正確率=', _E5_88_86_E5_AD_90, '/', _E5_88_86_E6_AF_8D, '(', _E5_8F_96_E5_88_B0_E5_B0_8F_E6_95_B8_E9_BB_9E_E4_BB_A5_E4_B8_8B4_E4_BD_8D(_E5_88_86_E5_AD_90 / _E5_88_86_E6_AF_8D), ')']])

# 描述此函式...
def _E5_88_9D_E5_A7_8B_E5_8C_96_E7_8E_A9_E9_81_8A_E6_88_B2_E8_AE_8A_E6_95_B8():
    global _E6_95_B8_E5_80_BC, _E5_88_86_E5_AD_90, _E5_88_86_E6_AF_8D, _E9_81_8A_E6_88_B2_E7_8B_80_E6_85_8B, _E5_B9_80_E6_95_B8, _E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F, _E9_81_8A_E6_88_B2_E6_AC_A1_E6_95_B8, _E7_8E_A9_E5_AE_B6_E7_9A_84x_E5_BA_A7_E6_A8_99, _E9_81_8E_E9_97_9C_E6_AC_A1_E6_95_B8, _E7_8E_A9_E5_AE_B6_E7_9A_84y_E5_BA_A7_E6_A8_99, AI_E6_A8_A1_E5_9E_8B, _E7_8E_A9_E5_AE_B6_E8_A1_8C_E5_8B_95, _E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_85_A5, _E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_87_BA
    _E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F = 0
    _E7_8E_A9_E5_AE_B6_E7_9A_84x_E5_BA_A7_E6_A8_99 = 0
    _E7_8E_A9_E5_AE_B6_E7_9A_84y_E5_BA_A7_E6_A8_99 = 0
    _E7_8E_A9_E5_AE_B6_E8_A1_8C_E5_8B_95 = 0

if sys.stdout == sys.__stdout__:
    sys.stdout = io.TextIOWrapper(open(sys.stdout.fileno(), 'wb', 0), encoding='utf-8', write_through=True)

# 描述此函式...
def _E8_BC_B8_E5_87_BA_E9_81_8A_E6_88_B2_E6_88_90_E7_B8_BE():
    global _E6_95_B8_E5_80_BC, _E5_88_86_E5_AD_90, _E5_88_86_E6_AF_8D, _E9_81_8A_E6_88_B2_E7_8B_80_E6_85_8B, _E5_B9_80_E6_95_B8, _E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F, _E9_81_8A_E6_88_B2_E6_AC_A1_E6_95_B8, _E7_8E_A9_E5_AE_B6_E7_9A_84x_E5_BA_A7_E6_A8_99, _E9_81_8E_E9_97_9C_E6_AC_A1_E6_95_B8, _E7_8E_A9_E5_AE_B6_E7_9A_84y_E5_BA_A7_E6_A8_99, AI_E6_A8_A1_E5_9E_8B, _E7_8E_A9_E5_AE_B6_E8_A1_8C_E5_8B_95, _E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_85_A5, _E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_87_BA
    print(''.join([str(x2) for x2 in ['過關！' if _E9_81_8A_E6_88_B2_E7_8B_80_E6_85_8B == "GAME_PASS" else '失敗！', '(總幀數=', _E5_B9_80_E6_95_B8, ')', _E6_AD_A3_E7_A2_BA_E7_8E_87(_E9_81_8E_E9_97_9C_E6_AC_A1_E6_95_B8, _E9_81_8A_E6_88_B2_E6_AC_A1_E6_95_B8)]]))


class MLPlay:
    def __init__(self, ai_name, *args, **kwargs):
        global _E6_95_B8_E5_80_BC, _E5_88_86_E5_AD_90, _E5_88_86_E6_AF_8D, _E9_81_8A_E6_88_B2_E7_8B_80_E6_85_8B, _E5_B9_80_E6_95_B8, _E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F, _E9_81_8A_E6_88_B2_E6_AC_A1_E6_95_B8, _E7_8E_A9_E5_AE_B6_E7_9A_84x_E5_BA_A7_E6_A8_99, _E9_81_8E_E9_97_9C_E6_AC_A1_E6_95_B8, _E7_8E_A9_E5_AE_B6_E7_9A_84y_E5_BA_A7_E6_A8_99, AI_E6_A8_A1_E5_9E_8B, _E7_8E_A9_E5_AE_B6_E8_A1_8C_E5_8B_95, _E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_85_A5, _E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_87_BA
        _E5_88_9D_E5_A7_8B_E5_8C_96_E9_81_8A_E6_88_B2_E6_88_90_E7_B8_BE_E8_AE_8A_E6_95_B8()
        _E5_88_9D_E5_A7_8B_E5_8C_96_E7_8E_A9_E9_81_8A_E6_88_B2_E8_AE_8A_E6_95_B8()
        with open(os.path.join(os.path.dirname(__file__), '模型_訓練產生的' + '.pickle'), 'rb') as f:
            AI_E6_A8_A1_E5_9E_8B = pickle.load(f)
    def update(self, scene_info, keyboard=[], *args, **kwargs):
        global _E6_95_B8_E5_80_BC, _E5_88_86_E5_AD_90, _E5_88_86_E6_AF_8D, _E9_81_8A_E6_88_B2_E7_8B_80_E6_85_8B, _E5_B9_80_E6_95_B8, _E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F, _E9_81_8A_E6_88_B2_E6_AC_A1_E6_95_B8, _E7_8E_A9_E5_AE_B6_E7_9A_84x_E5_BA_A7_E6_A8_99, _E9_81_8E_E9_97_9C_E6_AC_A1_E6_95_B8, _E7_8E_A9_E5_AE_B6_E7_9A_84y_E5_BA_A7_E6_A8_99, AI_E6_A8_A1_E5_9E_8B, _E7_8E_A9_E5_AE_B6_E8_A1_8C_E5_8B_95, _E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_85_A5, _E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_87_BA
        _E5_B9_80_E6_95_B8 = scene_info['frame']
        _E9_81_8A_E6_88_B2_E7_8B_80_E6_85_8B = scene_info['status']
        # 失敗的遊戲紀錄，可以不收集喔!
        if _E9_81_8A_E6_88_B2_E7_8B_80_E6_85_8B == "GAME_ALIVE":
            _E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F = scene_info['id']
            _E7_8E_A9_E5_AE_B6_E7_9A_84x_E5_BA_A7_E6_A8_99 = scene_info['x']
            _E7_8E_A9_E5_AE_B6_E7_9A_84y_E5_BA_A7_E6_A8_99 = scene_info['y']
            _E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_85_A5 = [[_E7_8E_A9_E5_AE_B6_E7_9A_84x_E5_BA_A7_E6_A8_99, _E7_8E_A9_E5_AE_B6_E7_9A_84y_E5_BA_A7_E6_A8_99]]
            # 利用AI模型預測移動方向，1代表向右移動，2代表向左移動
            _E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_87_BA = AI_E6_A8_A1_E5_9E_8B.predict(_E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_85_A5).tolist()
            _E7_8E_A9_E5_AE_B6_E8_A1_8C_E5_8B_95 = _E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_87_BA[0]
            if _E7_8E_A9_E5_AE_B6_E8_A1_8C_E5_8B_95 == 1:
                return ['SPEED']
            elif _E7_8E_A9_E5_AE_B6_E8_A1_8C_E5_8B_95 == 2:
                return ['BRAKE']
            elif _E7_8E_A9_E5_AE_B6_E8_A1_8C_E5_8B_95 == 3:
                return ['MOVE_LEFT']
            elif _E7_8E_A9_E5_AE_B6_E8_A1_8C_E5_8B_95 == 4:
                return ['MOVE_RIGHT']
        else:
            _E9_81_8A_E6_88_B2_E6_AC_A1_E6_95_B8 = (_E9_81_8A_E6_88_B2_E6_AC_A1_E6_95_B8 if isinstance(_E9_81_8A_E6_88_B2_E6_AC_A1_E6_95_B8, Number) else 0) + 1
            # 失敗的遊戲紀錄，可以不收集喔!
            if _E9_81_8A_E6_88_B2_E7_8B_80_E6_85_8B == "GAME_PASS":
                _E9_81_8E_E9_97_9C_E6_AC_A1_E6_95_B8 = (_E9_81_8E_E9_97_9C_E6_AC_A1_E6_95_B8 if isinstance(_E9_81_8E_E9_97_9C_E6_AC_A1_E6_95_B8, Number) else 0) + 1
            _E8_BC_B8_E5_87_BA_E9_81_8A_E6_88_B2_E6_88_90_E7_B8_BE()
            return "RESET"
    def reset(self):
        global _E6_95_B8_E5_80_BC, _E5_88_86_E5_AD_90, _E5_88_86_E6_AF_8D, _E9_81_8A_E6_88_B2_E7_8B_80_E6_85_8B, _E5_B9_80_E6_95_B8, _E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F, _E9_81_8A_E6_88_B2_E6_AC_A1_E6_95_B8, _E7_8E_A9_E5_AE_B6_E7_9A_84x_E5_BA_A7_E6_A8_99, _E9_81_8E_E9_97_9C_E6_AC_A1_E6_95_B8, _E7_8E_A9_E5_AE_B6_E7_9A_84y_E5_BA_A7_E6_A8_99, AI_E6_A8_A1_E5_9E_8B, _E7_8E_A9_E5_AE_B6_E8_A1_8C_E5_8B_95, _E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_85_A5, _E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_87_BA
        pass
