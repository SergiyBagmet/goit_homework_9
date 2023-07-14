from commands import BOT_COMMANDS, BOT_EXIT
from parser_sanitayz import *


def main(): 
    while True:
        user_input = input("Enter command: ")
        command, *user_info = parser(user_input)

        if command in BOT_EXIT:
            print("Good bye!")
            break
        try:    
            do_command = BOT_COMMANDS[command]
            bot_message = do_command(*user_info)
        except KeyError:
            bot_message = "Unknown command !!!"

        print(bot_message+"\n")   
        
  


if __name__ == '__main__':
   main()