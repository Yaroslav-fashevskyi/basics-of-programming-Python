
def sort_list(items: list, descending: bool = False, separator: str = ',', unique: bool = False, max_items: int = None):
    if unique:
        items = list(set(items))
    items.sort(reverse=descending)
    if max_items is not None:
        items = items[:max_items]
    return separator.join(map(str, items))

print(sort_list([1, 3, 8, 3, 1], descending=True))
print(sort_list([1, 3, 8, 3, 1], separator=' | '))
print(sort_list([1, 3, 7, 3, 1], unique=True))
print(sort_list([1, 3, 8, 3, 1], unique=True, max_items=3))
print(sort_list([5, 3, 8, 3, 1], unique=True, max_items=3, descending=True))

'''
Напишіть функцію sort_list, яка приймає три параметри:
items (list): список елементів для сортування (обов'язковий параметр).
descending (bool): параметр, що визначає порядок сортування (необов'язковий параметр, за замовчуванням False, тобто сортування за зростанням).
separator (str): символ, що використовується для розділення елементів в рядку результату (необов'язковий параметр, за замовчуванням - кома).
Функція має повертати рядок з відсортованими елементами, розділеними вказаним розділювачем.
Розширте функцію sort_list, додавши ще два параметри:
unique (bool): прапорець, що вказує, чи потрібно видаляти дублікати з вихідного списку (необов'язковий параметр, за замовчуванням False).
max_items (int): максимальна кількість елементів у відсортованому списку (необов'язковий параметр, за замовчуванням None, що означає, що всі елементи включаються).
Функція має видаляти дублікати з початкового списку, якщо unique=True, сортувати його та обмежувати кількість елементів у кінцевому результаті до значення max_items, якщо це значення вказано.

'''