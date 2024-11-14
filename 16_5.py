#Задача E
from math import dist, cos, sin

deca_x, deca_y = map(float, input().split())
pola_r, pola_f = map(float, input().split())
pola_x = pola_r * cos(pola_f)
pola_y = pola_r * sin(pola_f)
print(dist((deca_x, deca_y), (pola_x, pola_y)))