from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def fuel_type(self):
        pass


class Car(Vehicle):
    def move(self):
        print("Автомобіль їде дорогою")

    def fuel_type(self):
        print("Паливо: бензин")


class ElectricScooter(Vehicle):
    def move(self):
        print("Електросамокат рухається містом")

    def fuel_type(self):
        print("Паливо: електроенергія")


vehicles = [Car(), ElectricScooter()]

for v in vehicles:
    v.move()
    v.fuel_type()
    print("----------------")
