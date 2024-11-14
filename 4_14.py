#Задача N
N = int(input())
M = int(input())
snake = []
counter = 1
for i in range(N):
    row = []
    for j in range(M):
        row.append(counter)
        counter += 1
    if i % 2 == 1:  
        row.reverse()
    snake.append(row)
max_width = len(str(snake[-1][-1])) 
for row in snake:
    print(" ".join(f"{num:>{max_width}}" for num in row))
