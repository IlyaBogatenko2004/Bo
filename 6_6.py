#Задача F
a, b = int(input()), int(input())
porridges = []
for _ in range(a + b):
    if (x := input()) not in porridges:
        porridges.append(x)
    else:
        porridges.remove(x)
if len(porridges):
    for kid in sorted(porridges):
        print(kid)
else:
    print('Таких нет')