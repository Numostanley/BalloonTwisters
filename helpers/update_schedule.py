import json
from dataclasses import dataclass

from utils.get_base_dir import BASE_DIR

@dataclass
class UpdateSchedule:
    schedules: dict
    
    def update(self):
        json_data = json.dumps(self.schedules, indent=4, sort_keys=True)
        with open(f"{BASE_DIR}/extras/schedule.json", "w") as f:
            f.write(json_data)
        print("Schedule update was successful.")
        