class Car:
    def __init__(self, model):
        self.model = model

    def show(self):
        print("Модель автомобіля:", self.model)

c = Car("Toyota")
c.show()
