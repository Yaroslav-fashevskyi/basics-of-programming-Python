import math
import random


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius ** 2)

    def get_circumference(self):
        return 2 * math.pi * self.radius


if __name__ == '__main__':

    rect_length = random.randint(1, 10)
    rect_width = random.randint(1, 10)
    rectangle = Rectangle(rect_length, rect_width)


    circle_radius = random.randint(1, 10)
    circle = Circle(circle_radius)

    print("Прямокутник: довжина =", rect_length, ", ширина =", rect_width)
    print("Площа прямокутника:", rectangle.get_area())
    print("Периметр прямокутника:", rectangle.get_perimeter())

    print("Коло: радіус =", circle_radius)
    print("Площа кола:", circle.get_area())
    print("Довжина кола:", circle.get_circumference())
