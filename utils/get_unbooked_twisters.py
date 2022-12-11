from collections import deque

from utils.get_base_dir import BASE_DIR

def get_unbooked_twisters(schedules: dict):
    unbooked_twisters = deque()
    with open(f"{BASE_DIR}/extras/balloon_twisters.dat", "r") as f:
        balloon_twisters = f.readlines()
        for line in balloon_twisters:
            twister = line.split("\n")[0]
            if twister not in schedules.keys():
                unbooked_twisters.append(twister)
    return unbooked_twisters
