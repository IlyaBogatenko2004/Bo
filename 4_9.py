#Задача I
N = int(input())
max_digits = []
for _ in range(N):
    number = input()
    max_digit = max(number)
    max_digits.append(max_digit)
big_number = ''.join(max_digits)
print(big_number)

