#Задача H
def update(journal):
    j = journal.copy()
    for i in range(len(j.loc[:, 'name'])):
        j.loc[:, 'average'] = (j['maths'] + j['physics'] + j['computer science']) / 3
    return j.sort_values(by=['average', 'name'], ascending=(False, True))