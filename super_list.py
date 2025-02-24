def find_max(lst):
    for item in lst:
        if not isinstance(item, (int, float)):
            return "Максимальний елемент: Помилка: список містить нечислові значення."
    lst.sort(reverse=True)
    return f"Максимальний елемент: {lst[0]}"

def find_min(lst):
    for item in lst:
        if not isinstance(item, (int, float)):
            return "Мінімальний елемент: Помилка: список містить нечислові значення."
    lst.sort(reverse=False)
    return f"Мінімальний елемент: {lst[0]}"

def average(lst):

    if all(isinstance(item, (int, float)) for item in lst):
         average_num = sum(lst) / len(lst)
         return f"Середнє значення: {average_num}"
    else:
        return "Помилка: список містить нечислові значення."

def remove_duplicates(lst):
    return f"Список без дублікатів: {list(set(lst))}"

def reverse_list(lst):
    return f"Список у зворотному порядку: {lst[::-1]}"

def filter_even(lst):
    even_numbers = []

    for item in lst:
        if isinstance(item, int):
            if item % 2 == 0:
                even_numbers.append(item)
    return f"Список з парними числами: {even_numbers}"





'''
find_max(lst): Знаходить максимальний елемент у списку. Виконати без використання функції max().
find_min(lst): Знаходить мінімальний елемент у списку. Виконати без використання функції min().
average(lst): Обчислює середнє значення елементів у списку. Якщо список складається з рядків - вивести помилку.
remove_duplicates(lst): Видаляє дублікати зі списку але не змінює його тип даних.
reverse_list(lst): Повертає список у зворотному порядку.
filter_even(lst): Повертає новий список, що містить тільки парні числа.

'''