from dataclasses import dataclass

from .base import Command
from helpers.cancel_schedule import cancel_schedule

@dataclass
class Cancel(Command):
    customer_name: str
    holiday: str
    
    def process(self):
        return cancel_schedule(self.customer_name, self.holiday)
    