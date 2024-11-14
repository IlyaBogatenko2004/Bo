#Задача G
numbers = tuple()


def enter_results(*args):
    global numbers
    numbers += args


def get_sum():
    return round(sum(numbers[::2]), 2), round(sum(numbers[1::2]), 2)


def get_average():
    return round(2 * get_sum()[0] / len(numbers), 2), round(2 * get_sum()[1] / len(numbers), 2)