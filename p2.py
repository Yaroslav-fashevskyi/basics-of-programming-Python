class Money:
    def __init__(self, money):
        self.__money = 0
        self.set_money(money)

    def __check_money(self, money):
        return isinstance(money, int) and money >= 0 #параметр money має бути цілим числом, більшим або рівним нулю.

    def set_money(self, money):
        if self.__check_money(money):
            self.__money = money
        else:
            print("Неправильне значення коштів!")

    def get_money(self):
        return self.__money #повертає баланс який зараз

    def add_money(self, money_obj):
        if isinstance(money_obj, Money):
            self.__money += money_obj.get_money()
        else:
            print("Обєкт не є типу money")


if __name__ == "__main__":
    money1 = Money(10)
    money2 = Money(20)

    money1.set_money(100)
    money2.add_money(money1)
    print("money1:", money1.get_money())
    print("money2:", money2.get_money())
