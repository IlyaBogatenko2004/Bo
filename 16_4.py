#Задача D
import math as m

numbers = list(map(float, input().split()))
print(m.pow(m.prod(numbers), 1 / len(numbers)))