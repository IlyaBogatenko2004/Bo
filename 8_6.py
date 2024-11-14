#Задача F
from itertools import product

nominal = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'валет', 'дама', 'король', 'туз']
suits = ['пик', 'треф', 'бубен', 'червей']
suits.remove(input())
for card in product(nominal, suits):
    print(card[0], card[1])