#Задача M
N = int(input())
M = int(input())
rectangle = []
for i in range(N):
    row = []
    for j in range(M):
        value = (i + 1) + j * N
        row.append(value)
    rectangle.append(row)
max_width = len(str(rectangle[-1][-1])) 
for row in rectangle:
    print(" ".join(f"{num:>{max_width}}" for num in row))
