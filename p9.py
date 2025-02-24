name = input("Введіть ваше ім'я: ")
phone = input("Введіть ваш номер телефону у форматі XXXXXXXXXX: ")
email = input("Введіть ваш email: ")

name_up = name.upper()

formatted_phone = f"+38 ({phone[:3]}) {phone[3:6]}-{phone[6:8]}-{phone[8:]}"

print(f"NAME: {name_up}, PHONE: {formatted_phone}, EMAIL: {email}")
'''

Створіть програму, яка приймає від користувача ім'я, телефонний номер і email та:
Перетворює ім'я на великі літери;
Форматує номер телефону так, щоб він мав вигляд: +38 (XXX) XXX-XX-XX;
Виводить результат у форматі: "NAME: [ІМ'Я], PHONE: [НОМЕР], EMAIL: [EMAIL]"
	Номер телефону при вводі ОБОВʼЯЗКОВО вказуйте в форматі XXXXXXXXXX.

'''