import json
import random
import logging

# # Configure the logging module
logging.basicConfig(level=logging.DEBUG,  # Set the logging level to DEBUG
                    format="[%(asctime)s]   [%(name)s]  [%(levelname)s] %(message)s")

# Create a logger instance for your module
logger = logging.getLogger(__name__)

class MLPlay:
    def __init__(self,ai_name,*args, **kwargs):

        logger.info(f"Initial ai_client : {ai_name}")

    def update(self, scene_info: dict, *args, **kwargs):
        """
        Generate the command according to the received scene information
        """
        logger.debug("AI received data from game :"+ json.dumps(scene_info))

        actions = ["UP", "DOWN", "LEFT", "RIGHT"]

        return random.sample(actions, 1)

    def reset(self):
        """
        Reset the status
        """
        print("reset ml script")
        pass
