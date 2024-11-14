#задача I
q = input()
w = input()
e = input()
a = q[0]
s = w[0]
d = e[0]
if min(a, s, d) == a:
    print(q)
elif min(a, s, d) == s:
    print(w)
elif min(a, s, d) == d:
    print(e)
