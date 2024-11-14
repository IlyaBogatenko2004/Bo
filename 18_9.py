#Задача I
from requests import put
from json import dumps
from sys import stdin

address = 'http://' + input() + '/users/' + input()
line = [i.strip().split('=') for i in stdin]
data = {}
for j in line:
    data[j[0]] = j[1]
put(address, data=dumps(data))