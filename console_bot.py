
def hello(*_):
    print("How can I help you?")

def add_name_phone(data: list) :
    print(f"name : {data[0]}\nphone : {data[1]}" )

BOT_COMMANDS = {
    "hello": hello,
    "add": add_name_phone,
}

BOT_EXIT = ["good bye", "close", "exit"]

def parser(user_input: str) -> list:
    user_input = user_input.lower().strip()
    return user_input.split(" ")

def main():
    while True:
        user_input = input("Enter command: ")
        command, *data = parser(user_input)
        
        if command in BOT_EXIT:
            print("Good bye!")
            break

        do_command = BOT_COMMANDS[command]
        do_command(data)

if __name__ == '__main__':
    main()