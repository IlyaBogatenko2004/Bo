# задача G
q = int(input())
w = int(input())
noc = 0
for i in range(q * w + 1):
    if i % q == 0 and i % w == 0:
        noc = i
    if noc != 0:
        print(noc)
        break        