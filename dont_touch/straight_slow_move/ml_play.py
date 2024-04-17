class MLPlay:
    def __init__(self, ai_name, *args, **kwargs):
        self.player_no = ai_name
        self.r_sensor_value = 0
        self.l_sensor_value = 0
        self.f_sensor_value = 0
        self.control_list = {"left_PWM": 0, "right_PWM": 0}
        print(f"{ai_name} is moving in slow straight forward.")

    def update(self, scene_info: dict, keyboard: list = [], *args, **kwargs):
        """
        Generate the command according to the received scene information
        """
        if scene_info["status"] != "GAME_ALIVE":
            return "RESET"

        return {"left_PWM": 150, "right_PWM": 150}

    def reset(self):
        """
        Reset the status
        """
        # print("reset ml script")
        pass
