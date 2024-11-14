#Задача F
def best(j):
    new_j = j.copy()
    return new_j[(new_j['maths'] > 3) & (new_j['physics'] > 3) & (new_j['computer science'] > 3)]