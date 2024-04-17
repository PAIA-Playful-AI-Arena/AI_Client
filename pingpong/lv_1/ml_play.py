"""
created_at_utc  : 2022-12-16T09:51:54Z
created_at_w3c  : 2022-12-16T17:51:54+08:00
PAIA-Desktop    : 2.4.1
MLGame          : 10.0.2
game            : pingpong
game_version    : 2.3.1
"""

import pickle
import os
import random
import math
import sys
import io

_E6_95_B8_E5_80_BC = None
_E5_88_86_E5_AD_90 = None
_E5_88_86_E6_AF_8D = None
_E7_90_83x_E9_80_9F_E5_BA_A6 = None
_E7_90_83y_E9_80_9F_E5_BA_A6 = None
_E5_B9_80_E6_95_B8 = None
_E7_90_83_E7_9A_84x_E5_BA_A7_E6_A8_99 = None
_E9_81_8A_E6_88_B2_E7_8B_80_E6_85_8B = None
_E5_B7_B2_E7_B6_93_E7_99_BC_E7_90_83 = None
_E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F = None
_E7_99_BC_E7_90_83_E6_96_B9_E3_80_81_E6_96_B9_E5_90_91 = None
_E7_90_83_E7_9A_84y_E5_BA_A7_E6_A8_99 = None
_E9_81_8A_E6_88_B2_E6_AC_A1_E6_95_B8 = None
_E5_B9_B3_E5_8F_B0_E7_9A_84x_E5_BA_A7_E6_A8_99 = None
AI_E6_A8_A1_E5_9E_8B = None
_E7_90_83_E7_9A_84x_E6_96_B9_E5_90_91_E9_80_9F_E5_BA_A6 = None
_E5_B9_B3_E5_8F_B0_E8_A1_8C_E5_8B_95 = None
_E9_81_8E_E9_97_9C_E6_AC_A1_E6_95_B8 = None
_E7_90_83_E7_9A_84y_E6_96_B9_E5_90_91_E9_80_9F_E5_BA_A6 = None
_E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_85_A5 = None
_E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_87_BA = None

# 描述此函式...
def _E5_88_9D_E5_A7_8B_E5_8C_96_E9_81_8A_E6_88_B2_E6_88_90_E7_B8_BE_E8_AE_8A_E6_95_B8():
    global _E6_95_B8_E5_80_BC, _E5_88_86_E5_AD_90, _E5_88_86_E6_AF_8D, _E7_90_83x_E9_80_9F_E5_BA_A6, _E7_90_83y_E9_80_9F_E5_BA_A6, _E5_B9_80_E6_95_B8, _E7_90_83_E7_9A_84x_E5_BA_A7_E6_A8_99, _E9_81_8A_E6_88_B2_E7_8B_80_E6_85_8B, _E5_B7_B2_E7_B6_93_E7_99_BC_E7_90_83, _E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F, _E7_99_BC_E7_90_83_E6_96_B9_E3_80_81_E6_96_B9_E5_90_91, _E7_90_83_E7_9A_84y_E5_BA_A7_E6_A8_99, _E9_81_8A_E6_88_B2_E6_AC_A1_E6_95_B8, _E5_B9_B3_E5_8F_B0_E7_9A_84x_E5_BA_A7_E6_A8_99, AI_E6_A8_A1_E5_9E_8B, _E7_90_83_E7_9A_84x_E6_96_B9_E5_90_91_E9_80_9F_E5_BA_A6, _E5_B9_B3_E5_8F_B0_E8_A1_8C_E5_8B_95, _E9_81_8E_E9_97_9C_E6_AC_A1_E6_95_B8, _E7_90_83_E7_9A_84y_E6_96_B9_E5_90_91_E9_80_9F_E5_BA_A6, _E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_85_A5, _E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_87_BA
    _E5_B9_80_E6_95_B8 = 0
    _E9_81_8A_E6_88_B2_E7_8B_80_E6_85_8B = 0
    _E9_81_8A_E6_88_B2_E6_AC_A1_E6_95_B8 = {}
    _E9_81_8A_E6_88_B2_E6_AC_A1_E6_95_B8['1P'] = 0
    _E9_81_8A_E6_88_B2_E6_AC_A1_E6_95_B8['2P'] = 0
    _E9_81_8E_E9_97_9C_E6_AC_A1_E6_95_B8 = {}
    _E9_81_8E_E9_97_9C_E6_AC_A1_E6_95_B8['1P'] = 0
    _E9_81_8E_E9_97_9C_E6_AC_A1_E6_95_B8['2P'] = 0

# 描述此函式...
def _E5_8F_96_E5_88_B0_E5_B0_8F_E6_95_B8_E9_BB_9E_E4_BB_A5_E4_B8_8B4_E4_BD_8D(_E6_95_B8_E5_80_BC):
    global _E5_88_86_E5_AD_90, _E5_88_86_E6_AF_8D, _E7_90_83x_E9_80_9F_E5_BA_A6, _E7_90_83y_E9_80_9F_E5_BA_A6, _E5_B9_80_E6_95_B8, _E7_90_83_E7_9A_84x_E5_BA_A7_E6_A8_99, _E9_81_8A_E6_88_B2_E7_8B_80_E6_85_8B, _E5_B7_B2_E7_B6_93_E7_99_BC_E7_90_83, _E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F, _E7_99_BC_E7_90_83_E6_96_B9_E3_80_81_E6_96_B9_E5_90_91, _E7_90_83_E7_9A_84y_E5_BA_A7_E6_A8_99, _E9_81_8A_E6_88_B2_E6_AC_A1_E6_95_B8, _E5_B9_B3_E5_8F_B0_E7_9A_84x_E5_BA_A7_E6_A8_99, AI_E6_A8_A1_E5_9E_8B, _E7_90_83_E7_9A_84x_E6_96_B9_E5_90_91_E9_80_9F_E5_BA_A6, _E5_B9_B3_E5_8F_B0_E8_A1_8C_E5_8B_95, _E9_81_8E_E9_97_9C_E6_AC_A1_E6_95_B8, _E7_90_83_E7_9A_84y_E6_96_B9_E5_90_91_E9_80_9F_E5_BA_A6, _E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_85_A5, _E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_87_BA
    return round(_E6_95_B8_E5_80_BC * 10000) / 10000

if sys.stdout == sys.__stdout__:
    sys.stdout = io.TextIOWrapper(open(sys.stdout.fileno(), 'wb', 0), encoding='utf-8', write_through=True)

# 描述此函式...
def _E8_BC_B8_E5_87_BA_E9_81_8A_E6_88_B2_E6_88_90_E7_B8_BE():
    global _E6_95_B8_E5_80_BC, _E5_88_86_E5_AD_90, _E5_88_86_E6_AF_8D, _E7_90_83x_E9_80_9F_E5_BA_A6, _E7_90_83y_E9_80_9F_E5_BA_A6, _E5_B9_80_E6_95_B8, _E7_90_83_E7_9A_84x_E5_BA_A7_E6_A8_99, _E9_81_8A_E6_88_B2_E7_8B_80_E6_85_8B, _E5_B7_B2_E7_B6_93_E7_99_BC_E7_90_83, _E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F, _E7_99_BC_E7_90_83_E6_96_B9_E3_80_81_E6_96_B9_E5_90_91, _E7_90_83_E7_9A_84y_E5_BA_A7_E6_A8_99, _E9_81_8A_E6_88_B2_E6_AC_A1_E6_95_B8, _E5_B9_B3_E5_8F_B0_E7_9A_84x_E5_BA_A7_E6_A8_99, AI_E6_A8_A1_E5_9E_8B, _E7_90_83_E7_9A_84x_E6_96_B9_E5_90_91_E9_80_9F_E5_BA_A6, _E5_B9_B3_E5_8F_B0_E8_A1_8C_E5_8B_95, _E9_81_8E_E9_97_9C_E6_AC_A1_E6_95_B8, _E7_90_83_E7_9A_84y_E6_96_B9_E5_90_91_E9_80_9F_E5_BA_A6, _E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_85_A5, _E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_87_BA
    print(''.join([str(x4) for x4 in [_E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F, '過關！' if _E9_81_8E_E9_97_9C_E4_BA_86_E5_97_8E_() else '失敗！', math.fabs(_E7_90_83_E7_9A_84x_E6_96_B9_E5_90_91_E9_80_9F_E5_BA_A6), '(總幀數=', _E5_B9_80_E6_95_B8, ')', _E6_BA_96_E7_A2_BA_E7_8E_87(_E9_81_8E_E9_97_9C_E6_AC_A1_E6_95_B8[_E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F], _E9_81_8A_E6_88_B2_E6_AC_A1_E6_95_B8[_E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F])]]))

# 描述此函式...
def _E5_88_9D_E5_A7_8B_E5_8C_96_E7_8E_A9_E9_81_8A_E6_88_B2_E8_AE_8A_E6_95_B8():
    global _E6_95_B8_E5_80_BC, _E5_88_86_E5_AD_90, _E5_88_86_E6_AF_8D, _E7_90_83x_E9_80_9F_E5_BA_A6, _E7_90_83y_E9_80_9F_E5_BA_A6, _E5_B9_80_E6_95_B8, _E7_90_83_E7_9A_84x_E5_BA_A7_E6_A8_99, _E9_81_8A_E6_88_B2_E7_8B_80_E6_85_8B, _E5_B7_B2_E7_B6_93_E7_99_BC_E7_90_83, _E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F, _E7_99_BC_E7_90_83_E6_96_B9_E3_80_81_E6_96_B9_E5_90_91, _E7_90_83_E7_9A_84y_E5_BA_A7_E6_A8_99, _E9_81_8A_E6_88_B2_E6_AC_A1_E6_95_B8, _E5_B9_B3_E5_8F_B0_E7_9A_84x_E5_BA_A7_E6_A8_99, AI_E6_A8_A1_E5_9E_8B, _E7_90_83_E7_9A_84x_E6_96_B9_E5_90_91_E9_80_9F_E5_BA_A6, _E5_B9_B3_E5_8F_B0_E8_A1_8C_E5_8B_95, _E9_81_8E_E9_97_9C_E6_AC_A1_E6_95_B8, _E7_90_83_E7_9A_84y_E6_96_B9_E5_90_91_E9_80_9F_E5_BA_A6, _E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_85_A5, _E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_87_BA
    _E7_90_83_E7_9A_84x_E5_BA_A7_E6_A8_99 = 0
    _E7_90_83_E7_9A_84y_E5_BA_A7_E6_A8_99 = 0
    _E5_B9_B3_E5_8F_B0_E7_9A_84x_E5_BA_A7_E6_A8_99 = 0
    _E5_B9_B3_E5_8F_B0_E8_A1_8C_E5_8B_95 = 0
    _E5_B7_B2_E7_B6_93_E7_99_BC_E7_90_83 = {}
    _E5_B7_B2_E7_B6_93_E7_99_BC_E7_90_83['1P'] = False
    _E5_B7_B2_E7_B6_93_E7_99_BC_E7_90_83['2P'] = False
    _E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_85_A5 = []
    _E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_87_BA = []

# 取到小數點以下4位
def _E6_BA_96_E7_A2_BA_E7_8E_87(_E5_88_86_E5_AD_90, _E5_88_86_E6_AF_8D):
    global _E6_95_B8_E5_80_BC, _E7_90_83x_E9_80_9F_E5_BA_A6, _E7_90_83y_E9_80_9F_E5_BA_A6, _E5_B9_80_E6_95_B8, _E7_90_83_E7_9A_84x_E5_BA_A7_E6_A8_99, _E9_81_8A_E6_88_B2_E7_8B_80_E6_85_8B, _E5_B7_B2_E7_B6_93_E7_99_BC_E7_90_83, _E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F, _E7_99_BC_E7_90_83_E6_96_B9_E3_80_81_E6_96_B9_E5_90_91, _E7_90_83_E7_9A_84y_E5_BA_A7_E6_A8_99, _E9_81_8A_E6_88_B2_E6_AC_A1_E6_95_B8, _E5_B9_B3_E5_8F_B0_E7_9A_84x_E5_BA_A7_E6_A8_99, AI_E6_A8_A1_E5_9E_8B, _E7_90_83_E7_9A_84x_E6_96_B9_E5_90_91_E9_80_9F_E5_BA_A6, _E5_B9_B3_E5_8F_B0_E8_A1_8C_E5_8B_95, _E9_81_8E_E9_97_9C_E6_AC_A1_E6_95_B8, _E7_90_83_E7_9A_84y_E6_96_B9_E5_90_91_E9_80_9F_E5_BA_A6, _E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_85_A5, _E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_87_BA
    return ''.join([str(x5) for x5 in ['正確率=', _E5_88_86_E5_AD_90, '/', _E5_88_86_E6_AF_8D, '(', _E5_8F_96_E5_88_B0_E5_B0_8F_E6_95_B8_E9_BB_9E_E4_BB_A5_E4_B8_8B4_E4_BD_8D(_E5_88_86_E5_AD_90 / _E5_88_86_E6_AF_8D), ')']])

# 描述此函式...
def _E5_88_A4_E6_96_B7_E7_99_BC_E7_90_83_E6_96_B9_E8_88_87_E6_96_B9_E5_90_91(_E7_90_83x_E9_80_9F_E5_BA_A6, _E7_90_83y_E9_80_9F_E5_BA_A6):
    global _E6_95_B8_E5_80_BC, _E5_88_86_E5_AD_90, _E5_88_86_E6_AF_8D, _E5_B9_80_E6_95_B8, _E7_90_83_E7_9A_84x_E5_BA_A7_E6_A8_99, _E9_81_8A_E6_88_B2_E7_8B_80_E6_85_8B, _E5_B7_B2_E7_B6_93_E7_99_BC_E7_90_83, _E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F, _E7_99_BC_E7_90_83_E6_96_B9_E3_80_81_E6_96_B9_E5_90_91, _E7_90_83_E7_9A_84y_E5_BA_A7_E6_A8_99, _E9_81_8A_E6_88_B2_E6_AC_A1_E6_95_B8, _E5_B9_B3_E5_8F_B0_E7_9A_84x_E5_BA_A7_E6_A8_99, AI_E6_A8_A1_E5_9E_8B, _E7_90_83_E7_9A_84x_E6_96_B9_E5_90_91_E9_80_9F_E5_BA_A6, _E5_B9_B3_E5_8F_B0_E8_A1_8C_E5_8B_95, _E9_81_8E_E9_97_9C_E6_AC_A1_E6_95_B8, _E7_90_83_E7_9A_84y_E6_96_B9_E5_90_91_E9_80_9F_E5_BA_A6, _E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_85_A5, _E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_87_BA
    if _E7_90_83y_E9_80_9F_E5_BA_A6 < 0 and _E7_90_83x_E9_80_9F_E5_BA_A6 < 0:
        _E7_99_BC_E7_90_83_E6_96_B9_E3_80_81_E6_96_B9_E5_90_91 = 11
    elif _E7_90_83y_E9_80_9F_E5_BA_A6 < 0 and _E7_90_83x_E9_80_9F_E5_BA_A6 > 0:
        _E7_99_BC_E7_90_83_E6_96_B9_E3_80_81_E6_96_B9_E5_90_91 = 12
    elif _E7_90_83y_E9_80_9F_E5_BA_A6 > 0 and _E7_90_83x_E9_80_9F_E5_BA_A6 < 0:
        _E7_99_BC_E7_90_83_E6_96_B9_E3_80_81_E6_96_B9_E5_90_91 = 21
    elif _E7_90_83y_E9_80_9F_E5_BA_A6 > 0 and _E7_90_83x_E9_80_9F_E5_BA_A6 > 0:
        _E7_99_BC_E7_90_83_E6_96_B9_E3_80_81_E6_96_B9_E5_90_91 = 22

# 描述此函式...
def _E9_81_8E_E9_97_9C_E4_BA_86_E5_97_8E_():
    global _E6_95_B8_E5_80_BC, _E5_88_86_E5_AD_90, _E5_88_86_E6_AF_8D, _E7_90_83x_E9_80_9F_E5_BA_A6, _E7_90_83y_E9_80_9F_E5_BA_A6, _E5_B9_80_E6_95_B8, _E7_90_83_E7_9A_84x_E5_BA_A7_E6_A8_99, _E9_81_8A_E6_88_B2_E7_8B_80_E6_85_8B, _E5_B7_B2_E7_B6_93_E7_99_BC_E7_90_83, _E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F, _E7_99_BC_E7_90_83_E6_96_B9_E3_80_81_E6_96_B9_E5_90_91, _E7_90_83_E7_9A_84y_E5_BA_A7_E6_A8_99, _E9_81_8A_E6_88_B2_E6_AC_A1_E6_95_B8, _E5_B9_B3_E5_8F_B0_E7_9A_84x_E5_BA_A7_E6_A8_99, AI_E6_A8_A1_E5_9E_8B, _E7_90_83_E7_9A_84x_E6_96_B9_E5_90_91_E9_80_9F_E5_BA_A6, _E5_B9_B3_E5_8F_B0_E8_A1_8C_E5_8B_95, _E9_81_8E_E9_97_9C_E6_AC_A1_E6_95_B8, _E7_90_83_E7_9A_84y_E6_96_B9_E5_90_91_E9_80_9F_E5_BA_A6, _E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_85_A5, _E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_87_BA
    if _E9_81_8A_E6_88_B2_E7_8B_80_E6_85_8B == "GAME_1P_WIN" and _E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F == '1P':
        return True
    elif _E9_81_8A_E6_88_B2_E7_8B_80_E6_85_8B == "GAME_2P_WIN" and _E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F == '2P':
        return True
    elif _E9_81_8A_E6_88_B2_E7_8B_80_E6_85_8B == "GAME_DRAW":
        return True
    return False


class MLPlay:
    def __init__(self, ai_name, *args, **kwargs):
        global _E6_95_B8_E5_80_BC, _E5_88_86_E5_AD_90, _E5_88_86_E6_AF_8D, _E7_90_83x_E9_80_9F_E5_BA_A6, _E7_90_83y_E9_80_9F_E5_BA_A6, _E5_B9_80_E6_95_B8, _E7_90_83_E7_9A_84x_E5_BA_A7_E6_A8_99, _E9_81_8A_E6_88_B2_E7_8B_80_E6_85_8B, _E5_B7_B2_E7_B6_93_E7_99_BC_E7_90_83, _E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F, _E7_99_BC_E7_90_83_E6_96_B9_E3_80_81_E6_96_B9_E5_90_91, _E7_90_83_E7_9A_84y_E5_BA_A7_E6_A8_99, _E9_81_8A_E6_88_B2_E6_AC_A1_E6_95_B8, _E5_B9_B3_E5_8F_B0_E7_9A_84x_E5_BA_A7_E6_A8_99, AI_E6_A8_A1_E5_9E_8B, _E7_90_83_E7_9A_84x_E6_96_B9_E5_90_91_E9_80_9F_E5_BA_A6, _E5_B9_B3_E5_8F_B0_E8_A1_8C_E5_8B_95, _E9_81_8E_E9_97_9C_E6_AC_A1_E6_95_B8, _E7_90_83_E7_9A_84y_E6_96_B9_E5_90_91_E9_80_9F_E5_BA_A6, _E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_85_A5, _E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_87_BA
        _E5_88_9D_E5_A7_8B_E5_8C_96_E9_81_8A_E6_88_B2_E6_88_90_E7_B8_BE_E8_AE_8A_E6_95_B8()
        _E5_88_9D_E5_A7_8B_E5_8C_96_E7_8E_A9_E9_81_8A_E6_88_B2_E8_AE_8A_E6_95_B8()
        _E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F = ai_name
        AI_E6_A8_A1_E5_9E_8B = {}
        for _E7_99_BC_E7_90_83_E6_96_B9_E3_80_81_E6_96_B9_E5_90_91 in [11, 12, 21, 22]:
            with open(os.path.join(os.path.dirname(__file__), ''.join([str(x2) for x2 in ['模型_訓練產生的_', _E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F, '_', _E7_99_BC_E7_90_83_E6_96_B9_E3_80_81_E6_96_B9_E5_90_91]]) + '.pickle'), 'rb') as f:
                AI_E6_A8_A1_E5_9E_8B[''.join([str(x) for x in [_E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F, '_', _E7_99_BC_E7_90_83_E6_96_B9_E3_80_81_E6_96_B9_E5_90_91]])] = pickle.load(f)
        _E7_99_BC_E7_90_83_E6_96_B9_E3_80_81_E6_96_B9_E5_90_91 = 0
    def update(self, scene_info, keyboard=[], *args, **kwargs):
        global _E6_95_B8_E5_80_BC, _E5_88_86_E5_AD_90, _E5_88_86_E6_AF_8D, _E7_90_83x_E9_80_9F_E5_BA_A6, _E7_90_83y_E9_80_9F_E5_BA_A6, _E5_B9_80_E6_95_B8, _E7_90_83_E7_9A_84x_E5_BA_A7_E6_A8_99, _E9_81_8A_E6_88_B2_E7_8B_80_E6_85_8B, _E5_B7_B2_E7_B6_93_E7_99_BC_E7_90_83, _E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F, _E7_99_BC_E7_90_83_E6_96_B9_E3_80_81_E6_96_B9_E5_90_91, _E7_90_83_E7_9A_84y_E5_BA_A7_E6_A8_99, _E9_81_8A_E6_88_B2_E6_AC_A1_E6_95_B8, _E5_B9_B3_E5_8F_B0_E7_9A_84x_E5_BA_A7_E6_A8_99, AI_E6_A8_A1_E5_9E_8B, _E7_90_83_E7_9A_84x_E6_96_B9_E5_90_91_E9_80_9F_E5_BA_A6, _E5_B9_B3_E5_8F_B0_E8_A1_8C_E5_8B_95, _E9_81_8E_E9_97_9C_E6_AC_A1_E6_95_B8, _E7_90_83_E7_9A_84y_E6_96_B9_E5_90_91_E9_80_9F_E5_BA_A6, _E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_85_A5, _E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_87_BA
        _E5_B9_80_E6_95_B8 = scene_info['frame']
        _E9_81_8A_E6_88_B2_E7_8B_80_E6_85_8B = scene_info['status']
        # 失敗的遊戲紀錄，可以不收集喔!
        if _E9_81_8A_E6_88_B2_E7_8B_80_E6_85_8B == "GAME_ALIVE":
            if _E5_B7_B2_E7_B6_93_E7_99_BC_E7_90_83[_E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F]:
                _E7_90_83_E7_9A_84x_E5_BA_A7_E6_A8_99 = scene_info['ball'][0]
                _E7_90_83_E7_9A_84y_E5_BA_A7_E6_A8_99 = scene_info['ball'][1]
                _E7_90_83_E7_9A_84x_E6_96_B9_E5_90_91_E9_80_9F_E5_BA_A6 = scene_info['ball_speed'][0]
                _E7_90_83_E7_9A_84y_E6_96_B9_E5_90_91_E9_80_9F_E5_BA_A6 = scene_info['ball_speed'][1]
                if _E7_99_BC_E7_90_83_E6_96_B9_E3_80_81_E6_96_B9_E5_90_91 == 0:
                    _E5_88_A4_E6_96_B7_E7_99_BC_E7_90_83_E6_96_B9_E8_88_87_E6_96_B9_E5_90_91(_E7_90_83_E7_9A_84x_E6_96_B9_E5_90_91_E9_80_9F_E5_BA_A6, _E7_90_83_E7_9A_84y_E6_96_B9_E5_90_91_E9_80_9F_E5_BA_A6)
                else:
                    if _E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F == '1P':
                        _E5_B9_B3_E5_8F_B0_E7_9A_84x_E5_BA_A7_E6_A8_99 = scene_info['platform_1P'][0]
                    elif _E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F == '2P':
                        _E5_B9_B3_E5_8F_B0_E7_9A_84x_E5_BA_A7_E6_A8_99 = scene_info['platform_2P'][0]
                    _E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_85_A5 = [[_E7_90_83_E7_9A_84x_E6_96_B9_E5_90_91_E9_80_9F_E5_BA_A6, _E7_90_83_E7_9A_84y_E6_96_B9_E5_90_91_E9_80_9F_E5_BA_A6, _E7_90_83_E7_9A_84x_E5_BA_A7_E6_A8_99, _E7_90_83_E7_9A_84y_E5_BA_A7_E6_A8_99, _E5_B9_B3_E5_8F_B0_E7_9A_84x_E5_BA_A7_E6_A8_99]]
                    # 利用AI模型預測移動方向，1代表向右移動，2代表向左移動
                    _E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_87_BA = AI_E6_A8_A1_E5_9E_8B[''.join([str(x3) for x3 in [_E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F, '_', _E7_99_BC_E7_90_83_E6_96_B9_E3_80_81_E6_96_B9_E5_90_91]])].predict(_E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_85_A5).tolist()
                    _E5_B9_B3_E5_8F_B0_E8_A1_8C_E5_8B_95 = _E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_87_BA[0]
                    if scene_info['ball_speed'][0] > 15:
                        return "MOVE_LEFT"
                    if _E5_B9_B3_E5_8F_B0_E8_A1_8C_E5_8B_95 == 1:
                        return "MOVE_LEFT"
                    elif _E5_B9_B3_E5_8F_B0_E8_A1_8C_E5_8B_95 == 2:
                        return "MOVE_RIGHT"
                    elif _E5_B9_B3_E5_8F_B0_E8_A1_8C_E5_8B_95 == 3:
                        return "NONE"
            else:
                _E5_B7_B2_E7_B6_93_E7_99_BC_E7_90_83[_E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F] = True
                if random.randint(1, 2) == 1:
                    return "SERVE_TO_LEFT"
                else:
                    return "SERVE_TO_RIGHT"
        else:
            _E9_81_8A_E6_88_B2_E6_AC_A1_E6_95_B8[_E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F] = _E9_81_8A_E6_88_B2_E6_AC_A1_E6_95_B8[_E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F] + 1
            if _E9_81_8E_E9_97_9C_E4_BA_86_E5_97_8E_():
                _E9_81_8E_E9_97_9C_E6_AC_A1_E6_95_B8[_E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F] = _E9_81_8E_E9_97_9C_E6_AC_A1_E6_95_B8[_E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F] + 1
            _E8_BC_B8_E5_87_BA_E9_81_8A_E6_88_B2_E6_88_90_E7_B8_BE()
            return "RESET"
    def reset(self):
        global _E6_95_B8_E5_80_BC, _E5_88_86_E5_AD_90, _E5_88_86_E6_AF_8D, _E7_90_83x_E9_80_9F_E5_BA_A6, _E7_90_83y_E9_80_9F_E5_BA_A6, _E5_B9_80_E6_95_B8, _E7_90_83_E7_9A_84x_E5_BA_A7_E6_A8_99, _E9_81_8A_E6_88_B2_E7_8B_80_E6_85_8B, _E5_B7_B2_E7_B6_93_E7_99_BC_E7_90_83, _E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F, _E7_99_BC_E7_90_83_E6_96_B9_E3_80_81_E6_96_B9_E5_90_91, _E7_90_83_E7_9A_84y_E5_BA_A7_E6_A8_99, _E9_81_8A_E6_88_B2_E6_AC_A1_E6_95_B8, _E5_B9_B3_E5_8F_B0_E7_9A_84x_E5_BA_A7_E6_A8_99, AI_E6_A8_A1_E5_9E_8B, _E7_90_83_E7_9A_84x_E6_96_B9_E5_90_91_E9_80_9F_E5_BA_A6, _E5_B9_B3_E5_8F_B0_E8_A1_8C_E5_8B_95, _E9_81_8E_E9_97_9C_E6_AC_A1_E6_95_B8, _E7_90_83_E7_9A_84y_E6_96_B9_E5_90_91_E9_80_9F_E5_BA_A6, _E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_85_A5, _E6_A8_A1_E5_9E_8B_E8_BC_B8_E5_87_BA
        _E5_B7_B2_E7_B6_93_E7_99_BC_E7_90_83[_E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F] = False
        _E7_99_BC_E7_90_83_E6_96_B9_E3_80_81_E6_96_B9_E5_90_91 = 0
