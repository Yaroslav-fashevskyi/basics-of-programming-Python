class Car:
    mark = 'Volkswagen'
    model = 'Passat B5'
    weight = 2500000
    price = 7000

if __name__ == "__main__":
    mark_value = getattr(Car, 'mark', False)
    model_value = getattr(Car, 'model', False)

    print("mark:", mark_value)
    print("model:", model_value)


    setattr(Car, 'color', 'blue')
    delattr(Car, 'weight')

    print("Атрибути класу Car:", end=" ")
    for attr in dir(Car):
        if not attr.startswith("__"):
            print(getattr(Car, attr), end=" ")
    print()

#dir() щоб побачити всі атрибути клас
#etattr() щоб значення атрибутта отримати