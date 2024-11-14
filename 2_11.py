#задача K
s = str(int(input()))
s1 = int(s[0])
s2 = int(s[1])
s3 = int(s[2])
ma = max(s1, s2, s3)
mi = min(s1, s2, s3)
m2 = s1 + s2 + s3 - ma - mi
if ma + mi == m2 * 2:
    print('YES')
else:
    print('NO')
