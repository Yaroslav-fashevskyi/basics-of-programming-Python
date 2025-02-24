student1 = ("Іваненко", "Іван", 2002, ["математика", "фізика", "python"])
student2 = ("Петренко", "Андрій", 2001, ["алгебра", "геометрія", "java"])
student3 = ("Фашевський", "Ярослав", 2003, ["історія", "python", "фізика"])
students = [student1, student2, student3]
subject_to_find = "python"

print("Інформація про студентів:")
for student in students:
    surname, name, birth_year, subjects = student
    print(f"Прізвище: {surname}, Ім'я: {name}, Рік народження: {birth_year}, Предмети: {', '.join(subjects)}")

print(f"\nСтуденти, які вивчають {subject_to_find}:")
for student in students:
    surname, name, birth_year, subjects = student
    if subject_to_find in subjects:
        print(f"Прізвище: {surname}, Ім'я: {name}, Рік народження: {birth_year}, Предмети: {', '.join(subjects)}")




'''
Завдання 1.
Створіть програму, яка працює з інформацією про курси студентів. Кожен студент має такі дані:
Прізвище;
Ім'я;
Рік народження;
Список предметів, які він вивчає (математика, фізика, інформатика тощо).
Завдання:
Створіть кортежі для трьох студентів з різною інформацією.
Виведіть інформацію про кожного студента на екран(не об’єктом tuple!).
Знайдіть та виведіть на екран інформацію про студентів, які вивчають конкретний предмет(предмет – довільний).
Для виконання завдання використовуйте цикли та оператори умов.

# Виведення інформації про кожного студента


# Пошук студентів, які вивчають конкретний предмет
subject_to_find = "математика"  # Задаємо предмет для пошуку
print(f"\nСтуденти, які вивчають {subject_to_find}:")
for student in students:
    surname, name, birth_year, subjects = student
    if subject_to_find in subjects:
        print(f"Прізвище: {surname}, Ім'я: {name}, Рік народження: {birth_year}, Предмети: {', '.join(subjects)}")

'''
