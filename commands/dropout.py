from dataclasses import dataclass

from .base import Command
from utils.get_base_dir import BASE_DIR
from utils.logging import logger
from utils.get_twister_schedule import get_twister_schedule
from helpers.drop_twister import DropTwister
from helpers.reschedule import Reschedule


@dataclass
class DropOut(Command):
    baloon_twister_name: str
    
    def process(self):
        with open(f"{BASE_DIR}/extras/balloon_twisters.dat", "r") as f:
            balloon_twisters = f.readlines()
        
        if f"{self.baloon_twister_name}\n" in balloon_twisters:
            balloon_twisters.remove(f"{self.baloon_twister_name}\n")
            with open(f"{BASE_DIR}/extras/balloon_twisters.dat", "w") as f:
                f.write(balloon_twisters[0])
            for twister in balloon_twisters[1:]:
                with open(f"{BASE_DIR}/extras/balloon_twisters.dat", "a") as f:
                    f.write(twister)
            twister_schedule = get_twister_schedule(self.baloon_twister_name)    
            DropTwister(self.baloon_twister_name).drop()
            Reschedule(twister_schedule).update()
            logger.info("User has been removed.")
        else:
            logger.info("No registered user with that name.")
    