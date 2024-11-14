#Задача P
size = int(input())
width = int(input())
cell_format = f"{{:^{width}}}"
for i in range(1, size + 1):
    row = " | ".join(cell_format.format(i * j) for j in range(1, size + 1))
    print(row.replace(' | ', '|'))
    if i < size:
        print('-' * (size * (width + 1) - 1))
