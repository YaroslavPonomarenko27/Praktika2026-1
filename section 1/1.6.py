# Звичайна функція
def add(a, b):
    return a + b

result = add(5, 3)
print("Сума:", result)

# Рекурсивна функція
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("Факторіал 5:", factorial(5))
