rows = int(input("Введіть кількість рядків (не менше 3): "))
cols = int(input("Введіть кількість стовпців (не менше 3): "))

if rows < 3 or cols < 3:
    print("Розміри матриці повинні бути не менше 3x3.")
else:
    matrix = [[j + i * cols + 1 for j in range(cols)] for i in range(rows)]
    for row in matrix:
        for element in row:
            print(element, end=' ')
        print()



'''
Потрібно написати програму, яка виводитиме вже створену матрицю довільного розміру(від 3х3)
 в консоль за допомогою вкладеного циклу for.

'''

