#Задача F
N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))
gcd = numbers[0] 
for i in range(1, N):
    a = gcd
    b = numbers[i]
    while b != 0:
        a, b = b, a % b
    gcd = a 
print(gcd)
