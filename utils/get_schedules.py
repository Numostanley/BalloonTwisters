import json

from utils.get_base_dir import BASE_DIR

def get_schedules() -> dict:
    with open(f"{BASE_DIR}/extras/schedule.json", "r") as f:
        schedules = json.loads(f.read())
    return schedules
