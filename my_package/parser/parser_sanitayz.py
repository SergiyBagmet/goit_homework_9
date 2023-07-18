import re
from my_package import BOT_COMMANDS, BOT_EXIT
def parser(user_input: str) -> list:
    """
    парсинг строки 
    все внутренние пробели меняем на один пробел
    если команда из двух слов "совмещаем" в 0 елемент списка
    только команда list[0] в ловеркейс, возврат списком
    """
    user_input = re.sub(r'\s+',' ',user_input) # оставляем только по 1 пробелу 
    user_input = user_input.strip() # избавляемся от крайних пробелов пробелов
    user_list = user_input.split(" ") # формируем список для распаковки

    #TODO может есть способ по лучше? 
    #  формируем список двойних команд(два слова и больше) (можно било и вручную но)
    command_list = list(BOT_COMMANDS.keys())
    command_list.extend(BOT_EXIT)
    two_words_list = [s for s in command_list if " " in s]

    for words in two_words_list:
        if user_input.lower().startswith(words):
            i = words.count(" ") + 1
            user_list = [words] + user_list[i:]

    # єто был костиль который я заменил костилем выше

    # if "good"==user_list[0].lower() and "bye"==user_list[1].lower():
    #     command = f"{user_list[0]} {user_list[1]}"
    #     return [command.lower()] # специальний ретурн для команди "good bye"
    
    # if "show"==user_list[0].lower() and "all"==user_list[1].lower():
    #     command = f"{user_list[0]} {user_list[1]}"
    #     return [command.lower()] + [user_list[2:]] 

    command = user_list.pop(0)
    user_list.insert(0,command.lower()) #только команду в нижний регистр 
    return user_list


