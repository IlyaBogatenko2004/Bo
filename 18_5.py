#Задача E
from requests import get
from sys import stdin

address = 'http://' + input()
ways = [i.strip() for i in stdin]
summ = 0
for way in ways:
    summ += sum(get(address + way).json())
print(summ)