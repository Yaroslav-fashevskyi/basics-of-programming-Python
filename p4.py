num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))

print("Оберіть операцію:")
print("1. Додавання (+)")
print("2. Віднімання (-)")
print("3. Множення (*)")
print("4. Ділення (/)")
print("5. Піднесення до степеня (**)")

operation = input("Введіть номер операції (1/2/3/4/5): ")

if operation == '1':
    result = num1 + num2
    print(f"Результат: {num1} + {num2} = {result}")
elif operation == '2':
    result = num1 - num2
    print(f"Результат: {num1} - {num2} = {result}")
elif operation == '3':
    result = num1 * num2
    print(f"Результат: {num1} * {num2} = {result}")
elif operation == '4':
    if num2 == 0:
        print("Помилка: Ділення на нуль!")
    else:
        result = num1 / num2
        print(f"Результат: {num1} / {num2} = {result}")
elif operation == '5':
    result = num1 ** num2
    print(f"Результат: {num1} ** {num2} = {result}")
else:
    print("Помилка: Невірний номер операції!")

'''
Створіть програму для виконання основних арифметичних операцій:
додавання, віднімання, множення, ділення та піднесення до степеня.
 Користувач повинен вводити два числа і після цього обирати операцію, яку хоче здійснити над цими числами.
  Також додайте перевірку ділення на нуль, виведіть помилку через print().
'''