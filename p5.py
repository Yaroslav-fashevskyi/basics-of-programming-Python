students_grades = {
    "Ярослав": [85, 90, 78],
    "Олег": [92, 88, 95],
    "Іван": [75, 80, 70],
    "Аліна": [88, 91, 84],
    "Артем": [60, 70, 65]
}

print("Середні оцінки студентів:")
for student, grades in students_grades.items():
    average = sum(grades) / len(grades)
    print(f"Студент {student} має середню оцінку: {average}")

student_to_update = "Артем"
new_grade = 95

if student_to_update in students_grades:
    students_grades[student_to_update].append(new_grade)
    print(f"\nОновлені оцінки для {student_to_update}: {students_grades[student_to_update]}")

    # Обчислення нової середньої оцінки
    updated_average = sum(students_grades[student_to_update]) / len(students_grades[student_to_update])
    print(f"Середня оцінка {student_to_update} після додавання нової оцінки: {updated_average:.2f}")
else:
    print(f"\nСтудент {student_to_update} якись невідомий чувак якого немає в списку")


print("\n⭐️ Рейтинг студентів на основі середніх оцінок ⭐️")
sorted_students = sorted(students_grades.items(), key=lambda x: sum(x[1]) / len(x[1]), reverse=True)
for i, (student, grades) in enumerate(sorted_students, start=1):
    average = sum(grades) / len(grades)  # Обчислення середньої оцінки
    print(
        f"{i}. {student}: середня оцінка {average:.2f} - {'🎉 Вітаємо!' if average >= 85 else '💪 Працюйте над собою!'}")

'''
Напишіть програму для обчислення середніх оцінок студентів. Створіть словник, де ключем буде ім'я студента, а значенням — список його оцінок.
Додайте оцінки декільком студентам.
Обчисліть та виведіть середню оцінку для кожного студента.
Додайте нову оцінку для конкретного студента та виведіть його оцінки.
Придумайте цікавий вивід, можете використати для цього штучний інтелект.

'''