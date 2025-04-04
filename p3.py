class Person:
    first_name = "Ivan"
    last_name = "Ivanov"
    age = 30
    date_of_birth = "1995-01-01"

person = Person()

if __name__ == "__main__":
    print("Чи є атрибут first_name у об'єкті person?")
    print(hasattr(person, 'first_name'))
