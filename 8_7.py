#Задача G
from itertools import product

players, games = [], []
for _ in range(int(input())):
    players.append(input())
for i in product(players, players):
    if i[0] != i[1] and [i[1], i[0]] not in games:
        games.append([i[0], i[1]])
        print(f'{i[0]} - {i[1]}')