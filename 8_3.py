#Задача C
from itertools import count

a, b, step = list(map(float, input().split()))
for value in count(a, step):
    if value <= b:
        print(f'{value:.2f}')
    else:
        break