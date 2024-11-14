#Задача D
from requests import get

address = 'http://' + input()
key = input()
data = get(address).json()
print(data.get(key, 'No data'))