from datetime import datetime
def user_info(name: str, age: int = None, birth_date: str = None, show_birth_year: bool = False):
    current_year = datetime.now().year
    if age == None:
        age = "невідомий"
    if birth_date == None:
        birth_date = "невідома"

    birth_year_info = ""
    if age is not None and show_birth_year:
        birth_year = current_year - age
        birth_year_info = f", Рік народження: {birth_year}"
    return f"Ім'я: {name}, Вік: {age}, Дата народження: {birth_date} {birth_year_info}]"

print(user_info("Олег"))
print(user_info("Аліна", 25, "15.04.1999"))
print(user_info("Юля", 30, show_birth_year=True))

'''
Завдання 2.

Функція повинна повертати інформацію про користувача у форматі:
"Ім'я: [name], Вік: [age або 'невідомий'], Дата народження: [birth_date або 'невідома']".
Розширте функцію user_info, додавши необов'язковий параметр:
show_birth_year (bool): прапорець, що вказує, 
чи потрібно виводити рік народження користувача на основі віку (необов'язковий параметр, за замовчуванням False).
Якщо show_birth_year дорівнює True, і вік вказаний, виведіть додаткову інформацію 
з роком народження користувача, який обчислюється за формулою: поточний рік - вік.

'''