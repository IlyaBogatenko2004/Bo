#Задача L
N = int(input())
M = int(input())
current_number = 1
width = len(str(N * M))
for i in range(N):
    row = []
    for j in range(M):
        row.append(str(current_number).rjust(width))
        current_number += 1
    print(" ".join(row))
