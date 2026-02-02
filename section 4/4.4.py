class Student:
    def __init__(self, name, group, grades):
        self.name = name
        self.group = group
        self.grades = grades  

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

    def info(self):
        print("Ім'я:", self.name)
        print("Група:", self.group)
        print("Оцінки:", self.grades)
        print("Середній бал:", self.average_grade())


class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def info(self):
        print("Викладач:", self.name)
        print("Предмет:", self.subject)


student1 = Student("Марія", "ІПЗ-21", [90, 85, 88])
student2 = Student("Андрій", "ІПЗ-21", [75, 80, 78])

teacher = Teacher("Іван Петрович", "Програмування")

student1.add_grade(92)
student1.info()

print("------")

student2.info()

print("------")

teacher.info()
