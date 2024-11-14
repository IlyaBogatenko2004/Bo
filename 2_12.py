#задача L
q = int(input())
w = int(input())
e = int(input())
if q < w + e and w < q + e and e < w + q:
    print('YES')
else:
    print('NO')
