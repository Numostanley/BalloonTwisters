from dataclasses import dataclass
import json

from utils.get_base_dir import BASE_DIR
from utils.get_waiting_list import get_waiting_list

@dataclass
class UpdateWaitingList:
    booking: dict
    
    def add_to_top(self):
        waiting_list = get_waiting_list()
        waiting_list["waiting_list"].insert(0, self.booking)
        json_data = json.dumps(waiting_list, indent=4, sort_keys=True)
        with open(f"{BASE_DIR}/extras/waiting_list.json", "w") as f:
            f.write(json_data)
        print("Booking added to top of waiting list.")    
    
    def add_to_end(self):
        waiting_list = get_waiting_list()
        waiting_list["waiting_list"].append(self.booking)
        json_data = json.dumps(waiting_list, indent=4, sort_keys=True)
        with open(f"{BASE_DIR}/extras/waiting_list.json", "w") as f:
            f.write(json_data)
        print("Booking added to end of waiting list.")
        