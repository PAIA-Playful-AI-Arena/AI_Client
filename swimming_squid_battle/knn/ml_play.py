"""
created_at_utc  : 2024-11-01T06:50:43Z
created_at_w3c  : 2024-11-01T14:50:43+08:00
PAIA-Desktop    : 3.0.6
MLGame          : 10.5.2
game            : swimming_squid_battle
game_version    : 1.5.1
"""

import pickle
import os
import sys
import io

_E9_A3_9F_E7_89_A9_E6_B8_85_E5_96_AE = None
_E5_81_B5_E6_B8_AC_E7_AF_84_E5_9C_8D = None
_E6_A8_A1_E5_9E_8B = None
_E6_9C_AC_E6_AC_A1_E7_89_B9_E5_BE_B5_E6_B8_85_E5_96_AE = None
myx = None
_E4_B8_8A = None
myy = None
_E5_8F_B3 = None
ox = None
_E4_B8_8B = None
oy = None
_E5_B7_A6 = None
_E6_88_91_E5_AF_AC = None
_E6_AF_8F_E9_9A_BB_E9_A3_9F_E7_89_A9 = None
_E6_88_91_E9_AB_98 = None
x = None
y = None
_E9_A0_90_E6_B8_AC_E7_B5_90_E6_9E_9C = None
_E5_88_86_E6_95_B8 = None
_E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91 = None

if sys.stdout == sys.__stdout__:
    sys.stdout = io.TextIOWrapper(open(sys.stdout.fileno(), 'wb', 0), encoding='utf-8', write_through=True)

# 描述此函式...
def _E6_94_B6_E9_9B_86_E8_B3_87_E6_96_99():
    global _E9_A3_9F_E7_89_A9_E6_B8_85_E5_96_AE, _E5_81_B5_E6_B8_AC_E7_AF_84_E5_9C_8D, _E6_A8_A1_E5_9E_8B, _E6_9C_AC_E6_AC_A1_E7_89_B9_E5_BE_B5_E6_B8_85_E5_96_AE, myx, _E4_B8_8A, myy, _E5_8F_B3, ox, _E4_B8_8B, oy, _E5_B7_A6, _E6_88_91_E5_AF_AC, _E6_AF_8F_E9_9A_BB_E9_A3_9F_E7_89_A9, _E6_88_91_E9_AB_98, x, y, _E9_A0_90_E6_B8_AC_E7_B5_90_E6_9E_9C, _E5_88_86_E6_95_B8, _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91
    _E5_81_B5_E6_B8_AC_E7_AF_84_E5_9C_8D = 200
    _E4_B8_8A = 0
    _E5_8F_B3 = 0
    _E4_B8_8B = 0
    _E5_B7_A6 = 0
    for _E6_AF_8F_E9_9A_BB_E9_A3_9F_E7_89_A9 in _E9_A3_9F_E7_89_A9_E6_B8_85_E5_96_AE:
        x = _E6_AF_8F_E9_9A_BB_E9_A3_9F_E7_89_A9['x']
        y = _E6_AF_8F_E9_9A_BB_E9_A3_9F_E7_89_A9['y']
        _E5_88_86_E6_95_B8 = _E6_AF_8F_E9_9A_BB_E9_A3_9F_E7_89_A9['score']
        if myx - _E6_88_91_E5_AF_AC <= x and x <= myx + _E6_88_91_E5_AF_AC:
            if myy - _E5_81_B5_E6_B8_AC_E7_AF_84_E5_9C_8D <= y and y <= myy:
                _E4_B8_8A = _E4_B8_8A + _E5_88_86_E6_95_B8
            elif myy <= y and y <= myy + _E5_81_B5_E6_B8_AC_E7_AF_84_E5_9C_8D:
                _E4_B8_8B = _E4_B8_8B + _E5_88_86_E6_95_B8
        elif myy - _E6_88_91_E9_AB_98 <= y and y <= myy + _E6_88_91_E9_AB_98:
            if myx - _E5_81_B5_E6_B8_AC_E7_AF_84_E5_9C_8D <= x and x <= myx:
                _E5_B7_A6 = _E5_B7_A6 + _E5_88_86_E6_95_B8
            elif myx <= x and x <= myx + _E5_81_B5_E6_B8_AC_E7_AF_84_E5_9C_8D:
                _E5_8F_B3 = _E5_8F_B3 + _E5_88_86_E6_95_B8
    _E6_9C_AC_E6_AC_A1_E7_89_B9_E5_BE_B5_E6_B8_85_E5_96_AE = [_E4_B8_8A, _E5_8F_B3, _E4_B8_8B, _E5_B7_A6]


class MLPlay:
    def __init__(self, ai_name, *args, **kwargs):
        global _E9_A3_9F_E7_89_A9_E6_B8_85_E5_96_AE, _E5_81_B5_E6_B8_AC_E7_AF_84_E5_9C_8D, _E6_A8_A1_E5_9E_8B, _E6_9C_AC_E6_AC_A1_E7_89_B9_E5_BE_B5_E6_B8_85_E5_96_AE, myx, _E4_B8_8A, myy, _E5_8F_B3, ox, _E4_B8_8B, oy, _E5_B7_A6, _E6_88_91_E5_AF_AC, _E6_AF_8F_E9_9A_BB_E9_A3_9F_E7_89_A9, _E6_88_91_E9_AB_98, x, y, _E9_A0_90_E6_B8_AC_E7_B5_90_E6_9E_9C, _E5_88_86_E6_95_B8, _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91
        # 載入2P的AI模型
        with open(os.path.join(os.path.dirname(__file__), 'model' + '.pickle'), 'rb') as f:
            _E6_A8_A1_E5_9E_8B = pickle.load(f)
        _E6_9C_AC_E6_AC_A1_E7_89_B9_E5_BE_B5_E6_B8_85_E5_96_AE = []
    def update(self, scene_info, keyboard=[], *args, **kwargs):
        global _E9_A3_9F_E7_89_A9_E6_B8_85_E5_96_AE, _E5_81_B5_E6_B8_AC_E7_AF_84_E5_9C_8D, _E6_A8_A1_E5_9E_8B, _E6_9C_AC_E6_AC_A1_E7_89_B9_E5_BE_B5_E6_B8_85_E5_96_AE, myx, _E4_B8_8A, myy, _E5_8F_B3, ox, _E4_B8_8B, oy, _E5_B7_A6, _E6_88_91_E5_AF_AC, _E6_AF_8F_E9_9A_BB_E9_A3_9F_E7_89_A9, _E6_88_91_E9_AB_98, x, y, _E9_A0_90_E6_B8_AC_E7_B5_90_E6_9E_9C, _E5_88_86_E6_95_B8, _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91
        _E9_A3_9F_E7_89_A9_E6_B8_85_E5_96_AE = scene_info['foods']
        myx = scene_info['self_x']
        myy = scene_info['self_y']
        ox = scene_info['opponent_x']
        oy = scene_info['opponent_y']
        _E6_88_91_E5_AF_AC = scene_info['self_w']
        _E6_88_91_E9_AB_98 = scene_info['self_h']
        _E6_94_B6_E9_9B_86_E8_B3_87_E6_96_99()
        _E9_A0_90_E6_B8_AC_E7_B5_90_E6_9E_9C = _E6_A8_A1_E5_9E_8B.predict([_E6_9C_AC_E6_AC_A1_E7_89_B9_E5_BE_B5_E6_B8_85_E5_96_AE]).tolist()
        _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91 = _E9_A0_90_E6_B8_AC_E7_B5_90_E6_9E_9C[0]
        if _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91 == 1:
            return ['UP']
        elif _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91 == 2:
            return ['RIGHT']
        elif _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91 == 3:
            return ['DOWN']
        elif _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91 == 4:
            return ['LEFT']
    def reset(self):
        global _E9_A3_9F_E7_89_A9_E6_B8_85_E5_96_AE, _E5_81_B5_E6_B8_AC_E7_AF_84_E5_9C_8D, _E6_A8_A1_E5_9E_8B, _E6_9C_AC_E6_AC_A1_E7_89_B9_E5_BE_B5_E6_B8_85_E5_96_AE, myx, _E4_B8_8A, myy, _E5_8F_B3, ox, _E4_B8_8B, oy, _E5_B7_A6, _E6_88_91_E5_AF_AC, _E6_AF_8F_E9_9A_BB_E9_A3_9F_E7_89_A9, _E6_88_91_E9_AB_98, x, y, _E9_A0_90_E6_B8_AC_E7_B5_90_E6_9E_9C, _E5_88_86_E6_95_B8, _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91
        print('遊戲重置')
