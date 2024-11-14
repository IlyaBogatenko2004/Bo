#Задача B
def recursive_digit_sum(n):
    return n % 10 + recursive_digit_sum(n // 10) if n else 0