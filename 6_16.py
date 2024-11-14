#Задача P
near = set()
while x := input().split():
    for ind, i in enumerate(x):
        if i == 'зайка' and ind not in (0, len(x) - 1):
            near.add(x[ind - 1])
            near.add(x[ind + 1])
        elif i == 'зайка' and not ind:
            near.add(x[ind + 1])
        elif i == 'зайка' and ind == len(x) - 1:
            near.add(x[ind - 1])
for item in near:
    print(item)