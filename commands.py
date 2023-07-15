from parser_sanitayz import valid_phone
phone_book = {}

def input_error(func):
    """
    декоратор ловит ошибки функций 
    недостаток аргументов и созданние ошибки
    затем возвращает на принт 
    """
    def wrapper(*args):
        try:
            return func(*args)
        except KeyError as err:
            return str(err)
        except (ValueError,TypeError) :
            return f"for this command should be more data"
    return wrapper    

# не вижу смысла вешать @input_error
def hello(*_) -> str:
    """
    при визове(команда "hello") 
    возвращает фиксированую строку
    """
    bot_message = "How can I help you?"
    return bot_message

@valid_phone
@input_error
def add_name_phone(name: str, phone: str, *_) -> str :
    """
    заполняет телефоную книгу (словарь) 
    {"name" : "phone",}
    возвращает строку о работе функции 
    """
    if name not in phone_book.keys(): # если нет такого имени - запись
        phone_book[name] = phone
        return f"Contact '{name}' with phone '{phone}' has been added."
    
    else: # если имя уже есть  -  сообщение 
        raise KeyError( f"this name '{name}' is also in phone book \
if you whant change namber, writhe : 'change name new_phone'")
   
@valid_phone       
@input_error    
def change_phone(name: str, new_phone: str, *_) -> str:
    """
    меняем номер телефона по имени
    возвращаем строку о работе функции
    """
    back_phone = phone_book.get(name)
    if back_phone:
        phone_book[name] = new_phone
        return  f"successful changed contact : '{name}' {back_phone} -to-> {new_phone}"
    else:
        raise KeyError(f"this contact : '{name}' -  isn't in phone book")    

@input_error   
def get_phone(name: str, *_) ->str :
    """
    получаем номер по имени и возвращаем строку
    если нет записи ерор ловит декоратор 
    """
    phone = phone_book.get(name)
    if phone:
        return f"The phone number for contact '{name}' is  {phone}."
    else:
        raise KeyError(f"this contact : '{name}' -  isn't in phone book")
     
@input_error
def show_contacts(*_) -> str :
    """
    
    """
    if phone_book:
        contacts = "Contacts:\n\n"
        contacts += "{:^15} {:^15}\n".format("name","phone")
        for name, phone in sorted(phone_book.items()):
            contacts += "{:<15} {:<15}\n".format(name, phone)
        return contacts
    else:
        raise KeyError ("No contacts found.")

BOT_COMMANDS = {
    "hello": hello,
    #TODO "help" : all_commands,
    "add": add_name_phone,
    "change": change_phone,
    "phone": get_phone,
    "show all": show_contacts,
}

BOT_EXIT = ["good bye", "close", "exit"]