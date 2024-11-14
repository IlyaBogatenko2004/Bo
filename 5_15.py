#Задача O
numbers = list(map(int, input().split()))
a = numbers[0]
while len(numbers) > 1:
    b = numbers[1]
    while b:
        a, b = b, a % b
    numbers.pop(1)
print(a)