# задача B
s = 0
while True:
    k = input()
    if k == "Приехали!":
        break
    if "зайка" in k:
        s += 1
print(s)        