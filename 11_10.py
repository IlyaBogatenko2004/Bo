#Задача J
def secret_replace(text, **kwargs):
    result = ''
    kwargs = {d: (v, 0) for d, v in kwargs.items()}
    for i in text:
        if i in kwargs:
            result += kwargs[i][0][kwargs[i][1] % len(kwargs[i][0])]
            kwargs[i] = kwargs[i][0], kwargs[i][1] + 1
        else:
            result += i
    return result