#Задача G
from requests import get
from sys import stdin

address = 'http://' + input() + '/users/' + input()
d = ''.join(i for i in stdin)
data = {}
try:
    data = get(address).json()
except ValueError:
    print('Пользователь не найден')
if data:
    for key in data:
        d = d.replace('{' + key + '}', str(data[key]))
    print(d)  