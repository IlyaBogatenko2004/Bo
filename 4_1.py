#Задача A
s = int(input())
for i in range(1, s + 1):
    j = ''
    for k in range(1, s + 1):
        j = j + str(i * k) + ' '
    print(j) 