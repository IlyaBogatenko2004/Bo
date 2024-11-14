#Задача E
def result_accumulator(func):
    result = []

    def wrap(*args, method="accumulate"):
        result.append(func(*args))
        if method == "drop":
            temp = result.copy()
            result.clear()
            return temp
    return wrap