# Практична робота 19

## Завдання 1.
Напишіть функцію яка повертає переданий їй рядок у нижньому регістрі (з малими літерами).
Напишіть декоратор tagging для цієї функції, який має один параметр tag, що визначає рядок із назвою тега та початковим значенням "h1". Цей декоратор має укладати повернутий функцією рядок у тег tag і повертати результат.

Приклад роботи декоратора для рядка "python" та тегу h1:

<h1>python</h1>

### Код:
```python
def tagging(tag="h1"):
    def decorator(func):
        def wrapper(text):
            return f"<{tag}>{func(text)}</{tag}>"
        return wrapper
    return decorator

@tagging("h1")
def to_lowercase(text):
    return text.lower()

if __name__ == "__main__":
    print(to_lowercase("PYTHON"))
```
### Консоль:
![img.png](img.png)
## Завдання 2. 
Створіть декоратор log_calls(filename), який записує у вказаний файл формату .txt ім'я функції, що була викликана, її аргументи та результат виконання.
Файл повинен містити історію всіх викликів функції та не очищуватися між запусками програми. Приклад використання:

У файлі log.txt має з’явитися наступне:
Функція multiply викликана з аргументами (3, 4), результат: 12
Функція multiply викликана з аргументами (5, 2), результат: 10
### Код:
```python
import os

def log_calls(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            log_entry = f"Функція {func.__name__} викликана з аргументами {args}, результат: {result}\n"
            with open(filename, 'a', encoding="utf-8") as file:
                file.write(log_entry)
            return result
        return wrapper
    return decorator

@log_calls("log.txt")
def multiply(a, b):
    return a * b

if __name__ == '__main__':
    print(multiply(1, 2))
    print(multiply(2, 3))
    print(multiply(3, 4))
    print(multiply(5, 6))
    print(multiply(7, 8))
    print(multiply(9, 10))
```
### Консоль:
 ```  ```
## Завдання 3.
Реалізуйте декоратор cache_results, який зберігатиме результати виклику функції для однакових аргументів.
Якщо функція викликається вперше з певними аргументами, її результат обчислюється та зберігається в кеші. А якщо функція викликається повторно з такими самими аргументами, замість повторного обчислення повертається збережене значення.
Підказка: Використовуйте словник для збереження кешованих значень, де ключем буде кортеж аргументів(навіть якщо викликається з одним аргументом.
	Приклад використання такого декоратора:


Результат роботи програми:


### Код:
```python
def cache_results(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            print("Результат з кешу: ", args)
            return cache[args]
        print("Обчислюємо результат для: ", args)
        result = func(*args)
        cache[args] = result
        return result

    return wrapper

@cache_results
def multiply(a, b):
    return a * b

print(multiply(2, 3))
print(multiply(2, 3))
print(multiply(4, 5))
print(multiply(4, 5))
```
### Консоль:
![img_1.png](img_1.png)
## Завдання 4.
Напишіть функцію get_list яка приймає обʼєкт рядка. Сама функція повинна повертати список з цілих чисел, які надходить на її вхід у вигляді рядка з цілих чисел, записаних через пробіл. Приклад такого рядка:

“1 2 3 4 5”

Додайте рядок документації для функції get_list.  Визначте декоратор sum_list, який виконує підсумовування значень зі списку цієї функції та повертає результат.
Усередині декоратора декоруйте передану функцію get_list за допомогою команди @wraps (не забудьте зробити імпорт: from functools import wraps). Таке декорування необхідне, щоб вихідна функція get_list зберігала свої локальні властивості: __name__ і __doc__.
### Код:
```python
from functools import wraps

def sum_list(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        numbers = func(*args, **kwargs)
        return sum(numbers)
    return wrapper

@sum_list
def get_list(s):
    result = []
    for i in s.split():
        result.append(int(i))
    return result

if __name__ == "__main__":
    print(get_list("10 20 30 40"))
```
### Консоль:
![img_2.png](img_2.png)
## Завдання 5. 
Реалізуйте два декоратори: uppercase(перетворює результат функції на верхній регістр) та exclaim(додає три знаки оклику (!!!) до результату функції).
Застосуйте ці декоратори до двох різних функцій одночасно. Можете придумати власні функції, які повертатимуть рядок. Якщо ж ідей немає, скористайтеся наведеними прикладами: 
greet(name) – повертає рядок "Привіт, {name}".
farewell(name) – повертає рядок "До побачення, {name}".
### Код:
```python
def uppercase(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

def exclaim(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + "!!!"
    return wrapper

@exclaim
@uppercase
def greet(name):
    return f"Привіт, {name}"

@uppercase
@exclaim
def farewell(name):
    return f"До побачення, {name}"

if __name__ == "__main__":
    print(greet("Ярослав"))   
    print(farewell("Ярослав"))
```
### Консоль:
![img_3.png](img_3.png)