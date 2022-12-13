from operator import itemgetter

from utils.get_schedules import get_schedules
from utils.logging import logger

class Twister:
    def __init__(self, name) -> None:
        self.twister_name = name
        self.schedule: list[dict] = []
    
    def get_list(self) -> list:
        schedules = get_schedules()
        try:
            self.schedule = sorted(schedules[self.twister_name], key=itemgetter("customer_name"))
        except KeyError as e:
            logger.info("Sorry there's no booking for this holiday.")
        
        return self.schedule
