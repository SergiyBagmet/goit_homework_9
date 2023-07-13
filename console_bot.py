
from commands import *
from parser_sanitayz import *

def main():
    while True:
        user_input = input("Enter command: ")
        command, *user_info = parser(user_input)
        
        if command in BOT_EXIT:
            print("Good bye!")
            break

        do_command = BOT_COMMANDS[command]
        do_command(*user_info)

if __name__ == '__main__':
    main()