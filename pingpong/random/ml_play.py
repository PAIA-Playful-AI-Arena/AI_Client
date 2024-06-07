import random


class MLPlay:
    def __init__(self, ai_name, *args, **kwargs):

        self.served = False
        self.ai_name = ai_name
        print(ai_name)

    def update(self, scene_info, *args, **kwargs):
        if scene_info['status'] != "GAME_ALIVE":
            return "RESET"
        if not self.served:
            self.served = True
            return "SERVE_TO_RIGHT"

        return random.choice(["MOVE_LEFT", "MOVE_RIGHT"])

    def reset(self):
        self.served = False
