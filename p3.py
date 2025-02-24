import json


num_books = int(input("Скільки книг ви хочете записати?: "))
input_books = []


for i in range(num_books):
    print(f"Введіть інформацію про книгу {i + 1}:")

    title = input("Назва книги: ")
    author = input("Автор книги: ")
    year = int(input("Рік публікації: "))
    pages = int(input("Кількість сторінок: "))

    book = {
        "Назва книги": title,
        "Автор книги": author,
        "Рік публікації": year,
        "Кількість сторінок": pages
    }

    input_books.append(book)
file_name = "books_data_getrfgew7gfbweugfuwegfyuewgfiwue.json"
with open(file_name, 'w', encoding='utf-8') as file:
    json.dump(input_books, file, ensure_ascii=False, indent=4)


with open(file_name, 'r', encoding='utf-8') as file:
    books_content = json.load(file)
    print("Вміст JSON файлу:")
    print(json.dumps(books_content, ensure_ascii=False, indent=4))
'''
Створіть програму, яка запитує у користувача дані про книги та записує їх у JSON-файл.
 Кожна книга повинна містити наступну інформацію:
Назва книги.
Автор книги.
Рік публікації.
Кількість сторінок.
Програма повинна виконувати наступне:
Запитувати у користувача кількість книг, які потрібно зберегти.
Для кожної книги отримувати інформацію від користувача та зберегти її в словник input_books.
Після завершення запису, запишіть всі дані в  файл формату JSON  і після цього виведіть його вміст на екран.

'''