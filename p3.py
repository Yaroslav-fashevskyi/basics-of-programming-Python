"""
Напишіть функцію create_user(), яка приймає параметри username та password і повертає словник,
 що представляє нового користувача по заданим параметрам.
	Напишіть декоратор validate_input(), який перевіряє, чи передані дані проходять наступним критеріям:
довжина username більше 3 символів і значення є рядковим типом;
довжина password більше 6 символів і значення є рядковим типом.
Придумайте і додайте додатково ще 3 перевірки.

"""


def validate_input(func):
    def wrapper(username, password):
        if not isinstance(username, str) or len(username) <= 3:
            return "Username повинен бути рядком і мати більше 3 символів"
        if not isinstance(password, str) or len(password) <= 6:
            return "Password повинен бути рядком і мати більше 6 символів"
        if ' ' in username:
            return "Username не повинен містити пробіли"
        if ' ' in password:
            return "Password не повинен містити пробіли"
        if not any(char.isdigit() for char in password):
            return "Password повинен містити хоча б одну цифру"
        return func(username, password)

    return wrapper


@validate_input
def create_user(username, password):
    return {"username": username, "password": password}


if __name__ == "__main__":
    print(create_user("yaroslav", "12345678"))



