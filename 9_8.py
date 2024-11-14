#Задача H
files_in = input(), input()
file_out = input()
words = [set(), set()]
for i in range(len(files_in)):
    with open(files_in[i], 'r') as file_in:
        for line in file_in:
            words[i].update({x for x in line.split()})
with open(file_out, 'w') as file_out:
    for word in sorted(words[0].symmetric_difference(words[1])):
        print(word, file=file_out)