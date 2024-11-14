#Задача G
def same_type(func):
    def wrapper(*args):
        if len({type(i) for i in args}) != 1:
            print("Обнаружены различные типы данных")
            return False
        return func(*args)
    return wrapper