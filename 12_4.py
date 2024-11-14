#Задача D
def answer(func):
    def wrap(*args, **kwargs):
        return f'Результат функции: {func(*args, **kwargs)}'
    return wrap