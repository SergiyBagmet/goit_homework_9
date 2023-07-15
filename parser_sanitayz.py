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
    
    # TODO test after decorater all commands func
    if "show"==user_list[0].lower() and "all"==user_list[1].lower():
        command = f"{user_list[0]} {user_list[1]}"
        return [command.lower()] + [user_list[2:]] 


    command = user_list.pop(0)
    user_list.insert(0,command.lower()) #только команду в нижний регистр 
    return user_list


def valid_phone(func):
    """
    декоратора возвращает ваолидний очищений номер
    или False
    """
    def wraper(*args):
        try:
            name, phone, *_ = args 
        except (ValueError ,TypeError):
            return f"for this command should be more data"        
        digits = "".join(filter(str.isdigit, phone))
        if len(digits) > 10 :
            return func(name, digits,*_)
        else:
            return f"'{phone}' -  this isn't corect nomber"
    return wraper  
