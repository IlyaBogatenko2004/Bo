#Задача G
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
            if self.n > 0:
                self.n, self.d = self.__simp((abs(number), self.d))
                self.n = -self.n if number < 0 else self.n
            elif self.n < 0:
                self.n, self.d = self.__simp((abs(number), self.d))
                self.n = -self.n if number > 0 else self.n
        return abs(self.n)

    def denominator(self, number=0):
        if number:
            if self.n > 0:
                self.n, self.d = self.__simp((self.n, abs(number)))
                self.n = -self.n if number < 0 else self.n
            elif self.n < 0:
                self.n, self.d = self.__simp((abs(self.n), abs(number)))
                self.n = -self.n if number > 0 else self.n
        return self.d

    def __neg__(self):
        return Fraction(-self.n, self.d)

    def __add__(self, other):
        return Fraction(self.n * other.d + other.n * self.d, self.d * other.d)

    def __iadd__(self, other):
        self.n, self.d = self.__simp((self.n * other.d + other.n * self.d, self.d * other.d))
        return self

    def __sub__(self, other):
        return Fraction(self.n * other.d - other.n * self.d, self.d * other.d)

    def __isub__(self, other):
        self.n, self.d = self.__simp((self.n * other.d - other.n * self.d, self.d * other.d))
        return self

    def __mul__(self, other):
        return Fraction(self.n * other.n, self.d * other.d)

    def __imul__(self, other):
        self.n, self.d = self.__simp((self.n * other.n, self.d * other.d))
        return self

    def __truediv__(self, other):
        return Fraction(self.n * other.d, self.d * other.n)

    def __itruediv__(self, other):
        self.n, self.d = self.__simp((self.n * other.d, self.d * other.n))
        return self

    def reverse(self):
        self.n, self.d = self.__simp((self.d, self.n))
        return self

    def __str__(self):
        return f"{self.n}/{self.d}"

    def __repr__(self):
        return f"Fraction('{self.n}/{self.d}')"