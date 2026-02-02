# Базовий клас
class Shape:
    def draw(self):
        print("Фігура")

# Клас-нащадок
class Circle(Shape):
    def draw(self):
        print("Коло")

# Клас-нащадок
class Square(Shape):
    def draw(self):
        print("Квадрат")

# Список об'єктів різних класів
shapes = [Circle(), Square()]


for shape in shapes:
    shape.draw()
