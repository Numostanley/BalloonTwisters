from dataclasses import dataclass
from pprint import pprint

from .base import Command
from lists.holiday_list import Holiday
from lists.twisters_list import Twister

@dataclass
class Status(Command):
    holiday: str = None
    balloon_twister: str = None
    
    def process(self):
        if self.holiday:
            holiday_bookings = Holiday(self.holiday).get_list()
            pprint(holiday_bookings)
        elif self.balloon_twister:
            twister_bookings = Twister(self.balloon_twister).get_list()
            pprint(twister_bookings)
