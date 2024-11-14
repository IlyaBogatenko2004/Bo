#Задача H
import numpy as np


def snake(m, n, direction='H'):
    matrix = np.zeros((n, m), dtype=np.int16)
    num = 1
    if direction == 'H':
        for i in range(n):
            if not i % 2:
                matrix[i] = np.arange(num, num + m)
            else:
                matrix[i] = np.arange(num + m - 1, num - 1, -1)
            num += m
    else:
        for j in range(m):
            if not j % 2:
                matrix[:, j] = np.arange(num, num + n)
            else:
                matrix[:, j] = np.arange(num + n - 1, num - 1, -1)
            num += n
    return matrix