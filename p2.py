import datetime

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print("Марка:", self.brand, "| Модель:", self.model, "| Рік випуску:", self.year)

    def change_model(self, new_model):
        self.model = new_model

    def calculate_age(self):
        current_year = datetime.datetime.now().year
        return current_year - self.year

if __name__ == '__main__':
    car = Car("Tesla", "X", 2016)

    print("Інформація про автомобіль:")
    car.display_info()
    print("Вік автомобіля:", car.calculate_age())


    car.change_model("3")
    print("Після зміни моделі:")
    car.display_info()
