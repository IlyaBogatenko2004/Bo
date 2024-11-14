#Задача D
from sys import stdin

for line in (x := [i.strip() for i in stdin])[:-1]:
    if x[-1].lower() in line.lower():
        print(line)