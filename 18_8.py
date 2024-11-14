#Задача H
from requests import post
from json import dumps

address = 'http://' + input() + '/users'
data = {}
data["username"] = input()
data["last_name"] = input()
data["first_name"] = input()
data["email"] = input()
post(address, data=dumps(data))