#Задача G
N = int(input())
for participant in range(1, N + 1):
    delay = participant + 2
    for seconds in range(delay, 0, -1):
        print(f"До старта {seconds} секунд(ы)")
    print(f"Старт {participant}!!!")
