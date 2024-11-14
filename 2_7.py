#задача G
n = str(int(input()))
q = n[0:2]
e = n[2:4]
e = e[::-1]
if q == e:
    print('YES')
else:
    print('NO')