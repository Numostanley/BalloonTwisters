from utils.get_schedules import get_schedules


def get_twister_schedule(balloon_twister: str) -> list:
    schedules = get_schedules()
    twister_schedule = schedules[balloon_twister]
    return twister_schedule
    