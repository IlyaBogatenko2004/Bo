#Задача D
a, b = int(input()), int(input())
semolina, oatmeal = set(), set()
for _ in range(a):
    semolina.add(input())
for _ in range(b):
    oatmeal.add(input())
both = len(semolina & oatmeal)
print(both if both else 'Таких нет')