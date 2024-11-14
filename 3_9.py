# задача I
s = int(input())
k = 1
if s == 0:
    print(1)
else:
    for i in range(1, s + 1):
        k = k * i
print(k)  

