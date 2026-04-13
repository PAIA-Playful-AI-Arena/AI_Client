import math
import pickle
import os

x1 = None
y1 = None
x2 = None
y2 = None
_E5_81_B5_E6_B8_AC_E7_AF_84_E5_9C_8D = None
AI_E7_B7_A8_E8_99_9F = None
_E9_A3_9F_E7_89_A9_E6_B8_85_E5_96_AE = None
_E6_9C_80_E8_BF_91_E8_B7_9D_E9_9B_A2 = None
_E4_B8_8A = None
_E7_89_B9_E5_BE_B5_E6_B8_85_E5_96_AE = None
_E7_8E_A9_E5_AE_B6x = None
i = None
_E5_8F_B3 = None
_E6_96_B9_E5_90_91_E6_B8_85_E5_96_AE = None
_E7_8E_A9_E5_AE_B6y = None
_E9_A3_9F_E7_89_A9_E6_B8_85_E5_96_AE = None
_E8_B7_9D_E9_9B_A2 = None
_E4_B8_8B = None
_E8_B3_87_E6_96_99_E7_AD_86_E6_95_B8 = None
_E7_8E_A9_E5_AE_B6_E5_AF_AC = None
_E5_B7_A6 = None
_E7_8E_A9_E5_AE_B6_E9_AB_98 = None
_E6_A8_A1_E5_9E_8B = None
_E6_9C_AC_E6_AC_A1_E7_89_B9_E5_BE_B5_E6_B8_85_E5_96_AE = None
_E5_B0_8D_E6_89_8Bx = None
_E9_A3_9F_E7_89_A9x = None
_E5_88_86_E6_95_B8 = None
_E5_B0_8D_E6_89_8By = None
_E9_A3_9F_E7_89_A9y = None
_E9_81_8A_E6_88_B2_E7_8B_80_E6_85_8B = None
_E7_9B_AE_E5_88_86 = None
_E7_A0_B4_E5_88_86 = None
_E7_8E_A9_E5_AE_B6_E7_AD_89_E7_B4_9A = None
_E5_B0_8D_E6_89_8B_E7_AD_89_E7_B4_9A = None
_E4_B8_8A_E9_82_8A = None
_E4_B8_8B_E9_82_8A = None
_E5_B7_A6_E9_82_8A = None
_E5_8F_B3_E9_82_8A = None
_E9_A0_90_E6_B8_AC_E7_B5_90_E6_9E_9C = None
_E6_96_B9_E5_90_91 = None

# 描述此函式...
def _E6_94_B6_E9_9B_86_E8_B3_87_E6_96_99():
    global x1, y1, x2, y2, _E5_81_B5_E6_B8_AC_E7_AF_84_E5_9C_8D, AI_E7_B7_A8_E8_99_9F, _E9_A3_9F_E7_89_A9_E6_B8_85_E5_96_AE, _E6_9C_80_E8_BF_91_E8_B7_9D_E9_9B_A2, _E4_B8_8A, _E7_89_B9_E5_BE_B5_E6_B8_85_E5_96_AE, _E7_8E_A9_E5_AE_B6x, i, _E5_8F_B3, _E6_96_B9_E5_90_91_E6_B8_85_E5_96_AE, _E7_8E_A9_E5_AE_B6y, _E9_A3_9F_E7_89_A9_E6_B8_85_E5_96_AE, _E8_B7_9D_E9_9B_A2, _E4_B8_8B, _E8_B3_87_E6_96_99_E7_AD_86_E6_95_B8, _E7_8E_A9_E5_AE_B6_E5_AF_AC, _E5_B7_A6, _E7_8E_A9_E5_AE_B6_E9_AB_98, _E6_A8_A1_E5_9E_8B, _E6_9C_AC_E6_AC_A1_E7_89_B9_E5_BE_B5_E6_B8_85_E5_96_AE, _E5_B0_8D_E6_89_8Bx, _E9_A3_9F_E7_89_A9x, _E5_88_86_E6_95_B8, _E5_B0_8D_E6_89_8By, _E9_A3_9F_E7_89_A9y, _E9_81_8A_E6_88_B2_E7_8B_80_E6_85_8B, _E7_9B_AE_E5_88_86, _E7_A0_B4_E5_88_86, _E7_8E_A9_E5_AE_B6_E7_AD_89_E7_B4_9A, _E5_B0_8D_E6_89_8B_E7_AD_89_E7_B4_9A, _E4_B8_8A_E9_82_8A, _E4_B8_8B_E9_82_8A, _E5_B7_A6_E9_82_8A, _E5_8F_B3_E9_82_8A, _E9_A0_90_E6_B8_AC_E7_B5_90_E6_9E_9C, _E6_96_B9_E5_90_91
    _E5_81_B5_E6_B8_AC_E7_AF_84_E5_9C_8D = 79
    _E4_B8_8A = 0
    _E5_8F_B3 = 0
    _E4_B8_8B = 0
    _E5_B7_A6 = 0
    for i in _E9_A3_9F_E7_89_A9_E6_B8_85_E5_96_AE:
        _E9_A3_9F_E7_89_A9x = i['x']
        _E9_A3_9F_E7_89_A9y = i['y']
        _E5_88_86_E6_95_B8 = i['score']
        if _E9_A3_9F_E7_89_A9x >= _E7_8E_A9_E5_AE_B6x and math.fabs(_E7_8E_A9_E5_AE_B6y - _E9_A3_9F_E7_89_A9y) < _E5_81_B5_E6_B8_AC_E7_AF_84_E5_9C_8D:
            _E5_8F_B3 = _E5_8F_B3 + _E5_88_86_E6_95_B8
        elif _E9_A3_9F_E7_89_A9x < _E7_8E_A9_E5_AE_B6x and math.fabs(_E7_8E_A9_E5_AE_B6y - _E9_A3_9F_E7_89_A9y) < _E5_81_B5_E6_B8_AC_E7_AF_84_E5_9C_8D:
            _E5_B7_A6 = _E5_B7_A6 + _E5_88_86_E6_95_B8
        if _E9_A3_9F_E7_89_A9y >= _E7_8E_A9_E5_AE_B6y and math.fabs(_E7_8E_A9_E5_AE_B6x - _E9_A3_9F_E7_89_A9x) < _E5_81_B5_E6_B8_AC_E7_AF_84_E5_9C_8D:
            _E4_B8_8B = _E4_B8_8B + _E5_88_86_E6_95_B8
        elif _E9_A3_9F_E7_89_A9y < _E7_8E_A9_E5_AE_B6y and math.fabs(_E7_8E_A9_E5_AE_B6x - _E9_A3_9F_E7_89_A9x) < _E5_81_B5_E6_B8_AC_E7_AF_84_E5_9C_8D:
            _E4_B8_8A = _E4_B8_8A + _E5_88_86_E6_95_B8
    _E5_88_86_E6_95_B8 = (_E7_8E_A9_E5_AE_B6_E7_AD_89_E7_B4_9A - _E5_B0_8D_E6_89_8B_E7_AD_89_E7_B4_9A) * 66 + -6
    if _E5_B0_8D_E6_89_8Bx >= _E7_8E_A9_E5_AE_B6x and math.fabs(_E7_8E_A9_E5_AE_B6y - _E5_B0_8D_E6_89_8By) < _E5_81_B5_E6_B8_AC_E7_AF_84_E5_9C_8D:
        _E5_8F_B3 = _E5_8F_B3 + _E5_88_86_E6_95_B8
    elif _E5_B0_8D_E6_89_8Bx < _E7_8E_A9_E5_AE_B6x and math.fabs(_E7_8E_A9_E5_AE_B6y - _E5_B0_8D_E6_89_8By) < _E5_81_B5_E6_B8_AC_E7_AF_84_E5_9C_8D:
        _E5_B7_A6 = _E5_B7_A6 + _E5_88_86_E6_95_B8
    if _E5_B0_8D_E6_89_8By >= _E7_8E_A9_E5_AE_B6y and math.fabs(_E7_8E_A9_E5_AE_B6x - _E5_B0_8D_E6_89_8Bx) < _E5_81_B5_E6_B8_AC_E7_AF_84_E5_9C_8D:
        _E4_B8_8B = _E4_B8_8B + _E5_88_86_E6_95_B8
    elif _E5_B0_8D_E6_89_8By < _E7_8E_A9_E5_AE_B6y and math.fabs(_E7_8E_A9_E5_AE_B6x - _E5_B0_8D_E6_89_8By) < _E5_81_B5_E6_B8_AC_E7_AF_84_E5_9C_8D:
        _E4_B8_8A = _E4_B8_8A + _E5_88_86_E6_95_B8
    if math.fabs(_E7_8E_A9_E5_AE_B6y - _E4_B8_8A_E9_82_8A) < 80:
        _E4_B8_8A = _E4_B8_8A + -80
    if math.fabs(_E7_8E_A9_E5_AE_B6y - _E4_B8_8B_E9_82_8A) < 50:
        _E4_B8_8B = _E4_B8_8B + -50
    if math.fabs(_E7_8E_A9_E5_AE_B6x - _E5_B7_A6_E9_82_8A) < 50:
        _E5_B7_A6 = _E5_B7_A6 + -50
    if math.fabs(_E7_8E_A9_E5_AE_B6x - _E5_8F_B3_E9_82_8A) < 50:
        _E5_8F_B3 = _E5_8F_B3 + -50
    _E6_9C_AC_E6_AC_A1_E7_89_B9_E5_BE_B5_E6_B8_85_E5_96_AE = [_E4_B8_8A, _E5_8F_B3, _E4_B8_8B, _E5_B7_A6]
    _E7_89_B9_E5_BE_B5_E6_B8_85_E5_96_AE.append(_E6_9C_AC_E6_AC_A1_E7_89_B9_E5_BE_B5_E6_B8_85_E5_96_AE)

class MLPlayArgsSaver:
    def __init__(self):
        self.ai_name = None

        self.init_kwargs = None
        self.scene_info = None
        self.keyboard = None

mlplayArgs = MLPlayArgsSaver()

# 描述此函式...
def _E8_A8_88_E7_AE_97_E8_B7_9D_E9_9B_A2(x1, y1, x2, y2):
    global _E5_81_B5_E6_B8_AC_E7_AF_84_E5_9C_8D, AI_E7_B7_A8_E8_99_9F, _E9_A3_9F_E7_89_A9_E6_B8_85_E5_96_AE, _E6_9C_80_E8_BF_91_E8_B7_9D_E9_9B_A2, _E4_B8_8A, _E7_89_B9_E5_BE_B5_E6_B8_85_E5_96_AE, _E7_8E_A9_E5_AE_B6x, i, _E5_8F_B3, _E6_96_B9_E5_90_91_E6_B8_85_E5_96_AE, _E7_8E_A9_E5_AE_B6y, _E9_A3_9F_E7_89_A9_E6_B8_85_E5_96_AE, _E8_B7_9D_E9_9B_A2, _E4_B8_8B, _E8_B3_87_E6_96_99_E7_AD_86_E6_95_B8, _E7_8E_A9_E5_AE_B6_E5_AF_AC, _E5_B7_A6, _E7_8E_A9_E5_AE_B6_E9_AB_98, _E6_A8_A1_E5_9E_8B, _E6_9C_AC_E6_AC_A1_E7_89_B9_E5_BE_B5_E6_B8_85_E5_96_AE, _E5_B0_8D_E6_89_8Bx, _E9_A3_9F_E7_89_A9x, _E5_88_86_E6_95_B8, _E5_B0_8D_E6_89_8By, _E9_A3_9F_E7_89_A9y, _E9_81_8A_E6_88_B2_E7_8B_80_E6_85_8B, _E7_9B_AE_E5_88_86, _E7_A0_B4_E5_88_86, _E7_8E_A9_E5_AE_B6_E7_AD_89_E7_B4_9A, _E5_B0_8D_E6_89_8B_E7_AD_89_E7_B4_9A, _E4_B8_8A_E9_82_8A, _E4_B8_8B_E9_82_8A, _E5_B7_A6_E9_82_8A, _E5_8F_B3_E9_82_8A, _E9_A0_90_E6_B8_AC_E7_B5_90_E6_9E_9C, _E6_96_B9_E5_90_91
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# 描述此函式...
def _E8_A8_88_E7_AE_97_E9_A3_9F_E7_89_A9_E6_9C_80_E7_9F_AD_E8_B7_9D_E9_9B_A2():
    global x1, y1, x2, y2, _E5_81_B5_E6_B8_AC_E7_AF_84_E5_9C_8D, AI_E7_B7_A8_E8_99_9F, _E9_A3_9F_E7_89_A9_E6_B8_85_E5_96_AE, _E6_9C_80_E8_BF_91_E8_B7_9D_E9_9B_A2, _E4_B8_8A, _E7_89_B9_E5_BE_B5_E6_B8_85_E5_96_AE, _E7_8E_A9_E5_AE_B6x, i, _E5_8F_B3, _E6_96_B9_E5_90_91_E6_B8_85_E5_96_AE, _E7_8E_A9_E5_AE_B6y, _E9_A3_9F_E7_89_A9_E6_B8_85_E5_96_AE, _E8_B7_9D_E9_9B_A2, _E4_B8_8B, _E8_B3_87_E6_96_99_E7_AD_86_E6_95_B8, _E7_8E_A9_E5_AE_B6_E5_AF_AC, _E5_B7_A6, _E7_8E_A9_E5_AE_B6_E9_AB_98, _E6_A8_A1_E5_9E_8B, _E6_9C_AC_E6_AC_A1_E7_89_B9_E5_BE_B5_E6_B8_85_E5_96_AE, _E5_B0_8D_E6_89_8Bx, _E9_A3_9F_E7_89_A9x, _E5_88_86_E6_95_B8, _E5_B0_8D_E6_89_8By, _E9_A3_9F_E7_89_A9y, _E9_81_8A_E6_88_B2_E7_8B_80_E6_85_8B, _E7_9B_AE_E5_88_86, _E7_A0_B4_E5_88_86, _E7_8E_A9_E5_AE_B6_E7_AD_89_E7_B4_9A, _E5_B0_8D_E6_89_8B_E7_AD_89_E7_B4_9A, _E4_B8_8A_E9_82_8A, _E4_B8_8B_E9_82_8A, _E5_B7_A6_E9_82_8A, _E5_8F_B3_E9_82_8A, _E9_A0_90_E6_B8_AC_E7_B5_90_E6_9E_9C, _E6_96_B9_E5_90_91
    _E6_9C_80_E8_BF_91_E8_B7_9D_E9_9B_A2 = 0
    for i in _E9_A3_9F_E7_89_A9_E6_B8_85_E5_96_AE:
        _E8_B7_9D_E9_9B_A2 = _E8_A8_88_E7_AE_97_E8_B7_9D_E9_9B_A2(_E7_8E_A9_E5_AE_B6x, _E7_8E_A9_E5_AE_B6y, i[''], i[''])
        if False:
            pass


class MLPlay:
    def __init__(self, ai_name, *args, **kwargs):
        global x1, y1, x2, y2, _E5_81_B5_E6_B8_AC_E7_AF_84_E5_9C_8D, AI_E7_B7_A8_E8_99_9F, _E9_A3_9F_E7_89_A9_E6_B8_85_E5_96_AE, _E6_9C_80_E8_BF_91_E8_B7_9D_E9_9B_A2, _E4_B8_8A, _E7_89_B9_E5_BE_B5_E6_B8_85_E5_96_AE, _E7_8E_A9_E5_AE_B6x, i, _E5_8F_B3, _E6_96_B9_E5_90_91_E6_B8_85_E5_96_AE, _E7_8E_A9_E5_AE_B6y, _E9_A3_9F_E7_89_A9_E6_B8_85_E5_96_AE, _E8_B7_9D_E9_9B_A2, _E4_B8_8B, _E8_B3_87_E6_96_99_E7_AD_86_E6_95_B8, _E7_8E_A9_E5_AE_B6_E5_AF_AC, _E5_B7_A6, _E7_8E_A9_E5_AE_B6_E9_AB_98, _E6_A8_A1_E5_9E_8B, _E6_9C_AC_E6_AC_A1_E7_89_B9_E5_BE_B5_E6_B8_85_E5_96_AE, _E5_B0_8D_E6_89_8Bx, _E9_A3_9F_E7_89_A9x, _E5_88_86_E6_95_B8, _E5_B0_8D_E6_89_8By, _E9_A3_9F_E7_89_A9y, _E9_81_8A_E6_88_B2_E7_8B_80_E6_85_8B, _E7_9B_AE_E5_88_86, _E7_A0_B4_E5_88_86, _E7_8E_A9_E5_AE_B6_E7_AD_89_E7_B4_9A, _E5_B0_8D_E6_89_8B_E7_AD_89_E7_B4_9A, _E4_B8_8A_E9_82_8A, _E4_B8_8B_E9_82_8A, _E5_B7_A6_E9_82_8A, _E5_8F_B3_E9_82_8A, _E9_A0_90_E6_B8_AC_E7_B5_90_E6_9E_9C, _E6_96_B9_E5_90_91
        mlplayArgs.ai_name = ai_name
        mlplayArgs.init_kwargs = kwargs
        AI_E7_B7_A8_E8_99_9F = mlplayArgs.ai_name
        _E7_89_B9_E5_BE_B5_E6_B8_85_E5_96_AE = []
        _E6_96_B9_E5_90_91_E6_B8_85_E5_96_AE = []
        _E8_B3_87_E6_96_99_E7_AD_86_E6_95_B8 = 0
        # 載入2P的AI模型
        with open(os.path.join(os.path.dirname(__file__), 'model' + '.pickle'), 'rb') as f:
            _E6_A8_A1_E5_9E_8B = pickle.load(f)
        _E6_9C_AC_E6_AC_A1_E7_89_B9_E5_BE_B5_E6_B8_85_E5_96_AE = []
    def update(self, scene_info, keyboard=[], *args, **kwargs):
        global x1, y1, x2, y2, _E5_81_B5_E6_B8_AC_E7_AF_84_E5_9C_8D, AI_E7_B7_A8_E8_99_9F, _E9_A3_9F_E7_89_A9_E6_B8_85_E5_96_AE, _E6_9C_80_E8_BF_91_E8_B7_9D_E9_9B_A2, _E4_B8_8A, _E7_89_B9_E5_BE_B5_E6_B8_85_E5_96_AE, _E7_8E_A9_E5_AE_B6x, i, _E5_8F_B3, _E6_96_B9_E5_90_91_E6_B8_85_E5_96_AE, _E7_8E_A9_E5_AE_B6y, _E9_A3_9F_E7_89_A9_E6_B8_85_E5_96_AE, _E8_B7_9D_E9_9B_A2, _E4_B8_8B, _E8_B3_87_E6_96_99_E7_AD_86_E6_95_B8, _E7_8E_A9_E5_AE_B6_E5_AF_AC, _E5_B7_A6, _E7_8E_A9_E5_AE_B6_E9_AB_98, _E6_A8_A1_E5_9E_8B, _E6_9C_AC_E6_AC_A1_E7_89_B9_E5_BE_B5_E6_B8_85_E5_96_AE, _E5_B0_8D_E6_89_8Bx, _E9_A3_9F_E7_89_A9x, _E5_88_86_E6_95_B8, _E5_B0_8D_E6_89_8By, _E9_A3_9F_E7_89_A9y, _E9_81_8A_E6_88_B2_E7_8B_80_E6_85_8B, _E7_9B_AE_E5_88_86, _E7_A0_B4_E5_88_86, _E7_8E_A9_E5_AE_B6_E7_AD_89_E7_B4_9A, _E5_B0_8D_E6_89_8B_E7_AD_89_E7_B4_9A, _E4_B8_8A_E9_82_8A, _E4_B8_8B_E9_82_8A, _E5_B7_A6_E9_82_8A, _E5_8F_B3_E9_82_8A, _E9_A0_90_E6_B8_AC_E7_B5_90_E6_9E_9C, _E6_96_B9_E5_90_91
        mlplayArgs.scene_info = scene_info
        mlplayArgs.keyboard = keyboard
        _E9_A3_9F_E7_89_A9_E6_B8_85_E5_96_AE = (mlplayArgs.scene_info['foods'] if mlplayArgs.scene_info is not None else None)
        _E7_8E_A9_E5_AE_B6x = (mlplayArgs.scene_info['self_x'] if mlplayArgs.scene_info is not None else None)
        _E7_8E_A9_E5_AE_B6y = (mlplayArgs.scene_info['self_y'] if mlplayArgs.scene_info is not None else None)
        _E5_B0_8D_E6_89_8Bx = (mlplayArgs.scene_info['opponent_x'] if mlplayArgs.scene_info is not None else None)
        _E5_B0_8D_E6_89_8By = (mlplayArgs.scene_info['opponent_y'] if mlplayArgs.scene_info is not None else None)
        _E9_81_8A_E6_88_B2_E7_8B_80_E6_85_8B = (mlplayArgs.scene_info['status'] if mlplayArgs.scene_info is not None else None)
        _E7_9B_AE_E5_88_86 = (mlplayArgs.scene_info['score'] if mlplayArgs.scene_info is not None else None)
        _E7_A0_B4_E5_88_86 = (mlplayArgs.scene_info['score_to_pass'] if mlplayArgs.scene_info is not None else None)
        _E7_8E_A9_E5_AE_B6_E7_AD_89_E7_B4_9A = (mlplayArgs.scene_info['self_lv'] if mlplayArgs.scene_info is not None else None)
        _E5_B0_8D_E6_89_8B_E7_AD_89_E7_B4_9A = (mlplayArgs.scene_info['opponent_lv'] if mlplayArgs.scene_info is not None else None)
        _E4_B8_8A_E9_82_8A = (mlplayArgs.scene_info['env']['top'] if mlplayArgs.scene_info is not None else None)
        _E4_B8_8B_E9_82_8A = (mlplayArgs.scene_info['env']['bottom'] if mlplayArgs.scene_info is not None else None)
        _E5_B7_A6_E9_82_8A = (mlplayArgs.scene_info['env']['left'] if mlplayArgs.scene_info is not None else None)
        _E5_8F_B3_E9_82_8A = (mlplayArgs.scene_info['env']['right'] if mlplayArgs.scene_info is not None else None)
        _E6_94_B6_E9_9B_86_E8_B3_87_E6_96_99()
        _E9_A0_90_E6_B8_AC_E7_B5_90_E6_9E_9C = _E6_A8_A1_E5_9E_8B.predict([_E6_9C_AC_E6_AC_A1_E7_89_B9_E5_BE_B5_E6_B8_85_E5_96_AE]).tolist()
        _E6_96_B9_E5_90_91 = _E9_A0_90_E6_B8_AC_E7_B5_90_E6_9E_9C[0]
        if _E6_96_B9_E5_90_91 == 1:
            return ['UP']
        elif _E6_96_B9_E5_90_91 == 2:
            return ['RIGHT']
        elif _E6_96_B9_E5_90_91 == 3:
            return ['DOWN']
        elif _E6_96_B9_E5_90_91 == 4:
            return ['LEFT']
    def reset(self):
        global x1, y1, x2, y2, _E5_81_B5_E6_B8_AC_E7_AF_84_E5_9C_8D, AI_E7_B7_A8_E8_99_9F, _E9_A3_9F_E7_89_A9_E6_B8_85_E5_96_AE, _E6_9C_80_E8_BF_91_E8_B7_9D_E9_9B_A2, _E4_B8_8A, _E7_89_B9_E5_BE_B5_E6_B8_85_E5_96_AE, _E7_8E_A9_E5_AE_B6x, i, _E5_8F_B3, _E6_96_B9_E5_90_91_E6_B8_85_E5_96_AE, _E7_8E_A9_E5_AE_B6y, _E9_A3_9F_E7_89_A9_E6_B8_85_E5_96_AE, _E8_B7_9D_E9_9B_A2, _E4_B8_8B, _E8_B3_87_E6_96_99_E7_AD_86_E6_95_B8, _E7_8E_A9_E5_AE_B6_E5_AF_AC, _E5_B7_A6, _E7_8E_A9_E5_AE_B6_E9_AB_98, _E6_A8_A1_E5_9E_8B, _E6_9C_AC_E6_AC_A1_E7_89_B9_E5_BE_B5_E6_B8_85_E5_96_AE, _E5_B0_8D_E6_89_8Bx, _E9_A3_9F_E7_89_A9x, _E5_88_86_E6_95_B8, _E5_B0_8D_E6_89_8By, _E9_A3_9F_E7_89_A9y, _E9_81_8A_E6_88_B2_E7_8B_80_E6_85_8B, _E7_9B_AE_E5_88_86, _E7_A0_B4_E5_88_86, _E7_8E_A9_E5_AE_B6_E7_AD_89_E7_B4_9A, _E5_B0_8D_E6_89_8B_E7_AD_89_E7_B4_9A, _E4_B8_8A_E9_82_8A, _E4_B8_8B_E9_82_8A, _E5_B7_A6_E9_82_8A, _E5_8F_B3_E9_82_8A, _E9_A0_90_E6_B8_AC_E7_B5_90_E6_9E_9C, _E6_96_B9_E5_90_91
        pass
