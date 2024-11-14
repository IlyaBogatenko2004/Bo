#задача J
s = str(int(input()))
s1 = int(s[0])
s2 = int(s[1])
s3 = int(s[2])
q = s2 + s3
w = s1 + s2
e = str(max(q, w)) + str(min(q, w))
print(e)