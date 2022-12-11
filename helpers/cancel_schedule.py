from utils.get_schedules import get_schedules
from .update_schedule import UpdateSchedule

def cancel_schedule(customer_name: str, holiday: str):
    schedules = get_schedules()
    
    for count, item in enumerate(schedules.items()):
        for i in item[1]:
            if i["customer_name"] == customer_name and i["holiday"] == holiday:
                twister = list(schedules.keys())[count]
                print("Found" + f"{schedules[twister][item[1].index(i)]}")
                del schedules[twister][item[1].index(i)]
                UpdateSchedule(schedules).update()
                print("Schedule Cancelled.")
    