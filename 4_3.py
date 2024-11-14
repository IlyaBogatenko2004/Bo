#Задача C
n = int(input())
s = 1
for i in range(1, n + 1):
    for j in range(i):
        if s <= n:
            print(s, end=' ')
            s += 1
    print()  



