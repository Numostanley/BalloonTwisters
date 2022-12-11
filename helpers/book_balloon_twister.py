from collections import deque
from dataclasses import dataclass

from utils.logging import logger
from helpers.update_schedule import UpdateSchedule
from helpers.update_waiting_list import UpdateWaitingList
from helpers.update_holiday_bookings import HolidayBookings


@dataclass
class BookTwister:
    unbooked_twisters: deque
    schedules: dict
    data: dict
    new_booking: bool = True
    
    def book(self):
        all_twisters = set(self.schedules.keys())
        unavailable_twisters = set()

        if self.unbooked_twisters:
            twister = self.unbooked_twisters.popleft()
            self.schedules[twister] = [self.data,]
            UpdateSchedule(self.schedules).update()
            HolidayBookings(self.data["holiday"], self.data["customer_name"], twister).update()
            print(f"Schedule: balloon_twister: {twister}, {self.data}")
        else:
            for count, item in enumerate(self.schedules.items()):
                for i in item[1]:
                    if self.data["holiday"] in i["holiday"]:
                        twister1 = list(self.schedules.keys())[count]
                        unavailable_twisters.add(twister1)
        
            available_twisters = all_twisters.difference(unavailable_twisters)
            if available_twisters:
                twister = available_twisters.pop()
                self.schedules[twister].append(self.data)
                
                UpdateSchedule(self.schedules).update()
                HolidayBookings(self.data["holiday"], self.data["customer_name"], twister).update()
                print(f"Schedule: balloon_twister: {twister}, {self.data}")
            else:
                logger.info("No available balloon twister")
                if self.new_booking:
                    UpdateWaitingList(self.data).add_to_end()
                else:
                    UpdateWaitingList(self.data).add_to_top()
