#Задача H
for _ in range(int(input())):
    if "зайка" in (place := input()):
        print(place.index("зайка") + 1)
    else:
        print("Заек нет =(")
