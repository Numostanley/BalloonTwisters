from dataclasses import dataclass

from helpers.book_balloon_twister import BookTwister
from utils.get_schedules import get_schedules
from utils.get_unbooked_twisters import get_unbooked_twisters

@dataclass
class Reschedule:
    unscheduled_bookings: list
    new_booking: bool = False
    
    def update(self) -> None:
        schedules = get_schedules()
        unbooked_twisters = get_unbooked_twisters(schedules)
        for data in self.unscheduled_bookings:
            BookTwister(unbooked_twisters, schedules, data, self.new_booking).book()
