#Задача C
dl = int(input())
kol = int(input())
for i in range(kol):
    ans = input()
    if len(ans) <= dl:
        print(ans)
    else:
        print(ans[0:dl-3] + "...")