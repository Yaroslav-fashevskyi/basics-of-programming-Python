def addition(first_number, second_number):
    return first_number + second_number

def subtraction(first_number, second_number):
    return first_number - second_number

def multiplication(first_number, second_number):
    return first_number * second_number

def division(first_number, second_number):
    if second_number == 0:
        return "Помилка: друге число дорівнює 0"
    return first_number / second_number

def power(first_number, second_number):
    return first_number ** second_number


def perform_calculation():
    first_number = float(input("Введіть перше число: "))
    second_number = float(input("Введіть друге число: "))
    action = input("Введіть дію яку потрібно виконати (+, -, *, /, **): ")

    if action == "+":
        result = addition(first_number, second_number)
    elif action == "-":
        result = subtraction(first_number, second_number)
    elif action == "*":
        result = multiplication(first_number, second_number)
    elif action == "/":
        result = division(first_number, second_number)
    elif action == "**":
        result = power(first_number, second_number)
    else:
        print("такої дії не існує")

    print(f"{first_number} {action} {second_number} = {result}")

#perform_calculation()

def ask_continue():
    response = input("Хочете продовжити (так/ні)? ").strip().lower()
    return response == "так"

def main():
    while True:
        perform_calculation()
        if not ask_continue():
            print("Дякуємо за використання калькулятора!")
            break

main()
'''


Етап 2.

Етап 3.
Створіть функцію ask_continue(), яка повертає логічне значення, що вказує, чи хоче користувач продовжити користуватися калькулятором.
Створіть функцію main(), яка об’єднує всі функції, які створені на попередніх етапах. Ця функція повинна слугувати точкою входу у вашу програму. Для повноцінної роботи калькулятора не забудьте використати безкінечний цикл.

'''