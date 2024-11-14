#Задача A
try:
    func()
except Exception as error:
    print(type(error).__name__)
else:
    print('No Exceptions')   