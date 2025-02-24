number_of_grades = int(input("Enter number of grades: "))
grade_list = []

for a in range(1, number_of_grades + 1):
    while True:
        grade = int(input(f"Enter grade {a}: "))
        if 1 <= grade <= 12:
            grade_list.append(grade)
            break
        else:
            print("Помилка: Введіть оцінку від 1 до 12")
if grade_list:
    average = sum(grade_list) / len(grade_list)
    print(f"The average grade is {average}")
else:
    print("Не введено жодної оцінки")


if grade_list:
    if average >= 10:
        print("Відмінно")
    elif average >= 7:
        print("Добре")
    elif average >= 4:
        print("Задовільно")
    elif average >= 1:
        print("Незадовільно")

'''


Створіть програму, яка запитує у користувача кількість оцінок, а потім приймає самі оцінки (від 1 до 12).
 Після введення всіх оцінок програма повинна вивести середній бал.
  Також повинно сформуватися повідомлення про його успішність,
   наприклад “Відмінно” для 10-12 балів, “добре” для 7-9 і так далі.
'''