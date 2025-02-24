minutes_input = int(input("Enter minutes: "))
hours = 60
hours_normal = minutes_input // hours
minutes_remainder = minutes_input % hours

print("Повних годин: ",hours_normal)
print("Хвилин залишилося: ",minutes_remainder)


'''Завдання 3.
Напишіть програму, яка приймає кількість хвилин і обчислює,
 скільки це повних годин та скільки хвилин залишилося після перетворення.
	Підказка: використовуйте оператори цілочисельного ділення та остачі від ділення.
'''