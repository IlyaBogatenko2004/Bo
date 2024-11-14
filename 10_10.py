#Задача J
def merge(a, b):
    c = list(a) + list(b)
    n = len(c)
    for i in range(n):
        for j in range(0, n - i - 1):
            if c[j] > c[j + 1]:
                c[j], c[j + 1] = c[j + 1], c[j]
    return tuple(c)