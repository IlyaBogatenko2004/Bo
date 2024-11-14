#Задача G
name = input()
numbers = []
with open(name, 'r') as f:
    for line in f:
        numbers.extend([int(x) for x in line.split()])
print(len(numbers))
print(len(list(filter(lambda x: x > 0, numbers))))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(round(sum(numbers) / len(numbers), 2))