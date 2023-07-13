def hello(*_):
    print("How can I help you?")

def add_name_phone(name, phone) :
    
    print(f"name : {name}\nphone : {phone}" )

BOT_COMMANDS = {
    "hello": hello,
    "add": add_name_phone,
}

BOT_EXIT = ["good bye", "close", "exit"]