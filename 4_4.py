#Задача D
t = 0
k = int(input())
for s in range(k):
    a = int(input())
    for i in range(len(str(a))):
        t += int(str(a)[i])
print(t)  