#Задача E
items = set()
for _ in range(3):
    items = items.union({item for item in input().split(', ')})
for i, item in enumerate(sorted(items), start=1):
    print(f'{i}. {item}')