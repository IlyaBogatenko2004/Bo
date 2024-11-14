#Задача D
class Fraction:

    def __simp(self, coords):
        a, b = coords[0], coords[1]
        while b:
            a, b = b, a % b
        return coords[0] // a, coords[1] // a

    def __init__(self, *args):
        if isinstance(args[0], str):
            self.n, self.d = self.__simp(tuple(map(int, args[0].split('/'))))
        else:
            self.n, self.d = self.__simp(args)

    def numerator(self, number=0):
        if number:
            self.n, self.d = self.__simp((number, self.d))
        return self.n

    def denominator(self, number=0):
        if number:
            self.n, self.d = self.__simp((self.n, number))
        return self.d

    def __str__(self):
        return f"{self.n}/{self.d}"

    def __repr__(self):
        return f"Fraction({self.n}, {self.d})"