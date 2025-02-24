import random
random_numbers = []
unique_numbers = set()

for i in range(10):
    random_numbers.append(random.randint(1, 100))

print("Випадкові числа:", random_numbers)


for num in random_numbers:
    unique_numbers.add(num)

sorted_numbers = sorted(unique_numbers)

for num in sorted_numbers:
    print(num)





'''
Потрібно створити список з 10 випадковими числами.
Потрібно конвертувати цей список в множину, використовуючи функцію set() та відсортувати його в порядку зростання. 
Вивести всі елементи множини в консоль(не об’єктом set!).
'''