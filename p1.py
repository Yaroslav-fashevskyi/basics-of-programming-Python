class User:
    def __init__(self, name: str, surname: str, age: int):
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__accounts = []  # Список банківських рахунків користувача

    # Метод для додавання нового банківського рахунку
    def add_account(self, account) -> None:
        self.__accounts.append(account)

    # Гетери для отримання даних користувача
    def get_name(self) -> str:
        return self.__name

    def get_surname(self) -> str:
        return self.__surname

    def get_age(self) -> int:
        return self.__age

    def get_accounts(self) -> list:
        return self.__accounts


class BankAccount:
    __account_counter = 1000000  # Початкове значення лічильника номерів рахунків

    def __init__(self, owner: User, initial_balance: float):
        self.__account_number = BankAccount.__account_counter
        BankAccount.__account_counter += 1  # Автоматичне збільшення номера рахунку
        self.__balance = initial_balance
        self.__owner = owner

    # Метод для поповнення рахунку
    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.__balance += amount
            print(f"Поповнено рахунок №{self.__account_number} на суму {amount}. Новий баланс: {self.__balance}")
        else:
            print("Сума поповнення повинна бути додатною.")

    # Метод для зняття коштів
    def withdraw(self, amount: float) -> None:
        if amount > self.__balance:
            print("Недостатньо коштів для зняття!")
        elif amount <= 0:
            print("Сума зняття повинна бути додатною.")
        else:
            self.__balance -= amount
            print(f"Знято {amount} з рахунку №{self.__account_number}. Новий баланс: {self.__balance}")

    # Гетер для отримання балансу
    def get_balance(self) -> float:
        return self.__balance

    # Гетер для отримання номера рахунку
    def get_account_number(self) -> int:
        return self.__account_number

    # Гетер для отримання власника рахунку
    def get_owner(self) -> User:
        return self.__owner


class BankSystem:
    # Створення нового користувача
    def create_user(self, name: str, surname: str, age: int) -> User:
        user = User(name, surname, age)
        print(f"Створено користувача: {name} {surname}, вік: {age}")
        return user

    # Створення нового банківського рахунку для користувача
    def create_account(self, user: User, initial_balance: float) -> BankAccount:
        account = BankAccount(user, initial_balance)
        user.add_account(account)
        print(
            f"Створено банківський рахунок №{account.get_account_number()} для користувача {user.get_name()} {user.get_surname()} з початковим балансом {initial_balance}")
        return account

    # Поповнення рахунку
    def deposit(self, account: BankAccount, amount: float) -> None:
        account.deposit(amount)

    # Зняття коштів з рахунку
    def withdraw(self, account: BankAccount, amount: float) -> None:
        account.withdraw(amount)

    # Переказ коштів між рахунками
    def transfer(self, sender_account: BankAccount, receiver_account: BankAccount, amount: float) -> None:
        if amount <= 0:
            print("Сума переказу повинна бути додатною.")
            return

        if sender_account.get_balance() < amount:
            print("Переказ неможливий: недостатньо коштів на рахунку відправника.")
        else:
            sender_account.withdraw(amount)
            receiver_account.deposit(amount)
            print(
                f"Переказ {amount} з рахунку №{sender_account.get_account_number()} на рахунок №{receiver_account.get_account_number()} виконано.")


if __name__ == "__main__":
    print("=== Система банківських рахунків ===")
    bank_system = BankSystem()
    user1 = bank_system.create_user("Олег", "Олег", 18)
    account1 = bank_system.create_account(user1, 1000)
    bank_system.deposit(account1, 500)
    bank_system.withdraw(account1, 200)
    user2 = bank_system.create_user("Ярослав", "Ярослав", 18)
    account2 = bank_system.create_account(user2, 1500)
    bank_system.transfer(account1, account2, 300)

    print(f"Баланс рахунку {account1.get_account_number()} (користувач {user1.get_name()}): {account1.get_balance()}")
    print(f"Баланс рахунку {account2.get_account_number()} (користувач {user2.get_name()}): {account2.get_balance()}")
