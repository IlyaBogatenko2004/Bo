#Задача F
def order(*args):
    temp = in_stock
    GRADES = {
        "Эспрессо": {"coffee": 1},
        "Капучино": {"coffee": 1,
                     "milk": 3},
        "Макиато": {"coffee": 2,
                    "milk": 1},
        "Кофе по-венски": {"coffee": 1,
                           "cream": 2},
        "Латте Макиато": {"coffee": 1,
                          "milk": 2,
                          "cream": 1},
        "Кон Панна": {"coffee": 1,
                      "cream": 1},
    }
    for grade in args:
        for ingr in GRADES[grade]:
            if GRADES[grade].get(ingr, 0) > in_stock[ingr]:
                break
        else:
            for ingr in GRADES[grade]:
                in_stock[ingr] -= GRADES[grade][ingr]
            return grade
    if in_stock == temp:
        return "К сожалению, не можем предложить Вам напиток"