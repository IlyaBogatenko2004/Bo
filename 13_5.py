#Задача E
class Rectangle:
    def __init__(self, *coords):
        self.coords = coords
        self.first_line = abs(self.coords[0][0] - self.coords[1][0])
        self.second_line = abs(self.coords[0][1] - self.coords[1][1])

    def perimeter(self):
        return round(2 * (self.first_line + self.second_line), 2)

    def area(self):
        return round(self.first_line * self.second_line, 2)