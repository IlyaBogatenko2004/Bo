#Задача I
d = {}
while x := input().split():
    for i in x:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
for j in d:
    print(j, d[j])