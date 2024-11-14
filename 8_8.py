#Задача H
cereals = []
for _ in range(int(input())):
    cereals.append(input())
amount = int(input())
cereals *= amount // len(cereals) + 1
for i in range(amount):
    print(cereals[i])