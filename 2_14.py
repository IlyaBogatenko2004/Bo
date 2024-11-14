#задача N
p = int(input())
q = str(p)
w = int(q[0] + q[1])
e = int(q[0] + q[2])
r = int(q[1] + q[2])
t = int(q[1] + q[0])
y = int(q[2] + q[1])
u = int(q[2] + q[0])
a = min(w, e, r, t, y, u)
s = max(w, e, r, t, y, u)
if a < 10 and a != 0:
    print(int(f'{str(a)}0'), s)
elif a == 0:
    print(s, s)
else:
    print(a, s)
