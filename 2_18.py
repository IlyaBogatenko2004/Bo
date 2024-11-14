#задача R
a = int(input())
b = int(input())
c = int(input())
x = max(a, b, c)
z = min(a, b, c)
y = a + b + c - x - z
if x ** 2 == y ** 2 + z ** 2:
    print('100%')
elif x ** 2 < y ** 2 + z ** 2:
    print('крайне мала')   
elif x ** 2 > y ** 2 + z ** 2:
    print('велика')