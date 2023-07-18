from my_package import BOT_COMMANDS, BOT_EXIT, parser

def main(): 
    while True:
        user_input = input(">>>")
        command, *user_info = parser(user_input) #  команда + запаковка ост строка(списком) если она есть 

        if command in BOT_EXIT: # условие на виход TODO а можно било написать отдельной функцией?
            print("Good bye!")
            break
           
        do_command = BOT_COMMANDS.get(command) # получем функию по команде
        if do_command:
            bot_message = do_command(*user_info) # передаем запаковний список инпута если он есть 
        else:
            bot_message = "Unknown command!!! write 'help' to get info commands"

        print(bot_message+"\n")   
        
  


if __name__ == '__main__':
   main()