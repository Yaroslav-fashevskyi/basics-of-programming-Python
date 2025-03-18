def tagging(tag="h1"):
    def decorator(func):
        def wrapper(text):
            return f"<{tag}>{func(text)}</{tag}>"
        return wrapper
    return decorator

@tagging("h1")
def to_lowercase(text):
    return text.lower()

if __name__ == "__main__":
    print(to_lowercase("PYTHON"))
