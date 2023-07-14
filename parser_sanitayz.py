import re
def parser(user_input: str) -> list:
    """
    
    """
    user_input = re.sub(r'\s+',' ',user_input) # оставляем только по 1 пробелу 
    user_input = user_input.strip() # избавляемся от крайних пробелов пробелов
    user_list = user_input.split(" ") # формируем список для распаковки

    if "good"==user_list[0].lower() and "bye"==user_list[1].lower():
        command = f"{user_list[0]} {user_list[1]}"
        return [command.lower()] # специальний ретурн для команди "good bye"

    command = user_list.pop(0)
    user_list.insert(0,command.lower()) #только команду в нижний регистр 
    return user_list

def sanitaze_phone(phone: str) -> str :
    """
    очишает строку с номером телефона оставляя только цифри
    """
    digits = re.sub(r'\D', '', phone)
    return digits

def is_valid_phone(phone: str) -> bool :
    """
    проверка валидности номера
    только цифри длина 
    """
    pass
