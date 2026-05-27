"""
create_by         : exam_admin_01
create_at         : 2026-04-17 14:30:24
create_at_utc     : 2026-04-17T06:30:24Z
PAIA-Desktop      : 0.2.2
MLGame            : 0.7.2
game            : Proly
game_version    : 1.3.2
"""

class MLPlayArgsSaver:
    def __init__(self):
        self.name = None
        self.init_kwargs = None
        self.observations = None
        self.keyboard = None

mlplayArgs = MLPlayArgsSaver()


class MLPlay:
    def __init__(self, observation_structure, action_space_info, name, *args, **kwargs):
        mlplayArgs.name = name
        mlplayArgs.init_kwargs = kwargs
        pass
    def update(self, observations, done, info, keyboard=set(), *args, **kwargs):
        mlplayArgs.observations = observations
        mlplayArgs.keyboard = keyboard
        return ([0, 0], [0, 0])
    def reset(self):
        pass
