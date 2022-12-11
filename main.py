import sys

from commands.schedule import Schedule
from commands.signup import SignUp
from commands.cancel import Cancel
from commands.dropout import DropOut
from commands.status import Status
from utils.inputer import inputer
from utils.status_inputer import status_inputer
from utils.logging import logger

def main():
    command = "Please input any of the following commands. \n"
    command += "1. Schedule\n"
    command += "2. Cancel\n"
    command += "3. Status\n"
    command += "4. SignUp\n"
    command += "5. DropOut\n"
    
    print(command)
    user_input = input()
    
    if user_input == '1':
        user = inputer()
        Schedule(user[0], user[1]).process()
        
    elif user_input == '2':
        user = inputer()
        Cancel(user[0], user[1]).process()
        
    elif user_input == '3':
        status_input = status_inputer()
        if status_input[0] == "holiday":
            Status(holiday=status_input[1]).process()
        elif status_input[0] == "twister":
            Status(balloon_twister=status_input[1]).process()
        
    elif user_input == '4':
        user_name = input("input your username name:")
        SignUp(user_name).process()
        
    elif user_input == "5":
        user_name = input("input your username name:")
        DropOut(user_name).process()
        
    else:
        logger.error("Invalid input.")
        sys.exit(1)
        
if __name__ == '__main__':
    main()
