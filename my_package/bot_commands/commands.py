from functools import wraps
import re
phone_book = {} # TODO где его правильно било бы обьявить?

def input_error(func):
    @wraps(func) #для тру доки/имени
    def wrapper(*args):
        """
        декоратор ловит ошибки функций 
        недостаток аргументов и созданние ошибки
        затем возвращает на принт 
        """
        try:
            return func(*args)
        except KeyError as err: # сделал по условию но он падает написал сам)
            return str(err)
        except (ValueError,TypeError) :
            return f"for this command should be more data"
    return wrapper    


def valid_phone(func): 
    @wraps(func)
    def wraper(*args):
        """
        декоратора возвращает валидний очищений номер
        или False
        """
        try: #TODO как тут обработать через @input_error
            name, phone, *_ = args 
        except (ValueError ,TypeError): 
            return f"for this command should be more data"      
          
        digits = "".join(filter(str.isdigit, phone)) # тільки цифри тут може бути нормальна регулярка))
        valid = re.search(r'380\d{9,}|80\d{9,}|0\d{9,}',digits)
        if valid :
            return func(name, digits,*_)
        else:
            return f"'{phone}' -  isn't corect nomber"
    return wraper  

# не вижу смысла вешать @input_error
# хотя если убрать *_ тогда декоратор поможет) наврное)
def hello(*_) -> str:
    """
    need only command 
    """
    bot_message = "How can I help you?"
    return bot_message

def help_info(*_):
    """
    need only command
    print all bot's commands
    """
    bot_message = "\n"
    for key,func in BOT_COMMANDS.items() : # я думаю доки для этого не пишут) а тут вайнот
        line = f"command [{key}] -template-> {str(func.__doc__).strip()}\n\n"
        bot_message += line
    bot_message += f"for exit write -any-of-these-> {str(BOT_EXIT)[1:-1]}"    
    return bot_message    

@valid_phone
@input_error
def add_name_phone(name: str, phone: str, *_) -> str :
    """
    add name 380123456789
    creates a new contact in the phone book 
    """
    if (name not in phone_book.keys()) and (phone not in phone_book.values()): # если нет такого имени - запись
        phone_book[name] = phone 
        return f"Contact '{name}' with phone '{phone}' has been added."
    
    elif phone in phone_book.values(): # если номер уже есть 
        raise KeyError ( f"this nomber {phone} already in the phone book")
    else: # если имя уже есть 
        raise KeyError( f"this name '{name}' is already in the phone book")
   
@valid_phone       
@input_error    
def change_phone(name: str, new_phone: str, *_) -> str:
    """
    change name 380123456789 
    change existing contact in the phone book
    """
    back_phone = phone_book.get(name) # получаем номер
    if back_phone and (new_phone not in phone_book.values()): # если получили и такого номера нет - меняем
        phone_book[name] = new_phone
        return  f"successful changed contact : '{name}' {back_phone} -to-> {new_phone}"
    
    elif new_phone in phone_book.values(): # если номер уже есть 
        raise KeyError ( f"this nomber {new_phone} already in the phone book")
    else:
        raise KeyError(f"this contact : '{name}' -  isn't in phone book")    

@input_error   
def get_phone(name: str, *_) ->str :
    """
    phone name
    print phone nomber existing contact
    """
    phone = phone_book.get(name) # получаем номер по иени
    if phone:
        return f"The phone number for contact '{name}' is  {phone}."
    else:
        raise KeyError(f"this contact : '{name}' -  isn't in phone book")
     
@input_error
def show_contacts(*_) -> str :
    """
    need only command 
    print all phone nombers existing contacts
    """
    if phone_book: # если телефонная книга не пустая возвращаем на принт
        contacts = "Contacts:\n\n"
        contacts += "{:^15} {:^15}\n".format("name","phone")
        for name, phone in sorted(phone_book.items()):# TODO как отсортировать по алфавиту без учета регистра но при єтом сохранить словарь и принти
            contacts += "{:<15} {:<15}\n".format(name, phone)
        return contacts
    else:
        raise KeyError ("No contacts found.")
@input_error
def del_contact(name, *_) -> str :
    """
    del name
    delete existing contact from phone book
    """
    phone = phone_book.get(name) # если есть имя - удаляем
    if phone:
        phone_book.pop(name)
        return f"The contact '{name}' - {phone} has been deleted"
    else:
        raise KeyError(f"this contact : '{name}' -  isn't in phone book")
    

BOT_COMMANDS = {
    "hello": hello,
    "help" : help_info,
    "add": add_name_phone,
    "change": change_phone,
    "phone": get_phone,
    "show all": show_contacts,
    "del" : del_contact,
}

BOT_EXIT = ["good bye", "close", "exit"]