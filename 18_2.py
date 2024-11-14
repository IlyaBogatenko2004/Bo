#Задача B
from requests import get

address = 'http://' + input()
summ = 0
while data := int(get(address).text):
    summ += data
print(summ)