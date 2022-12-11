from dataclasses import dataclass

from .base import Command
from utils.get_base_dir import BASE_DIR
from utils.logging import logger


@dataclass
class SignUp(Command):
    baloon_twister_name: str
    
    def process(self):
        with open(f"{BASE_DIR}/extras/balloon_twisters.dat", "r") as f:
            balloon_twisters = f.readlines()
        twisters_list = []
        for line in balloon_twisters:
            twister = line.split("\n")[0]
            twisters_list.append(twister)
        if self.baloon_twister_name in twisters_list:
            logger.info("User is already registered.")
        else:
            with open(f"{BASE_DIR}/extras/balloon_twisters.dat", "a") as f:
                f.write(f"\n{self.baloon_twister_name}")
            logger.info(f"{self.baloon_twister_name} has been registered.")
