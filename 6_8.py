#Задача H
a, kids = int(input()), []
for _ in range(a):
    kids.extend([input().split()])
kids.sort()
key, counter = input(), 0
for kid in kids:
    if key in kid[1:]:
        print(kid[0])
        counter += 1
if not counter:
    print('Таких нет')