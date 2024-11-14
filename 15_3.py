#Задача C
class Broken:
    def __repr__(self):
        raise Exception


try:
    a = Broken()
    func(a)
except Exception:
    print('Ура! Ошибка!')