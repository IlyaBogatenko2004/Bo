#Задача C
objects = []
for _ in range(int(input())):
    objects.extend(input().split())
print('\n'.join(set(objects)))