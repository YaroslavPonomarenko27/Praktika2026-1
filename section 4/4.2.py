class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def info(self):
        print("Ім'я:", self.name)
        print("Оцінка:", self.grade)

# Створення об'єктів (екземплярів класу)
student1 = Student("Олена", 95)
student2 = Student("Андрій", 88)

student1.info()
print("-----")
student2.info()
