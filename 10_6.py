#Задача F
lst = []


def modern_print(string):
    print(string) if string not in lst else None
    lst.append(string)