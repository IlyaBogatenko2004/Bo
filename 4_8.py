#Задача H
N = int(input())
winner_name = ""
max_digit_sum = -1
for _ in range(N):
    name = input().strip()  
    number = input().strip()  
    digit_sum = sum(int(digit) for digit in number)
    if digit_sum >= max_digit_sum: 
        max_digit_sum = digit_sum
        winner_name = name  
print(winner_name)

