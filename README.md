# basics-of-programming-Python

Примітка: 
	Правильність роботи функції перевіряйте в конструкції 
if _ _name_ _ == ‘_ _main_ _’

Завдання 1. 
	Створити найпростіший декоратор function_decorator(), який в функції-обгортки wrapper() виводить два рядка - “До виклику функції” і “Після виклику функції”.
	Напишіть функцію, яка повертає суму двох цілих чисел та додайте до неї декоратор  function_decorator().

### Код:

``` python

def function_decorator(original_function):
    def wrapper(a, b):
        print('До виклику функції')
        result = original_function(a, b)
        print(result)
        print('Після виклику функції')
        return result
    return wrapper

@function_decorator
def add_num(a, b):
    return a + b

if __name__ == '__main__':
    add_num(1, 2)
```
### Результат:

![img.png](img.png)

Завдання 2.
	Напишіть функцію get_rectangle_area(), яка повертає площу прямокутника, яка розраховується по двом параметрам:  width і height.
Визначте декоратор show_console() для цієї функції, який відображає результат на екрані у вигляді рядка:
"Площа прямокутника: <значення>"

### Код:

``` python

def show_console(func):
    def wrapper(width, height):
        result = func(width, height)
        print(f"Площа прямокутника: {result}")
        return result
    return wrapper

@show_console
def get_rectangle_area(width, height):
    return width * height

if __name__ == "__main__":
    get_rectangle_area(4321, 234467890)
```
### Результат:

![img.png](img_1.png)

Завдання 3. 
	Напишіть функцію create_user(), яка приймає параметри username та password і повертає словник, що представляє нового користувача по заданим параметрам.
	Напишіть декоратор validate_input(), який перевіряє, чи передані дані проходять наступним критеріям:
довжина username більше 3 символів і значення є рядковим типом;
довжина password більше 6 символів і значення є рядковим типом.
Придумайте і додайте додатково ще 3 перевірки.

### Код
```python
def validate_input(func):
    def wrapper(username, password):
        if not isinstance(username, str) or len(username) <= 3:
            return "Username повинен бути рядком і мати більше 3 символів"
        if not isinstance(password, str) or len(password) <= 6:
            return "Password повинен бути рядком і мати більше 6 символів"
        if ' ' in username:
            return "Username не повинен містити пробіли"
        if ' ' in password:
            return "Password не повинен містити пробіли"
        if not any(char.isdigit() for char in password):
            return "Password повинен містити хоча б одну цифру"
        return func(username, password)

    return wrapper


@validate_input
def create_user(username, password):
    return {"username": username, "password": password}


if __name__ == "__main__":
    print(create_user("yaroslav", "12345678"))
```
### Результат
![img_2.png](img_2.png)