def parser(user_input: str) -> list:
    user_input = user_input.lower().strip()
    return user_input.split(" ")
