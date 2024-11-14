#Задача G
def can_eat(horse, shape):
    return abs(horse[0] - shape[0]) + abs(horse[1] - shape[1]) == 3