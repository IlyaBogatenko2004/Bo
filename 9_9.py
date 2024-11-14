#Задача I
first_file, second_file = input(), input()
data = []
with open(first_file, 'r') as f:
    for line in f:
        data.append(line.strip().replace('\t', '').split())
data = [i for i in data if any(i)]
with open(second_file, 'w') as g:
    for line in data:
        print(' '.join(line), file=g)