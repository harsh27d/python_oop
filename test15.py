class Shape:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color


class Rectangle(Shape):
    def __init__(self, x, y, width, height, color):
        super().__init__(color)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


obj1 = Rectangle(0, 0, 50, 60, "red")

print("Area ",obj1.get_area())
print("Color",obj1.get_color())
        