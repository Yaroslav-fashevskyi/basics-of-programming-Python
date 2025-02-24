name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
account_balance = float(input("Enter your account balance: "))

print("Name: {name}, Age: {age}, Balance: ${account_balance}".format(name=name, age=age, account_balance=account_balance))




'''
Напишіть програму, яка приймає три різні значення: ім'я (рядок), вік (ціле число) 
та баланс рахунку (число з плаваючою точкою), і повертає форматований рядок типу:
 "Name: John, Age: 25, Balance: $154.30". Для форматування ви повинні використати метод format().
'''