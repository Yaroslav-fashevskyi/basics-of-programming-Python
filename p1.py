def calculate_average(*args):
    list = []
    for number in args:
        list.append(number)
    if len(list) == 0:
        return 0
    average_value = sum(list) / len(list)
    return average_value


if __name__ == '__main__':
    print(calculate_average(2, 4, 6))
    print(calculate_average(1, 3, 5, 7, 9))
    print(calculate_average())
