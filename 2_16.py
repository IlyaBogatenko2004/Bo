#задача P
q = int(input())
w = int(input())
e = int(input())
a = max(q, w, e)
d = min(q, w, e)
s = q + w + e - a - d
z = 'Петя'
x = 'Вася'
c = 'Толя'
if a == q and s == w and d == e:
    print(f"{z: ^24}")
    print(f"  {x: <22}")
    print(f"{c: >22}  ")
    print('   II      I      III ')
elif a == w and s == e and d == q:
    print(f"{x: ^24}")
    print(f"  {c: <22}")
    print(f"{z: >22}  ")
    print('   II      I      III ')
elif a == e and s == w and d == q:
    print(f"{c: ^24}")
    print(f"  {x: <22}")
    print(f"{z: >22}  ")
    print('   II      I      III ')
elif a == e and s == q and d == w:
    print(f"{c: ^24}")
    print(f"  {z: <22}")
    print(f"{x: >22}  ")
    print('   II      I      III ')
elif a == w and s == q and d == e:
    print(f"{x: ^24}")
    print(f"  {z: <22}")
    print(f"{c: >22}  ")
    print('   II      I      III ')
elif a == q and s == e and d == w:
    print(f"{z: ^24}")
    print(f"  {c: <22}")
    print(f"{x: >22}  ")
    print('   II      I      III ')
