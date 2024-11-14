#задача O
p = str(int(input()))
k = str(int(input()))
q = int(p[0])
w = int(p[1])
e = int(k[0])
r = int(k[1])
a = max(q, w, e, r)
s = min(q, w, e, r)
d = (q + w + e + r - a - s) % 10
print(int(f'{a}{d}{s}'))
