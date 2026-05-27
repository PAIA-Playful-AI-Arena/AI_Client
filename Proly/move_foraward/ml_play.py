"""
create_by       : test_process
create_at       : 2026-05-27 14:25:44
create_at_utc   : 2026-05-27T06:25:44Z
PAIA-Desktop    : 3.3.2
MLGame          : 0.8.0
game            : Proly
game_version    : 1.4.1
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
        return ([(mlplayArgs.observations['target_position'][0] if mlplayArgs.observations is not None else None), (mlplayArgs.observations['target_position'][1] if mlplayArgs.observations is not None else None)], [0, 0])
    def reset(self):
        pass
