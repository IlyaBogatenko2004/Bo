#Задача I
from itertools import product

for i in (n := range(1, int(input()) + 1)):
    print(' '.join(map(lambda x: str(x[0] * x[1]), product(n, [i]))))