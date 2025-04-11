class Clock:
    def __init__(self, time):
        self.__time = 0 # приватна змінна ізначеннячасу
        self.set_time(time)

    def __check_time(self, time):
        return isinstance(time, int) and 0 <= time < 100000

    def set_time(self, time):
        if self.__check_time(time):
            self.__time = time
        else:
            print("Неправильне значення часу!")

    def get_time(self):
        return self.__time # час який зараз поточний поверне

if __name__ == "__main__":
    clock = Clock(0)
    clock.set_time(1000000)
    clock.set_time(8212)
    print("Поточний час:", clock.get_time())

