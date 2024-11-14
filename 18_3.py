#Задача C
from requests import get
address = 'http://' + input()
data = get(address).json()
print(sum(i for i in data if isinstance(i, int)))