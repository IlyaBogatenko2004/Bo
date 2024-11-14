#Задача N
data = list(map(int, input().split()))
number = int(input())
for i in data:
    print(i ** number, end=' ')