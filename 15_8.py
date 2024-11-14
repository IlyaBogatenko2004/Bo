#Задача H
class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


def username_validation(username):
    if not isinstance(username, str):
        raise TypeError
    if sum((i.lower() not in '0123456789_abcdefghijklmnopqrstuvwxyz') for i in username):
        raise BadCharacterError
    if username[0].isdigit():
        raise StartsWithDigitError
    return username