"""
created_at_utc  : 2023-05-23T06:29:40Z
created_at_w3c  : 2023-05-23T14:29:40+08:00
PAIA-Desktop    : 2.4.1-competition-tn
MLGame          : 10.0.2
game            : racing_car
game_version    : 3.4.1
"""

import pickle
import os
from src import autoRCar

_E6_9C_AC_E6_AC_A1_E7_89_B9_E5_BE_B5 = None
_E7_9B_AE_E6_A8_99_E8_B3_BD_E9_81_93 = None
_E6_9C_AC_E8_BB_8A_E8_B3_BD_E9_81_93 = None
_E4_B8_8A_E6_AC_A1_E5_89_8D_E9_80_B2_E6_96_B9_E5_90_91 = None
model = None
_E5_89_8D_E9_80_B2_E6_96_B9_E5_90_91 = None
_E9_A0_90_E6_B8_AC_E7_B5_90_E6_9E_9C = None

autoCar = autoRCar.autoRCar()


class MLPlay:
    def __init__(self, ai_name, *args, **kwargs):
        global _E6_9C_AC_E6_AC_A1_E7_89_B9_E5_BE_B5, _E7_9B_AE_E6_A8_99_E8_B3_BD_E9_81_93, _E6_9C_AC_E8_BB_8A_E8_B3_BD_E9_81_93, _E4_B8_8A_E6_AC_A1_E5_89_8D_E9_80_B2_E6_96_B9_E5_90_91, model, _E5_89_8D_E9_80_B2_E6_96_B9_E5_90_91, _E9_A0_90_E6_B8_AC_E7_B5_90_E6_9E_9C
        _E6_9C_AC_E6_AC_A1_E7_89_B9_E5_BE_B5 = []
        _E7_9B_AE_E6_A8_99_E8_B3_BD_E9_81_93 = -1
        _E4_B8_8A_E6_AC_A1_E5_89_8D_E9_80_B2_E6_96_B9_E5_90_91 = 1
        with open(os.path.join(os.path.dirname(__file__), 'model' + '.pickle'), 'rb') as f:
            model = pickle.load(f)
    def update(self, scene_info, keyboard=[], *args, **kwargs):
        global _E6_9C_AC_E6_AC_A1_E7_89_B9_E5_BE_B5, _E7_9B_AE_E6_A8_99_E8_B3_BD_E9_81_93, _E6_9C_AC_E8_BB_8A_E8_B3_BD_E9_81_93, _E4_B8_8A_E6_AC_A1_E5_89_8D_E9_80_B2_E6_96_B9_E5_90_91, model, _E5_89_8D_E9_80_B2_E6_96_B9_E5_90_91, _E9_A0_90_E6_B8_AC_E7_B5_90_E6_9E_9C
        if scene_info['status'] != "GAME_ALIVE":
            return "RESET"
        else:
            _E6_9C_AC_E6_AC_A1_E7_89_B9_E5_BE_B5, _E6_9C_AC_E8_BB_8A_E8_B3_BD_E9_81_93 = autoCar.getCarInfo(scene_info, 80, 5)
            if _E7_9B_AE_E6_A8_99_E8_B3_BD_E9_81_93 == -1:
                _E7_9B_AE_E6_A8_99_E8_B3_BD_E9_81_93 = _E6_9C_AC_E8_BB_8A_E8_B3_BD_E9_81_93
            if _E7_9B_AE_E6_A8_99_E8_B3_BD_E9_81_93 != _E6_9C_AC_E8_BB_8A_E8_B3_BD_E9_81_93 and not autoCar.isCenterLane(_E7_9B_AE_E6_A8_99_E8_B3_BD_E9_81_93):
                _E5_89_8D_E9_80_B2_E6_96_B9_E5_90_91 = _E4_B8_8A_E6_AC_A1_E5_89_8D_E9_80_B2_E6_96_B9_E5_90_91
            else:
                _E9_A0_90_E6_B8_AC_E7_B5_90_E6_9E_9C = model.predict([_E6_9C_AC_E6_AC_A1_E7_89_B9_E5_BE_B5]).tolist()
                _E5_89_8D_E9_80_B2_E6_96_B9_E5_90_91 = _E9_A0_90_E6_B8_AC_E7_B5_90_E6_9E_9C[0]
            _E4_B8_8A_E6_AC_A1_E5_89_8D_E9_80_B2_E6_96_B9_E5_90_91 = _E5_89_8D_E9_80_B2_E6_96_B9_E5_90_91
            if _E5_89_8D_E9_80_B2_E6_96_B9_E5_90_91 == -1:
                _E7_9B_AE_E6_A8_99_E8_B3_BD_E9_81_93 = _E6_9C_AC_E8_BB_8A_E8_B3_BD_E9_81_93
                return ['BRAKE']
            elif _E5_89_8D_E9_80_B2_E6_96_B9_E5_90_91 == -5:
                _E7_9B_AE_E6_A8_99_E8_B3_BD_E9_81_93 = _E6_9C_AC_E8_BB_8A_E8_B3_BD_E9_81_93 - 1
                return ['SPEED', 'MOVE_LEFT']
            elif _E5_89_8D_E9_80_B2_E6_96_B9_E5_90_91 == 5:
                _E7_9B_AE_E6_A8_99_E8_B3_BD_E9_81_93 = _E6_9C_AC_E8_BB_8A_E8_B3_BD_E9_81_93 + 1
                return ['SPEED', 'MOVE_RIGHT']
            else:
                _E7_9B_AE_E6_A8_99_E8_B3_BD_E9_81_93 = _E6_9C_AC_E8_BB_8A_E8_B3_BD_E9_81_93
                return ['SPEED']
    def reset(self):
        global _E6_9C_AC_E6_AC_A1_E7_89_B9_E5_BE_B5, _E7_9B_AE_E6_A8_99_E8_B3_BD_E9_81_93, _E6_9C_AC_E8_BB_8A_E8_B3_BD_E9_81_93, _E4_B8_8A_E6_AC_A1_E5_89_8D_E9_80_B2_E6_96_B9_E5_90_91, model, _E5_89_8D_E9_80_B2_E6_96_B9_E5_90_91, _E9_A0_90_E6_B8_AC_E7_B5_90_E6_9E_9C
        _E7_9B_AE_E6_A8_99_E8_B3_BD_E9_81_93 = -1
        _E4_B8_8A_E6_AC_A1_E5_89_8D_E9_80_B2_E6_96_B9_E5_90_91 = 1
