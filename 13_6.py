#Задача F
class Rectangle:
    def __init__(self, *coords):
        self.coords = coords
        self.upper_left_x = round(min(self.coords[0][0], self.coords[1][0]), 2)
        self.upper_left_y = round(max(self.coords[0][1], self.coords[1][1]), 2)
        self.lower_right_x = round(max(self.coords[0][0], self.coords[1][0]), 2)
        self.lower_right_y = round(min(self.coords[0][1], self.coords[1][1]), 2)
        self.width = abs(self.coords[0][0] - self.coords[1][0])
        self.height = abs(self.coords[0][1] - self.coords[1][1])

    def perimeter(self):
        return round(2 * (self.width + self.height), 2)

    def area(self):
        return round(self.width * self.height, 2)

    def get_pos(self):
        return self.upper_left_x, self.upper_left_y

    def get_size(self):
        return round(self.width, 2), round(self.height, 2)

    def move(self, dx, dy):
        self.coords = (self.coords[0][0] + dx, self.coords[0][1] + dy), (self.coords[1][0] + dx, self.coords[1][1] + dy)
        self.__init__(*self.coords)

    def resize(self, width, height):
        self.coords = self.get_pos(), (self.upper_left_x + width, self.upper_left_y - height)
        self.__init__(*self.coords)