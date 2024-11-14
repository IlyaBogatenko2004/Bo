#Задача M
from itertools import permutations

items = []
for _ in range(int(input())):
    items.append(input())
for i in sorted(permutations(items)):
    print(', '.join(i))