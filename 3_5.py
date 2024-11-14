# задача E
s = 0
while True:
    k = float(input())
    if k >= 500:
        s += 0.9 * k
    if k < 500:
        s += k
    if k == 0:
        break
print(s)                