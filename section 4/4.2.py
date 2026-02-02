# Базовий клас
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Привіт, мене звати {self.name}")

# Створення об'єкта
p = Person("Іван", 30)
p.greet()
