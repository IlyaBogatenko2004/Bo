#Задача B
from sys import stdin

print(round(sum(x := [int(i.split()[2]) - int(i.split()[1]) for i in stdin.readlines()]) / len(x)))