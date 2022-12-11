from dataclasses import dataclass

from .base import Command
from utils.get_unbooked_twisters import get_unbooked_twisters
from helpers.book_balloon_twister import BookTwister
from utils.get_schedules import get_schedules


@dataclass
class Schedule(Command):
    customer_name: str
    holiday: str
    
    def process(self):
        schedules = get_schedules()
        data = {"customer_name": f"{self.customer_name}", "holiday": f"{self.holiday}"}
        unbooked_twisters = get_unbooked_twisters(schedules)
        BookTwister(unbooked_twisters, schedules, data).book()
        return 
