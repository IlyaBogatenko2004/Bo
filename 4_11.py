#Задача K
N = int(input())
numbers = [int(input()) for _ in range(N)]
prime_count = 0
for number in numbers:
    if number < 2:
        continue  
    is_prime = True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_count += 1
print(prime_count)
