#Задача C
from sys import stdin

for i in stdin.readlines():
    if not i.startswith('#'):
        print(i[:i.find('#')])