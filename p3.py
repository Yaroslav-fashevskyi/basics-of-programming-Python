def cache_results(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            print("Результат з кешу: ", args)
            return cache[args]
        print("Обчислюємо результат для: ", args)
        result = func(*args)
        cache[args] = result
        return result

    return wrapper

@cache_results
def multiply(a, b):
    return a * b


if __name__ == "__main__":

    print(multiply(2, 3))
    print(multiply(2, 3))
    print(multiply(4, 5))
    print(multiply(4, 5))
