import sys

from utils.get_holidays import get_holidays
from utils.logging import logger

def inputer():
    holidays = get_holidays()
    select_holiday = "Please select holiday. \n"
    customer_name = input("input customer name:")
    for key, value in holidays.items():
        select_holiday += f"{key}. {value}\n"    
    print(select_holiday)
    try:
        holiday = holidays[int(input("Select holiday:"))]
    except KeyError as e:
        logger.error(f"Invalid Input {e}. Please enter the correct number.")
        sys.exit(1)
    except ValueError as e:
        logger.error(f"Invalid Input {e}. Please enter the correct number.")
        sys.exit(1)
        
    return [customer_name, holiday]
