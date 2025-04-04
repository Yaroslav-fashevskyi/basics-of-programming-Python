class Good:
    name = 'Cheese'
    weight = 156
    category = 'Foods'
    price = 450

Good.price = 1000
Good.count = 10

if __name__ == "__main__":
    print("name:", Good.name)
    print("weight:", Good.weight)
    print("category:", Good.category)
    print("price:", Good.price)
    print("count:", Good.count)
