"""
Розширте функцію greet_message, додавши новий необовʼязковий аргумент language,
 за допомогою якого можна вказати бажану мову повідомлення. За замовчуванням функція буде
 повертати повідомлення англійською мовою. Додайте привітання на наступних мовах:
українська;
польська;
німецька.
	Кожна мова повинна відображати культурні особливості та коректно виводити імʼя та прізвище.
	 Розгляньте можливість включення додаткових виразів або фраз, що є типовим для відповідної мови.
	Додайте валідацію, яка перевіряє, чи введене значення для аргументу language є одним
	 з підтримуваних(українська, польська, німецька) та виводить рядок про помилку, якщо мова не є коректною,
	 та використовуйте англійську мову як за замовчуванням.

"""


def greet_message(first_name, last_name, language="en"):
   # видаляєм пробіли на початку і в кінці
   first_name = first_name.strip()
   last_name = last_name.strip()


   # щоб не було пусте значення
   if not first_name or not last_name:
       return "Помилка: Ім'я та прізвище не можуть бути пустими."


   # щоб були літери
   if not any(c.isalpha() for c in first_name) or not any(c.isalpha() for c in last_name):
       return "Помилка: Ім'я та прізвище повинні містити хоча б одну літеру."


   # перевірка імя
   if not first_name.replace(" ", "").replace("-", "").isalpha():
       return "Помилка: Ім'я повинно містити тільки літери, пробіли або дефіси."


   # Перевірка прізвища
   if not last_name.replace("-", "").isalpha():
       return "Помилка: Прізвище повинно містити тільки літери або дефіс."


   # Форматуємо ім'я: кожне слово або частину через дефіс з великої літери
   formatted_first_name = " ".join(word.capitalize() for word in first_name.split(" "))
   formatted_first_name = "-".join(word.capitalize() for word in formatted_first_name.split("-"))


   # Форматуємо прізвище (дозволяємо подвійні через дефіс)
   formatted_last_name = "-".join(word.capitalize() for word in last_name.split("-"))


   # Валідація мови
   supported_languages = ['en', 'ua', 'pl', 'de']
   if language not in supported_languages:
       language = 'en'  # якщо немає мови буде англійська як база


   # Привітання на різних мовах
   greetings = {
       'en': f"Hello world! My name is {formatted_first_name} {formatted_last_name}",
       'ua': f"Привіт, світ! Мене звати {formatted_first_name} {formatted_last_name}",
       'pl': f"Cześć, świecie! Nazywam się {formatted_first_name} {formatted_last_name}",
       'de': f"Hallo Welt! Mein Name ist {formatted_first_name} {formatted_last_name}"
   }


   return greetings[language]


# дані від користувача
language = input("Choose your preferred language (en/ua/pl/de): ").lower()
first_name = input("Введіть імʼя: ")
last_name = input("Введіть прізвище: ")


# функцію запускає
result = greet_message(first_name, last_name, language)
print(result)



"""
# Викликаємо функцію для числа та виводимо результат
result_num = descending_order(num)
print(result_num)
"""
"""
first_name = input("Введіть ваше ім'я: ")
last_name = input("Введіть ваше прізвище: ")



def greet_message(first_name, last_name):

    if not first_name.strip() or not last_name.strip():
        return "Помилка: Ім'я та прізвище не можуть бути пустими."

    if not any(c.isalpha() for c in first_name) or not any(c.isalpha() for c in last_name):
        return "Помилка: Ім'я та прізвище повинні містити хоча б одну літеру."

    #Забезпечте, щоб введені значення завжди починаються з великої літери,
    #а всі інші символи були з маленької літери, незалежно від формату введення.

    last_name1 = last_name.capitalize()
    first_name1 = first_name.capitalize()

    return print(f"Hello world! My name is {first_name1} {last_name1}")

result = greet_message(first_name, last_name)

"""




"""
def greet_message():
    import re

    first_name = input("Введіть ваше ім'я: ")
    last_name = input("Введіть ваше прізвище: ")
    language = input("Оберіть мову (англійська, українська, польська, німецька): ")

    # Перевірка, чи ім'я та прізвище не пусті та містять хоча б одну літеру
    if not first_name or not last_name:
        return "Помилка: Ім'я та прізвище не можуть бути пустими."

    if not re.match(r'^[A-Za-zА-Яа-яЁёЇїІіЄєҐґ -]+$', first_name) or not re.match(r'^[A-Za-zА-Яа-яЁёЇїІіЄєҐґ -]+$',
                                                                                  last_name):
        return "Помилка: Ім'я та прізвище повинні містити тільки літери."

    # Форматування імені та прізвища
    def format_name(name: str) -> str:
        return "-".join(word.capitalize() for word in name.split("-")) if "-" in name else " ".join(
            word.capitalize() for word in name.split())

    first_name = format_name(first_name)
    last_name = format_name(last_name)

    greetings = {
        "англійська": f"Hello world! My name is {first_name} {last_name}.",
        "українська": f"Привіт, світ! Мене звати {first_name} {last_name}.",
        "польська": f"Cześć świecie! Mam na imię {first_name} {last_name}.",
        "німецька": f"Hallo Welt! Mein Name ist {first_name} {last_name}."
    }

    return greetings.get(language,
                         "Помилка: Непідтримувана мова. Використовується англійська." + "\n" + greetings["англійська"])


def descending_order():
    number = input("Введіть число: ")

    if not number.isdigit():
        return "Помилка: Введене значення повинно бути невід'ємним цілим числом."

    return int("".join(sorted(number, reverse=True)))


# Приклади використання
print(greet_message())
print(descending_order())

"""
"""
def addition(first_number, second_number):
    return first_number + second_number

def subtraction(first_number, second_number):
    return first_number - second_number

def multiplication(first_number, second_number):
    return first_number * second_number

def division(first_number, second_number):
    if second_number == 0:
        return "Помилка: друге число дорівнює 0"
    return first_number / second_number

def power(first_number, second_number):
    return first_number ** second_number


def perform_calculation():
    first_number = float(input("Введіть перше число: "))
    second_number = float(input("Введіть друге число: "))
    action = input("Введіть дію яку потрібно виконати (+, -, *, /, **): ")

    if action == "+":
        result = addition(first_number, second_number)
    elif action == "-":
        result = subtraction(first_number, second_number)
    elif action == "*":
        result = multiplication(first_number, second_number)
    elif action == "/":
        result = division(first_number, second_number)
    elif action == "**":
        result = power(first_number, second_number)
    else:
        print("такої дії не існує")

    print(f"{first_number} {action} {second_number} = {result}")

#perform_calculation()

def ask_continue():
    response = input("Хочете продовжити (так/ні)? ").strip().lower()
    return response == "так"

def main():
    while True:
        perform_calculation()
        if not ask_continue():
            print("Дякуємо за використання калькулятора!")
            break

main()
"""