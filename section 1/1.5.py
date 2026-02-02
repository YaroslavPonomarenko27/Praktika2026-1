text = "Програмування мовою Python"

print("Довжина рядка:", len(text))
print("Великими літерами:", text.upper())
print("Малими літерами:", text.lower())

words = text.split(" ")
print("Слова в рядку:", words)

print("----------------------")

numbers = [5, 12, 3, 8, 20]

numbers.append(15)
numbers.insert(2, 10)
numbers.sort()

print("Відсортований список:", numbers)

print("Максимальне значення:", max(numbers))
print("Мінімальне значення:", min(numbers))
print("Сума елементів:", sum(numbers))

print("----------------------")

sentence = "Я вивчаю Python і алгоритми"
word_list = sentence.split()

print("Список слів:", word_list)

word_list.remove("і")
new_sentence = " ".join(word_list)

print("Нове речення:", new_sentence)
