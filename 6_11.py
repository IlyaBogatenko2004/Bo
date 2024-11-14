#Задача K
people = []
for _ in range(int(input())):
    people.append(input())
print(len([i for i in people if people.count(i) > 1]))