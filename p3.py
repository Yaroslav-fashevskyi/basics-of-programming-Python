class Book:
    def __init__(self, author, title, price):
        self.__author = author
        self.__title = title
        self.__price = price

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_price(self, price):
        self.__price = price

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_price(self):
        return self.__price

if __name__ == "__main__":
    book1 = Book("Ідеальний шторм", "Дірк Райнгардт", 400)
    book2 = Book("Джордж Орвелл", "1984", 349)
    book3 = Book("US Army", "Посібник рейнджера", 599)

    print("Book 1: Автор:", book1.get_author(), ", Назва:", book1.get_title(), ", Ціна:", book1.get_price())
    print("Book 2: Автор:", book2.get_author(), ", Назва:", book2.get_title(), ", Ціна:", book2.get_price())
    print("Book 3: Автор:", book3.get_author(), ", Назва:", book3.get_title(), ", Ціна:", book3.get_price())

    book1.set_price(555)
    book2.set_title("1984 - 2")
    book3.set_author("by US Army")

    print("Після змін:")
    print("Book 1: Автор:", book1.get_author(), ", Назва:", book1.get_title(), ", Ціна:", book1.get_price())
    print("Book 2: Автор:", book2.get_author(), ", Назва:", book2.get_title(), ", Ціна:", book2.get_price())
    print("Book 3: Автор:", book3.get_author(), ", Назва:", book3.get_title(), ", Ціна:", book3.get_price())
