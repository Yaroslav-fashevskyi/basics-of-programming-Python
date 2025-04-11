import re

class CardCheck:
    @staticmethod
    def check_card_number(card_number):
        pattern = r"^\d{4}-\d{4}-\d{4}-\d{4}-\d{4}$"
        return bool(re.match(pattern, card_number))

    @classmethod
    def check_name(cls, name):
        pattern = r"^[A-Z]+ [A-Z]+$"
        return bool(re.match(pattern, name))

if __name__ == "__main__":
    test_number1 = "4441-1234-5678-9113-1234"
    test_number2 = "1516-1135-2311"
    test_name1 = "YAROSLAV FASHEVSKYI"
    test_name2 = "Yaroslav Fashevskyi"


    print(f"{test_number1}: {CardCheck.check_card_number(test_number1)}")  # True
    print(f"{test_number2}: {CardCheck.check_card_number(test_number2)}")  # False


    print(f"{test_name1}: {CardCheck.check_name(test_name1)}")  # True
    print(f"{test_name2}: {CardCheck.check_name(test_name2)}")  # False

