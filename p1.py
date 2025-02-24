def calculate_total_price(name: str, price_per_item: float, quantity: int = 1, discount: float = 0):
    total_price = price_per_item * quantity
    discount_amount = total_price * (discount / 100)
    final_price = total_price - discount_amount
    return f"Продукт: {name}, Кількість: {quantity}, Загальна вартість: {final_price} грн (зі знижкою {discount}%)."


print(calculate_total_price("/32 IPv4 subnet", 250, 5))
print(calculate_total_price("/31 IPv4 subnet", 500, 2, discount=10))

'''
Завдання 1.
Напишіть функцію calculate_total_price, яка приймає три параметри:
name (str): назва продукту (обов'язковий параметр);
price_per_item (float): вартість одного продукту (обов'язковий параметр);
quantity (int): кількість продуктів (необов'язковий параметр, за замовчуванням 1);
Функція має повертати рядок, що описує назву продукту і загальну вартість покупки.
Якщо кількість не вказана, то вважається, що користувач купує один продукт.
Розширте функцію calculate_total_price, щоб вона приймала ще один додатковий параметр:
discount (float): відсоток знижки на загальну вартість (необов'язковий параметр, за замовчуванням 0).
Тепер функція має обчислювати загальну вартість з урахуванням кількості продуктів та застосованої знижки. 
У вихідному рядку виводьте кінцеву вартість покупки.

'''