#Задача G
import numpy as np


def make_board(num):
    matrix = np.indices((num, num)).sum(axis=0) % 2
    return np.array(np.rot90(matrix), dtype='int8')