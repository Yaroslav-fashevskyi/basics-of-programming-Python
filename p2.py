file_name = input("Enter file name: ")

with open(file_name, 'w', encoding='utf-8') as file:
    print("Введіть текст для запису у файл. Для завершення введення натисніть Enter на порожньому рядку.")
    while True:
        text = input()
        if text == "":
            break
        file.write(text + "\n")

with open(file_name, 'r', encoding='utf-8') as file:
    content = file.read()

print("Вміст файлу:")
print(content)

'''
Створіть програму, яка виконує такі дії:
Програма запитує у користувача ім'я файлу для створення.
Користувач вводить рядки тексту, які потрібно записати у файл.
Введення завершується, коли користувач вводить порожній рядок.
Після запису програма зчитує весь текст із файлу та виводить його на екран.

'''