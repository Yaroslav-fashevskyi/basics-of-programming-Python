def greet_students(greeting, *names):
    if not names:
        print(f"Немає студентів для привітання")
    else:
        for name in names:
            print(f"{greeting}, {name}!")

if __name__ == "__main__":
    greet_students("Привіт")
    greet_students("Привіт", "Олег")
    greet_students("Привіт", "Юля", "Олег", "Аліна")