#Задача J
def make_linear(arr):
    new_arr = []
    for i in arr:
        if isinstance(i, list):
            new_arr.extend(make_linear(i))
        else:
            new_arr.append(i)
    return new_arr