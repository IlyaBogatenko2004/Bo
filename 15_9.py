#Задача I
class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


def name_validation(name):
    if not isinstance(name, str):
        raise TypeError
    if sum(i.lower() not in 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя' for i in name):
        raise CyrillicError
    if name != name.lower().capitalize():
        raise CapitalError
    return name


def username_validation(username):
    if not isinstance(username, str):
        raise TypeError
    if sum((i.lower() not in '0123456789_abcdefghijklmnopqrstuvwxyz') for i in username):
        raise BadCharacterError
    if username[0].isdigit():
        raise StartsWithDigitError
    return username


def user_validation(**kwargs):
    if [i for i in kwargs] != ['last_name', 'first_name', 'username'] or len(kwargs) != 3:
        raise KeyError
    if any(not isinstance(k, str) for k in kwargs.values()):
        raise TypeError
    kwargs['last_name'] = name_validation(kwargs['last_name'])
    kwargs['first_name'] = name_validation(kwargs['first_name'])
    kwargs['username'] = username_validation(kwargs['username'])
    return kwargs