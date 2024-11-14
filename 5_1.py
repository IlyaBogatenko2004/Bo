#Задача A
p = []
k = int(input())
for i in range(k):
    s = str(input())
    p += [s[0]]  
q = 0 
print(p)
for i in range(k):
    if p[i] == "а" or p[i] == "б" or p[i] == "в":
        q += 1
    else:
        q += 0
print(k, q)
if k == q:
    print("YES")
else:
    print('NO')           

