# задача F
name = str(input())
price = int(input())
weight = int(input())
money = int(input())
total_cost = price * weight
change = money - total_cost
print("Чек")
print(f"{name} - {weight}кг - {price}руб/кг")
print(f"Итого: {total_cost}руб")
print(f"Внесено: {money}руб")
print(f"Сдача: {change}руб")