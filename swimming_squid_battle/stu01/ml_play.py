import math
import pickle
import os

_E5_81_B5_E6_B8_AC_E7_AF_84_E5_9C_8D = None
_E6_96_B9_E5_90_91 = None
_E6_9C_AC_E6_AC_A1_E7_89_B9_E5_BE_B5_E6_B8_85_E5_96_AE = None
_E9_A3_9F_E7_89_A9_E6_B8_85_E5_96_AE = None
_E4_B8_8A = None
_E7_89_B9_E5_BE_B5 = None
_E7_8E_A9_E5_AE_B6x = None
_E5_8F_B3 = None
_E7_9B_AE_E6_A8_99 = None
_E7_8E_A9_E5_AE_B6y = None
_E4_B8_8B = None
AI_E6_A8_A1_E5_9E_8B = None
_E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99 = None
_E7_8E_A9_E5_AE_B6_E7_AD_89_E7_B4_9A = None
_E5_B7_A6 = None
_E8_A8_93_E7_B7_B4_E7_9B_AE_E6_A8_99 = None
_E5_B0_8D_E6_89_8Bx = None
i = None
_E5_B0_8D_E6_89_8By = None
_E9_A3_9F_E7_89_A9x = None
_E5_88_86_E6_95_B8 = None
_E5_B0_8D_E6_89_8B_E7_AD_89_E7_B4_9A = None
_E9_A3_9F_E7_89_A9y = None

class MLPlayArgsSaver:
    def __init__(self):
        self.ai_name = None

        self.init_kwargs = None
        self.scene_info = None
        self.keyboard = None

mlplayArgs = MLPlayArgsSaver()

# 描述此函式...
def _E6_94_B6_E9_9B_86_E8_B3_87_E6_96_992():
    global _E5_81_B5_E6_B8_AC_E7_AF_84_E5_9C_8D, _E6_96_B9_E5_90_91, _E6_9C_AC_E6_AC_A1_E7_89_B9_E5_BE_B5_E6_B8_85_E5_96_AE, _E9_A3_9F_E7_89_A9_E6_B8_85_E5_96_AE, _E4_B8_8A, _E7_89_B9_E5_BE_B5, _E7_8E_A9_E5_AE_B6x, _E5_8F_B3, _E7_9B_AE_E6_A8_99, _E7_8E_A9_E5_AE_B6y, _E4_B8_8B, AI_E6_A8_A1_E5_9E_8B, _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99, _E7_8E_A9_E5_AE_B6_E7_AD_89_E7_B4_9A, _E5_B7_A6, _E8_A8_93_E7_B7_B4_E7_9B_AE_E6_A8_99, _E5_B0_8D_E6_89_8Bx, i, _E5_B0_8D_E6_89_8By, _E9_A3_9F_E7_89_A9x, _E5_88_86_E6_95_B8, _E5_B0_8D_E6_89_8B_E7_AD_89_E7_B4_9A, _E9_A3_9F_E7_89_A9y
    _E5_81_B5_E6_B8_AC_E7_AF_84_E5_9C_8D = 50
    _E4_B8_8A = 0
    _E5_8F_B3 = 0
    _E4_B8_8B = 0
    _E5_B7_A6 = 0
    for i in _E9_A3_9F_E7_89_A9_E6_B8_85_E5_96_AE:
        _E9_A3_9F_E7_89_A9x = i['x']
        _E9_A3_9F_E7_89_A9y = i['y']
        _E5_88_86_E6_95_B8 = i['score']
        if _E9_A3_9F_E7_89_A9x > _E7_8E_A9_E5_AE_B6x and math.fabs(_E9_A3_9F_E7_89_A9y - _E7_8E_A9_E5_AE_B6y) < _E5_81_B5_E6_B8_AC_E7_AF_84_E5_9C_8D:
            _E5_8F_B3 = _E5_8F_B3 + _E5_88_86_E6_95_B8
        if _E9_A3_9F_E7_89_A9x < _E7_8E_A9_E5_AE_B6x and math.fabs(_E9_A3_9F_E7_89_A9y - _E7_8E_A9_E5_AE_B6y) < _E5_81_B5_E6_B8_AC_E7_AF_84_E5_9C_8D:
            _E5_B7_A6 = _E5_B7_A6 + _E5_88_86_E6_95_B8
        if _E9_A3_9F_E7_89_A9y > _E7_8E_A9_E5_AE_B6y and math.fabs(_E9_A3_9F_E7_89_A9x - _E7_8E_A9_E5_AE_B6x) < _E5_81_B5_E6_B8_AC_E7_AF_84_E5_9C_8D:
            _E4_B8_8B = _E4_B8_8B + _E5_88_86_E6_95_B8
        if _E9_A3_9F_E7_89_A9y < _E7_8E_A9_E5_AE_B6y and math.fabs(_E9_A3_9F_E7_89_A9x - _E7_8E_A9_E5_AE_B6x) < _E5_81_B5_E6_B8_AC_E7_AF_84_E5_9C_8D:
            _E4_B8_8A = _E4_B8_8A + _E5_88_86_E6_95_B8
    _E5_88_86_E6_95_B8 = (_E7_8E_A9_E5_AE_B6_E7_AD_89_E7_B4_9A - _E5_B0_8D_E6_89_8B_E7_AD_89_E7_B4_9A) * 50
    if _E5_B0_8D_E6_89_8Bx > _E7_8E_A9_E5_AE_B6x and math.fabs(_E5_B0_8D_E6_89_8By - _E7_8E_A9_E5_AE_B6y) < _E5_81_B5_E6_B8_AC_E7_AF_84_E5_9C_8D:
        _E5_8F_B3 = _E5_8F_B3 + _E5_88_86_E6_95_B8
    if _E5_B0_8D_E6_89_8Bx < _E7_8E_A9_E5_AE_B6x and math.fabs(_E5_B0_8D_E6_89_8By - _E7_8E_A9_E5_AE_B6y) < _E5_81_B5_E6_B8_AC_E7_AF_84_E5_9C_8D:
        _E5_B7_A6 = _E5_B7_A6 + _E5_88_86_E6_95_B8
    if _E5_B0_8D_E6_89_8By > _E7_8E_A9_E5_AE_B6y and math.fabs(_E5_B0_8D_E6_89_8Bx - _E7_8E_A9_E5_AE_B6x) < _E5_81_B5_E6_B8_AC_E7_AF_84_E5_9C_8D:
        _E4_B8_8B = _E4_B8_8B + _E5_88_86_E6_95_B8
    if _E5_B0_8D_E6_89_8By < _E7_8E_A9_E5_AE_B6y and math.fabs(_E5_B0_8D_E6_89_8Bx - _E7_8E_A9_E5_AE_B6x) < _E5_81_B5_E6_B8_AC_E7_AF_84_E5_9C_8D:
        _E4_B8_8A = _E4_B8_8A + _E5_88_86_E6_95_B8
    if math.fabs(_E7_8E_A9_E5_AE_B6y - (mlplayArgs.scene_info['env']['top'] if mlplayArgs.scene_info is not None else None)) < 50:
        _E4_B8_8A = _E4_B8_8A - 70
    if math.fabs(_E7_8E_A9_E5_AE_B6y - (mlplayArgs.scene_info['env']['bottom'] if mlplayArgs.scene_info is not None else None)) < 50:
        _E4_B8_8B = _E4_B8_8B - 70
    if math.fabs(_E7_8E_A9_E5_AE_B6x - (mlplayArgs.scene_info['env']['left'] if mlplayArgs.scene_info is not None else None)) < 50:
        _E5_B7_A6 = _E5_B7_A6 - 70
    if math.fabs(_E7_8E_A9_E5_AE_B6x - (mlplayArgs.scene_info['env']['right'] if mlplayArgs.scene_info is not None else None)) < 50:
        _E5_8F_B3 = _E5_8F_B3 - 70
    _E6_9C_AC_E6_AC_A1_E7_89_B9_E5_BE_B5_E6_B8_85_E5_96_AE = [[_E4_B8_8A, _E5_8F_B3, _E4_B8_8B, _E5_B7_A6]]

# 描述此函式...
def _E5_88_A4_E5_AE_9A_E6_96_B9_E5_90_912():
    global _E5_81_B5_E6_B8_AC_E7_AF_84_E5_9C_8D, _E6_96_B9_E5_90_91, _E6_9C_AC_E6_AC_A1_E7_89_B9_E5_BE_B5_E6_B8_85_E5_96_AE, _E9_A3_9F_E7_89_A9_E6_B8_85_E5_96_AE, _E4_B8_8A, _E7_89_B9_E5_BE_B5, _E7_8E_A9_E5_AE_B6x, _E5_8F_B3, _E7_9B_AE_E6_A8_99, _E7_8E_A9_E5_AE_B6y, _E4_B8_8B, AI_E6_A8_A1_E5_9E_8B, _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99, _E7_8E_A9_E5_AE_B6_E7_AD_89_E7_B4_9A, _E5_B7_A6, _E8_A8_93_E7_B7_B4_E7_9B_AE_E6_A8_99, _E5_B0_8D_E6_89_8Bx, i, _E5_B0_8D_E6_89_8By, _E9_A3_9F_E7_89_A9x, _E5_88_86_E6_95_B8, _E5_B0_8D_E6_89_8B_E7_AD_89_E7_B4_9A, _E9_A3_9F_E7_89_A9y
    _E6_96_B9_E5_90_91 = AI_E6_A8_A1_E5_9E_8B.predict(_E6_9C_AC_E6_AC_A1_E7_89_B9_E5_BE_B5_E6_B8_85_E5_96_AE).tolist()[-1]


class MLPlay:
    def __init__(self, ai_name, *args, **kwargs):
        global _E5_81_B5_E6_B8_AC_E7_AF_84_E5_9C_8D, _E6_96_B9_E5_90_91, _E6_9C_AC_E6_AC_A1_E7_89_B9_E5_BE_B5_E6_B8_85_E5_96_AE, _E9_A3_9F_E7_89_A9_E6_B8_85_E5_96_AE, _E4_B8_8A, _E7_89_B9_E5_BE_B5, _E7_8E_A9_E5_AE_B6x, _E5_8F_B3, _E7_9B_AE_E6_A8_99, _E7_8E_A9_E5_AE_B6y, _E4_B8_8B, AI_E6_A8_A1_E5_9E_8B, _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99, _E7_8E_A9_E5_AE_B6_E7_AD_89_E7_B4_9A, _E5_B7_A6, _E8_A8_93_E7_B7_B4_E7_9B_AE_E6_A8_99, _E5_B0_8D_E6_89_8Bx, i, _E5_B0_8D_E6_89_8By, _E9_A3_9F_E7_89_A9x, _E5_88_86_E6_95_B8, _E5_B0_8D_E6_89_8B_E7_AD_89_E7_B4_9A, _E9_A3_9F_E7_89_A9y
        mlplayArgs.ai_name = ai_name
        mlplayArgs.init_kwargs = kwargs
        _E6_9C_AC_E6_AC_A1_E7_89_B9_E5_BE_B5_E6_B8_85_E5_96_AE = []
        _E7_89_B9_E5_BE_B5 = []
        _E7_9B_AE_E6_A8_99 = []
        _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99 = []
        _E8_A8_93_E7_B7_B4_E7_9B_AE_E6_A8_99 = []
        with open(os.path.join(os.path.dirname(__file__), 'AI模型' + '.pickle'), 'rb') as f:
            AI_E6_A8_A1_E5_9E_8B = pickle.load(f)
    def update(self, scene_info, keyboard=[], *args, **kwargs):
        global _E5_81_B5_E6_B8_AC_E7_AF_84_E5_9C_8D, _E6_96_B9_E5_90_91, _E6_9C_AC_E6_AC_A1_E7_89_B9_E5_BE_B5_E6_B8_85_E5_96_AE, _E9_A3_9F_E7_89_A9_E6_B8_85_E5_96_AE, _E4_B8_8A, _E7_89_B9_E5_BE_B5, _E7_8E_A9_E5_AE_B6x, _E5_8F_B3, _E7_9B_AE_E6_A8_99, _E7_8E_A9_E5_AE_B6y, _E4_B8_8B, AI_E6_A8_A1_E5_9E_8B, _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99, _E7_8E_A9_E5_AE_B6_E7_AD_89_E7_B4_9A, _E5_B7_A6, _E8_A8_93_E7_B7_B4_E7_9B_AE_E6_A8_99, _E5_B0_8D_E6_89_8Bx, i, _E5_B0_8D_E6_89_8By, _E9_A3_9F_E7_89_A9x, _E5_88_86_E6_95_B8, _E5_B0_8D_E6_89_8B_E7_AD_89_E7_B4_9A, _E9_A3_9F_E7_89_A9y
        mlplayArgs.scene_info = scene_info
        mlplayArgs.keyboard = keyboard
        _E9_A3_9F_E7_89_A9_E6_B8_85_E5_96_AE = (mlplayArgs.scene_info['foods'] if mlplayArgs.scene_info is not None else None)
        _E7_8E_A9_E5_AE_B6x = (mlplayArgs.scene_info['self_x'] if mlplayArgs.scene_info is not None else None)
        _E7_8E_A9_E5_AE_B6y = (mlplayArgs.scene_info['self_y'] if mlplayArgs.scene_info is not None else None)
        _E7_8E_A9_E5_AE_B6_E7_AD_89_E7_B4_9A = (mlplayArgs.scene_info['self_lv'] if mlplayArgs.scene_info is not None else None)
        _E5_B0_8D_E6_89_8Bx = (mlplayArgs.scene_info['opponent_x'] if mlplayArgs.scene_info is not None else None)
        _E5_B0_8D_E6_89_8By = (mlplayArgs.scene_info['opponent_y'] if mlplayArgs.scene_info is not None else None)
        _E5_B0_8D_E6_89_8B_E7_AD_89_E7_B4_9A = (mlplayArgs.scene_info['opponent_lv'] if mlplayArgs.scene_info is not None else None)
        _E6_94_B6_E9_9B_86_E8_B3_87_E6_96_992()
        _E5_88_A4_E5_AE_9A_E6_96_B9_E5_90_912()
        if _E6_96_B9_E5_90_91 == 1:
            return ['UP']
        if _E6_96_B9_E5_90_91 == 2:
            return ['RIGHT']
        if _E6_96_B9_E5_90_91 == 3:
            return ['DOWN']
        if _E6_96_B9_E5_90_91 == 4:
            return ['LEFT']
    def reset(self):
        global _E5_81_B5_E6_B8_AC_E7_AF_84_E5_9C_8D, _E6_96_B9_E5_90_91, _E6_9C_AC_E6_AC_A1_E7_89_B9_E5_BE_B5_E6_B8_85_E5_96_AE, _E9_A3_9F_E7_89_A9_E6_B8_85_E5_96_AE, _E4_B8_8A, _E7_89_B9_E5_BE_B5, _E7_8E_A9_E5_AE_B6x, _E5_8F_B3, _E7_9B_AE_E6_A8_99, _E7_8E_A9_E5_AE_B6y, _E4_B8_8B, AI_E6_A8_A1_E5_9E_8B, _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99, _E7_8E_A9_E5_AE_B6_E7_AD_89_E7_B4_9A, _E5_B7_A6, _E8_A8_93_E7_B7_B4_E7_9B_AE_E6_A8_99, _E5_B0_8D_E6_89_8Bx, i, _E5_B0_8D_E6_89_8By, _E9_A3_9F_E7_89_A9x, _E5_88_86_E6_95_B8, _E5_B0_8D_E6_89_8B_E7_AD_89_E7_B4_9A, _E9_A3_9F_E7_89_A9y
        pass
