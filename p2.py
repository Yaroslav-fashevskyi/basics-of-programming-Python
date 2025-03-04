"""
Завдання 2.
	Напишіть функцію get_rectangle_area(), яка повертає площу прямокутника,
	 яка розраховується по двом параметрам:  width і height.
Визначте декоратор show_console() для цієї функції, який відображає результат на екрані у вигляді рядка:
"Площа прямокутника: <значення>"

"""

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
