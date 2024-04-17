import pickle
import os
import csv
from pynput import keyboard
from collections import defaultdict
from numbers import Number

_KEYBOARD_ON_PRESSED = None
_E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99 = None
_E9_A6_AC_E9_81_94_E8_BD_89_E9_80_9F = None
_E8_B3_87_E6_96_99_E8_A8_88_E6_95_B8 = None

def on_press(key):
  _KEYBOARD_ON_PRESSED[str(key)] = True

def on_release(key):
  _KEYBOARD_ON_PRESSED[str(key)] = False

_KEYBOARD_ON_PRESSED = defaultdict(bool)
listener = keyboard.Listener(
  on_press=on_press,
  on_release=on_release)
listener.start()


class MLPlay:
  def __init__(self, player):
    global _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99, _E9_A6_AC_E9_81_94_E8_BD_89_E9_80_9F, _E8_B3_87_E6_96_99_E8_A8_88_E6_95_B8, _KEYBOARD_ON_PRESSED
    _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99 = []
    _E9_A6_AC_E9_81_94_E8_BD_89_E9_80_9F = []
    _E8_B3_87_E6_96_99_E8_A8_88_E6_95_B8 = 1
  def update(self, scene_info):
    global _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99, _E9_A6_AC_E9_81_94_E8_BD_89_E9_80_9F, _E8_B3_87_E6_96_99_E8_A8_88_E6_95_B8, _KEYBOARD_ON_PRESSED
    if scene_info['status'] != "GAME_ALIVE":
      with open(os.path.join(os.path.dirname(__file__), 'feature' + str(_E8_B3_87_E6_96_99_E8_A8_88_E6_95_B8) + '.pickle'), 'wb') as f:
        pickle.dump(_E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99, f)
      with open(os.path.join(os.path.dirname(__file__), 'target' + str(_E8_B3_87_E6_96_99_E8_A8_88_E6_95_B8) + '.pickle'), 'wb') as f:
        pickle.dump(_E9_A6_AC_E9_81_94_E8_BD_89_E9_80_9F, f)
      # 可以將收集的特徵數據，打開來看
      with open(os.path.join(os.path.dirname(__file__), 'feature' + str(_E8_B3_87_E6_96_99_E8_A8_88_E6_95_B8) + '.csv'), 'w', newline='') as f:
        csv.writer(f, delimiter=',').writerows(_E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99)
      # 可以將收集的馬達數據，打開來看
      with open(os.path.join(os.path.dirname(__file__), 'target' + str(_E8_B3_87_E6_96_99_E8_A8_88_E6_95_B8) + '.csv'), 'w', newline='') as f:
        csv.writer(f, delimiter=',').writerows(_E9_A6_AC_E9_81_94_E8_BD_89_E9_80_9F)
      return "RESET"
    else:
      # 特徵資料，不一定只有這五種，還可以自行增加喔!
      _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99.append([scene_info['L_sensor'], scene_info['L_T_sensor'], scene_info['F_sensor'], scene_info['R_T_sensor'], scene_info['R_sensor']])
      if _KEYBOARD_ON_PRESSED["Key.up"] or (_KEYBOARD_ON_PRESSED["'W'"] or _KEYBOARD_ON_PRESSED["'w'"]):
        _E9_A6_AC_E9_81_94_E8_BD_89_E9_80_9F.append([255, 255])
        return [{'left_PWM': 255, 'right_PWM': 255}]
      elif _KEYBOARD_ON_PRESSED["Key.down"] or (_KEYBOARD_ON_PRESSED["'S'"] or _KEYBOARD_ON_PRESSED["'s'"]):
        _E9_A6_AC_E9_81_94_E8_BD_89_E9_80_9F.append([-50, -50])
        return [{'left_PWM': -50, 'right_PWM': -50}]
      elif _KEYBOARD_ON_PRESSED["Key.right"] or (_KEYBOARD_ON_PRESSED["'D'"] or _KEYBOARD_ON_PRESSED["'d'"]):
        _E9_A6_AC_E9_81_94_E8_BD_89_E9_80_9F.append([50, -50])
        return [{'left_PWM': 50, 'right_PWM': -50}]
      elif _KEYBOARD_ON_PRESSED["Key.left"] or (_KEYBOARD_ON_PRESSED["'A'"] or _KEYBOARD_ON_PRESSED["'a'"]):
        _E9_A6_AC_E9_81_94_E8_BD_89_E9_80_9F.append([-50, 50])
        return [{'left_PWM': -50, 'right_PWM': 50}]
      else:
        _E9_A6_AC_E9_81_94_E8_BD_89_E9_80_9F.append([50, 50])
        return [{'left_PWM': 50, 'right_PWM': 50}]
  def reset(self):
    global _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99, _E9_A6_AC_E9_81_94_E8_BD_89_E9_80_9F, _E8_B3_87_E6_96_99_E8_A8_88_E6_95_B8, _KEYBOARD_ON_PRESSED
    _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99 = []
    _E9_A6_AC_E9_81_94_E8_BD_89_E9_80_9F = []
    _E8_B3_87_E6_96_99_E8_A8_88_E6_95_B8 = (_E8_B3_87_E6_96_99_E8_A8_88_E6_95_B8 if isinstance(_E8_B3_87_E6_96_99_E8_A8_88_E6_95_B8, Number) else 0) + 1
