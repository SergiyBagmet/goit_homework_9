
phone_book = {}

def hello(*_) -> str:
    """
    при визове(команда "hello") 
    возвращает фиксированую строку
    """
    bot_message = "How can I help you?"
    return bot_message

def add_name_phone(name: str, phone: str, *_) -> str :
    """
    заполняет телефоную книгу (словарь) 
    {"name" : "phone",}
    возвращает строку о работе функции 
    """
    if name not in phone_book.keys(): # если нет такого имени - запись
        phone_book[name] = phone
        bot_message = f"added entry to the phone book :\t{name} - {phone}"
    else: # если имя уже есть  -  сообщение 
        bot_message = f"this name '{name}' is also in phone book\n\
if you whant change namber, writhe : 'change name new_phone'"
    return bot_message
       
    
def change_phone(name: str, new_phone: str, *_) -> str:
    """
    меняем номер телефона по имени
    возвращаем строку о работе функции
    """
    if name in phone_book.keys():
        back_phone = phone_book.get(name)
        phone_book[name] = new_phone
        bot_message = f"successful changed contact : '{name}' \n\
{back_phone} -to-> {new_phone}"
    else:
        bot_message = f"this contact : '{name}' -  isn't in phone book"    
    return bot_message

BOT_COMMANDS = {
    "hello": hello,
    "add": add_name_phone,
    "change": change_phone,
}

BOT_EXIT = ["good bye", "close", "exit"]