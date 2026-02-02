students = ["Анна", "Олег", "Ірина", "Максим"]
grades = [85, 90, 78, 88]

print("Список студентів та їх оцінки:")
for i in range(len(students)):
    print(students[i], "-", grades[i])

print("----------------------")

total = 0
index = 0

while index < len(grades):
    total += grades[index]
    index += 1

average = total / len(grades)
print("Середній бал групи:", average)

print("----------------------")


print("Оцінки вище 80:")
for grade in grades:
    if grade < 80:
        continue  
    print(grade)

print("----------------------")

print("Пошук першої оцінки нижче 80:")
for grade in grades:
    if grade < 80:
        print("Знайдено:", grade)
        break