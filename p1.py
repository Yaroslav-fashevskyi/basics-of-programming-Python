def get_initial_balance():
    # Запитує початковий баланс у користувача
    while True:
        try:
            balance = float(input("Введіть ваш початковий баланс: "))
            if balance > 0:
                return balance
            else:
                print("Баланс має бути додатним числом. Спробуйте ще раз")
        except ValueError:
            print("Будь ласка, введіть числове значення")


def show_menu():
    # Виводить меню банкомата
    print("Оберіть операцію:")
    print("1️⃣ Поповнити рахунок")
    print("2️⃣ Зняти гроші")
    print("3️⃣ Перевірити баланс")
    print("4️⃣ Вийти")


def deposit(balance):
    # Поповнити
    while True:
        try:
            amount = float(input("Введіть суму поповнення: "))
            if amount > 0:
                balance += amount
                print(f"Ваш новий баланс: {balance}")
                return balance
            else:
                print("Сума поповнення повинна бути додатною. Спробуйте ще раз.")
        except ValueError:
            print("Будь ласка, числове значення")


def withdraw(balance):
    # Зняти з рахунку
    while True:
        try:
            amount = float(input("Введіть суму для зняття: "))
            if amount > 0:
                if amount > balance:
                    print("Недостатньо коштів!")
                else:
                    balance -= amount
                    print(f"Ваш новий баланс: {balance}")
                    return balance
            else:
                print("Сума для зняття повинна бути додатною. Спробуйте ще раз.")
        except ValueError:
            print("Будь ласка, числове значення")


def check_balance(balance):
    # Вивести баланс
    print(f"Ваш баланс: {balance}")


def atm():
    # е ну це тип main
    balance = get_initial_balance()

    while True:
        show_menu()
        choice = input("Ваш вибір: ")

        if choice == '1':
            balance = deposit(balance)
        elif choice == '2':
            balance = withdraw(balance)
        elif choice == '3':
            check_balance(balance)
        elif choice == '4':
            print("Дякуємо за використання нашого потужного банкомата!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

atm()
