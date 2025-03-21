from functools import wraps

def sum_list(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        numbers = func(*args, **kwargs)
        return sum(numbers)
    return wrapper

@sum_list
def get_list(s):
    result = []
    for i in s.split():
        result.append(int(i))
    return result

if __name__ == "__main__":
    print(get_list("10 20 30 40"))

