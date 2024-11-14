# задача J
x = 0
y = 0
while True:
    s = input()
    if s == "СТОП":
        break
    e = int(input())
    if s == "СЕВЕР":
        y = y + e
    if s == "ЮГ":
        y = y - e
    if s == "ВОСТОК":
        x = x + e
    if s == "ЗАПАД":
        x = x - e   
print(y)
print(x)                   
