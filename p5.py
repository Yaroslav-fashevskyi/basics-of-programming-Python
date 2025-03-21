def uppercase(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

def exclaim(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + "!!!"
    return wrapper

@exclaim
@uppercase
def greet(name):
    return f"Привіт, {name}"

@uppercase
@exclaim
def farewell(name):
    return f"До побачення, {name}"

if __name__ == "__main__":
    print(greet("Ярослав"))
    print(farewell("Ярослав"))
