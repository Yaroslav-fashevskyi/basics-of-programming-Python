price = float(input("Введіть вартість однієї книги: "))
num_books = 2
prices = []

while num_books <= 10:
    total_price = round(price * num_books, 2)
    prices.append(total_price)
    num_books = num_books + 1

print(" ".join(map(str, prices)))





'''
Вводиться вартість однієї книги price гривень (дійсне число).
 Необхідно вивести на екран у рядок через пробіл вартості 2, 3, ... 10 таких книг із точністю до десятих. 
 Для округлення десятків використайте функцію round(). Програму реалізувати за допомогою циклу while та for.
'''