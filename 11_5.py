#Задача E
def to_string(*args, **kwargs):
    return kwargs.get("sep", " ").join([str(i) for i in args]) + kwargs.get("end", "\n")