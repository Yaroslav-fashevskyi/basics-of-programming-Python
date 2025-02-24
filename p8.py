text_input = input("Введіть рядок: ")
change_text = text_input.replace(' ', '@')

modified_text = (
    change_text
    .replace('a', '4')
    .replace('e', '3')
    .replace('i', '1')
    .replace('o', '0')
    .replace('u', '/')
    .replace('y', '+')
    .replace('A', '4')
    .replace('E', '3')
    .replace('I', '1')
    .replace('O', '0')
    .replace('U', '*')
    .replace('Y', '-')
)

modified_up_text = modified_text.capitalize()
modified_up_last_text = modified_up_text[:-1] + modified_up_text[-1].upper()

print("Результат:", modified_up_last_text)

'''
Напишіть програму, яка приймає від користувача рядок, виконує наступні дії:
Видаляє всі пробіли і заміняє їх на любий спеціальний символ;
Замінює голосні на відповідні числа: a → 4, e → 3, i → 1, o → 0;
Додайте також свій приклад заміни символів для кращого захисту пароля;
Перетворює першу та останню літеру в рядку на великі літери;
Виводить результат.

'''