import sys

from utils.get_holidays import get_holidays
from utils.logging import logger
from utils.get_base_dir import BASE_DIR

def status_inputer():
    inputs = "Select method to check status.\n"
    inputs += "1. By Holiday name.\n"
    inputs += "2. By Balloon twister name.\n"
    
    print(inputs)
    user_input = input()
    
    if user_input == "1":
        holidays = get_holidays()
        select_holiday = "Please select holiday. \n"
        for key, value in holidays.items():
            select_holiday += f"{key}. {value}\n"    
        print(select_holiday)
        try:
            holiday = holidays[int(input("Select holiday:"))]
            return ["holiday", holiday]
        except KeyError as e:
            logger.error(f"Invalid Input {e}. Please enter the correct number.")
            sys.exit(1)
        except ValueError as e:
            logger.error(f"Invalid Input {e}. Please enter the correct number.")
            sys.exit(1)
            
    elif user_input == "2":
        with open(f"{BASE_DIR}/extras/balloon_twisters.dat", "r") as f:
            balloon_twisters = f.readlines()
            twisters = []
            for line in balloon_twisters:
                twister = line.split("\n")[0]
                twisters.append(twister)
                
            select_twister = "Please select a balloon twister. \n"
            for twister in twisters:
                select_twister += f"{twisters.index(twister)}. {twister}\n"    
            print(select_twister)
            try:
                inputed_twister = twisters[int(input("Select holiday:"))]
                return ["twister", inputed_twister]
            except IndexError as e:
                logger.error(f"Invalid Input {e}. Please enter the correct number.")
                sys.exit(1)
            except ValueError as e:
                logger.error(f"Invalid Input {e}. Please enter the correct number.")
                sys.exit(1)
    else:
        logger.error("Invalid input.")
        sys.exit(1)
