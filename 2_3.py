#задача C
n = int(input())
s = int(input())
k = int(input())
if n > s and n > k:
    print('Петя')
elif s > n and s > k:
    print('Вася')
elif k > n and k > s:
    print('Толя')
