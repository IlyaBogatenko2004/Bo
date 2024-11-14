#задача D
n = int(input())
s = int(input())
k = int(input())
m2 = n + s + k - max(n, s, k) - min(n, s, k)
if max(n, s, k) == n:
    p = 'Петя'
elif max(n, s, k) == s:
    p = 'Вася'
elif max(n, s, k) == k:
    p = 'Толя'
v = ''
if m2 == n:
    v = 'Петя'
elif m2 == s:
    v = 'Вася'
elif m2 == k:
    v = 'Толя'
t = ''
if min(n, s, k) == n:
    t = 'Петя'
elif min(n, s, k) == s:
    t = 'Вася'
elif min(n, s, k) == k:
    t = 'Толя'
print(f'1. {p}')
print(f'2. {v}')
print(f'3. {t}')  