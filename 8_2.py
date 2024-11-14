#Задача B
for kids in zip(a := input().split(', '), b := input().split(', ')):
    print(f'{kids[0]} - {kids[1]}')