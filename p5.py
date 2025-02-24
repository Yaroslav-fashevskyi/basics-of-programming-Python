text = input("Введіть текст: ")
text_to_list = list(text)
replace_text = text.replace("-", " ")
print(replace_text)
print("Створений список: ", text_to_list)
print("Кількість символів A: ", replace_text.count('A'))
text_convert = replace_text.replace(" ", "")
text_convert_list = list(text_convert)
print("Кожна друга літера у списку: ", text_convert_list[0::2])
joined_text = ''.join(text_convert_list)
print("Новий рядок зі списку літер: ", joined_text)
'''
Напишіть програму, в якій користувач вводить рядкове значення
 “K-I-N-G-D-A-N-Y-L-O-U-N-I-V-E-R-S-I-T-Y”. Вам потрібно:
1. За допомогою рядкового метода replace() замінити всі “-“ на пробіли.
2. За допомогою функції list() створити список з введеного раніше рядка.
3. Знайти і вивести кількість символів "A" в рядку.
4. Виведіть на екран кожну другу літеру зі списку.
5. За допомогою рядкового методу join() з'єднайте всі літери зі списку, щоб отримати новий рядок.

'''