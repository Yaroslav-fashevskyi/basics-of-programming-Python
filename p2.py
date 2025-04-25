class Car:
    def __init__(self, brand: str, model: str, year: int, speed: float, power: float, color: str):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__speed = speed
        self.__power = power
        self.__color = color
        self.__driver = None  # Спочатку водія немає

    def set_driver(self, driver):
        self.__driver = driver

    def get_driver(self):
        return self.__driver

    def get_speed(self):
        return self.__speed

    def get_power(self):
        return self.__power

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_color(self):
        return self.__color

    def info(self):
        return f"{self.__brand} {self.__model} ({self.__year}, {self.__color})"


class Driver:
    def __init__(self, name: str, age: int, driving_experience: int):
        self.__name = name
        self.__age = age
        self.__driving_experience = driving_experience

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_driving_experience(self):
        return self.__driving_experience


class Race:
    # Метод, що проводить гонку між двома автомобілями та повертає переможця (як кортеж: (car, driver))
    def start_race(self, car1: Car, car2: Car):
        # Отримуємо досвід водія, якщо водій встановлений; інакше приймаємо його рівним 0
        driver1 = car1.get_driver()
        exp1 = driver1.get_driving_experience() if driver1 is not None else 0
        score1 = 0.5 * car1.get_speed() + 0.3 * car1.get_power() + 0.2 * exp1

        driver2 = car2.get_driver()
        exp2 = driver2.get_driving_experience() if driver2 is not None else 0
        score2 = 0.5 * car2.get_speed() + 0.3 * car2.get_power() + 0.2 * exp2

        print(f"Результат гонки:\n - {car1.info()} зі шкалою {score1}\n - {car2.info()} зі шкалою {score2}")

        if score1 > score2:
            return (car1, driver1)
        elif score2 > score1:
            return (car2, driver2)
        else:
            return None  # Нічия

    # Метод для виведення інформації про переможця
    def print_winner(self, winner):
        if winner is None:
            print("Гонка завершилась нічиєю!")
        else:
            car, driver = winner
            if driver is not None:
                print(f"Переможець: {car.info()} з водієм {driver.get_name()}")
            else:
                print(f"Переможець: {car.info()}")



if __name__ == "__main__":
    print("=== Система автогонок ===")

    car1 = Car("Tesla", "Y", 2022, 262, 300, "Black")
    car2 = Car("Tesla", "X", 2023, 269, 320, "White")


    driver1 = Driver("Олег", 18, 15)
    driver2 = Driver("Ярослав", 18, 10)


    car1.set_driver(driver1)
    car2.set_driver(driver2)


    race = Race()
    winner = race.start_race(car1, car2)
    race.print_winner(winner)
