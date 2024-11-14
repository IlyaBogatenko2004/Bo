#Задача G
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