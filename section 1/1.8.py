# Запис у файл
with open("example.txt", "w") as f:
    f.write("Привіт, файл!\n")
    f.write("Python працює!")

# Читання з файлу
with open("example.txt", "r") as f:
    for line in f:
        print(line.strip())
