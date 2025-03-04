"""
Завдання 1.
	Створити найпростіший декоратор function_decorator(),
	який в функції-обгортки wrapper() виводить два рядка -
	“До виклику функції” і “Після виклику функції”.
	Напишіть функцію, яка повертає суму двох цілих чисел та
	 додайте до неї декоратор  function_decorator().
"""

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




