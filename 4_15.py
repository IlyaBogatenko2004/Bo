#Задача O
N = int(input())
M = int(input())
snake = [[0] * M for _ in range(N)]
num = 1
for col in range(M):
    if col % 2 == 0:
        for row in range(N):
            snake[row][col] = num
            num += 1
    else:
        for row in range(N - 1, -1, -1):
            snake[row][col] = num
            num += 1
max_width = len(str(N * M))
for row in snake:
    print(" ".join(f"{x:>{max_width}}" for x in row))
