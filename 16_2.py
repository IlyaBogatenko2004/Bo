#Задача B
from math import gcd
from sys import stdin

for i in stdin:
    print(gcd(*map(int, i.split())))