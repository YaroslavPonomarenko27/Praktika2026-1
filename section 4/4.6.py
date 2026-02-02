class Shape:
    def draw(self):
        print("Фігура")

class Circle(Shape):
    def draw(self):
        print("Коло")

class Square(Shape):
    def draw(self):
        print("Квадрат")

# Використання
shapes = [Circle(), Square()]
for s in shapes:
    s.draw()
