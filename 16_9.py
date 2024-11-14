#Задача I
import numpy as np


def rotate(matrix, angle):
    return np.rot90(matrix, (360 - angle) // 90)