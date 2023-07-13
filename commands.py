from collections import defaultdict,namedtuple

#TODO вибрать способ записи данних
User = namedtuple("User",['name','phone'])
users = list()


def hello(*_):
    print("How can I help you?")

def add_name_phone(name, phone) :
    # TODO санитайзер номера??? проверка коректности!
    user = User(name, phone)
       
    
def change_phone(name, phone):
    pass
    

BOT_COMMANDS = {
    "hello": hello,
    "add": add_name_phone,
    "change": change_phone,
}

BOT_EXIT = ["good bye", "close", "exit"]