#Задача E
a, b = int(input()), int(input())
porridges = []
for _ in range(a + b):
    porridges.append(input())
both = len([i for i in porridges if porridges.count(i) == 1])
print(both if both else 'Таких нет')