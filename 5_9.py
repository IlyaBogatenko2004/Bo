#Задача I
while (n := input()):
    if not n.startswith('#'):
        print(n[:(n.index('#') if '#' in n else len(n))])