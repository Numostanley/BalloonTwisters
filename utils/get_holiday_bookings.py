import json

from utils.get_base_dir import BASE_DIR

def get_holiday_bookings() -> dict:
    with open(f"{BASE_DIR}/extras/holiday_bookings.json", "r") as f:
        holiday_bookings = json.loads(f.read())
    return holiday_bookings
