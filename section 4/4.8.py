from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Гав-гав")

class Cat(Animal):
    def make_sound(self):
        print("Мяу")

animals = [Dog(), Cat()]
for a in animals:
    a.make_sound()
