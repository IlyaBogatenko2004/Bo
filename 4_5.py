#Задача E
s = int(input())
y = 0
for i in range(s):
    flag = 0
    while True:
        k = input()
        if k == "ВСЁ":
            break
        else:
            if k == "зайка":
                flag = 1
    if flag == 1:
        y += 1
print(y)        