import string

def is_all_letters(user_input):
    for char in user_input:
        if char not in string.ascii_letters and not char.isspace():
            return "1. Всі символи - літери: Ні"
    return "1. Всі символи - літери: Так"

def capitalize_words(user_input):
    return f"2. Текст з великими літерами: {user_input.title()}"
# https://www.w3schools.com/python/ref_string_title.asp

def remove_punctuation(user_input):
    result = ""
    for char in user_input:
        if char not in string.punctuation:
            result += char
    return f"3. Текст без пунктуації: {result}"
# !"#$%&'()*+, -./:;<=>?@[\]^_`{|}~
# https://www.geeksforgeeks.org/string-punctuation-in-python/
def count_vowels(user_input):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for char in user_input:
        if char in vowels:
            vowel_count += 1
    return f"4. Кількість голосних: {vowel_count}"


user_input = input("Введіть текст: ")

print(is_all_letters(user_input))
print(capitalize_words(user_input))
print(remove_punctuation(user_input))
print(count_vowels(user_input))




'''
Створіть програму, яка використовує модуль string для роботи з текстовими даними. Весь код має бути організований у функціях (def). Програма повинна:
Перевірити, чи всі символи у введеному користувачем рядку є літерами.
Перетворити введений користувачем текст у формат, де кожне слово починається з великої літери.
Видалити всі символи пунктуації з введеного рядка.
Порахувати кількість голосних літер у тексті.
Для цього імпортуйте з модуля string такі атрибути як ascii_letters та punctuation.
Приблизний вигляд результату роботи програми:
1. Всі символи - літери: Ні
2. Текст з великими літерами: Привіт Як Твої Справи
3. Текст без пунктуації: Привіт як твої справи
4. Кількість голосних: 8

'''