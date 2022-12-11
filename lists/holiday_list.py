from utils.get_holiday_bookings import get_holiday_bookings
from utils.logging import logger

class Holiday:
    def __init__(self, holiday_name) -> None:
        self.holiday_name = holiday_name
        self.bookings: list[dict] = []
        
    def get_list(self) -> list:
        holiday_list = get_holiday_bookings()
        try:
            self.bookings = holiday_list[self.holiday_name]
        except KeyError as e:
            logger.info("Sorry there's no booking for this holiday.")
        
        return self.bookings
    