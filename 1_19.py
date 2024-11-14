# задача S
tov = input()
cen = int(input())
ves = int(input())
kolvo = int(input())
s = cen * ves
sd = kolvo - s
s2 = ' ' * (35 - 6 - len(tov))
s3 = ' ' * (35 - 5 - 6 - 2 - 3 - len(str(ves)) - len(str(cen)))
s4 = ' ' * (35 - 6 - 3 - len(str(s)))
s5 = ' ' * (35 - 8 - 3 - len(str(kolvo)))
s6 = ' ' * (35 - 6 - 3 - len(str(sd)))
print('================Чек================')
print(f'Товар:{s2}{tov}')
print(f'Цена:{s3}{ves}кг * {cen}руб/кг')
print(f'Итого:{s4}{s}руб')
print(f'Внесено:{s5}{kolvo}руб')
print(f'Сдача:{s6}{sd}руб')
print('===================================')
    