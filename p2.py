def log_calls(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            log_entry = f"Функція {func.__name__} викликана з аргументами {args}, результат: {result}\n"
            with open(filename, 'a', encoding="utf-8") as file:
                file.write(log_entry)
            return result
        return wrapper
    return decorator

@log_calls("log.txt")
def multiply(a, b):
    return a * b

if __name__ == '__main__':
    print(multiply(1, 2))
    print(multiply(2, 3))
    print(multiply(3, 4))
    print(multiply(5, 6))
    print(multiply(7, 8))
    print(multiply(9, 10))




