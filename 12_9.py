#Задача I
def cycle(line):
    while line:
        for i in line:
            yield i