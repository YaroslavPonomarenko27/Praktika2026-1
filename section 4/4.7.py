class Shape:
    def area(self):
        return 0

    def draw(self):
        print("Фігура")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def draw(self):
        print("Прямокутник")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def draw(self):
        print("Коло")

shapes = [
    Rectangle(5, 4),
    Circle(3),
    Rectangle(2, 7),
    Circle(5)
]

for shape in shapes:
    shape.draw()
    print("Площа:", shape.area())
