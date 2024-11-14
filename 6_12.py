#Задача L
people = []
for _ in range(int(input())):
    people.append(input())
people = [i + ' - ' + str(people.count(i)) for i in set(people) if people.count(i) > 1]
if people:
    for x in sorted(people):
        print(x)
else:
    print('Однофамильцев нет')