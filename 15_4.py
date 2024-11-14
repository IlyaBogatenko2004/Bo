#Задача D
def only_positive_even_sum(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError
    if not (a > 0 and not a % 2) or not (b > 0 and not b % 2):
        raise ValueError
    return a + b