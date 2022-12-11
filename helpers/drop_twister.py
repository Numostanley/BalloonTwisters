from dataclasses import dataclass

from utils.get_schedules import get_schedules
from helpers.update_schedule import UpdateSchedule

@dataclass
class DropTwister:
    balloon_twister: str
    
    def drop(self) -> None:
        schedules = get_schedules()
        del schedules[self.balloon_twister]
        UpdateSchedule(schedules).update()
        