import json

from utils.get_base_dir import BASE_DIR


def get_waiting_list():
    with open(f"{BASE_DIR}/extras/waiting_list.json", "r") as f:
        waiting_list = json.loads(f.read())
    return waiting_list
