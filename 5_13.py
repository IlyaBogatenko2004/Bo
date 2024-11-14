#Задача M
data = []
for _ in range(int(input())):
    data.append(int(input()))
number = int(input())
for i in data:
    print(i ** number)