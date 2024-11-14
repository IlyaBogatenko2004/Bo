#Задача A
import math as m

x = float(input())
a = m.log(m.pow(x, 3 / 16), 32)
b = m.pow(x, m.cos((m.pi * x) / (2 * m.e)))
c = m.pow(m.sin(x / m.pi), 2)
print(a + b - c)   