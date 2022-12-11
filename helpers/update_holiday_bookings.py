from dataclasses import dataclass
import json

from utils.get_holiday_bookings import get_holiday_bookings
from utils.get_base_dir import BASE_DIR

@dataclass
class HolidayBookings:
    holiday: str
    customer_name: str
    balloon_twister: str
    
    def update(self):
        data = {"customer_name": f"{self.customer_name}", "balloon_twister": f"{self.balloon_twister}"}
        holiday_bookings = get_holiday_bookings()
        if self.holiday in holiday_bookings.keys():
            holiday_bookings[self.holiday].append(data)
        else:
            holiday_bookings[self.holiday] = [data,]
        
        json_data = json.dumps(holiday_bookings, indent=4, sort_keys=True)
        
        with open(f"{BASE_DIR}/extras/holiday_bookings.json", "w") as f:
            f.write(json_data)
