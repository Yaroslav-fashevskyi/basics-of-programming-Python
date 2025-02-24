import math

def sqrt_math(num_1, num_2):
    sqrt_num = math.sqrt(num_1)
    return f"Квадратний корінь першого введеного числа {sqrt_num}"

def pow(num_1, num_2):
    pow_num = math.pow(num_1, num_2)
    return f"Піднесли перше число до степення другого числа {pow_num}"

def log_math(num_1, num_2):
    log_num = math.log(num_2, num_1)
    return f"Логарифм числа {num_2} за основою {num_1} дорівнює {log_num}"

def factorial(num_1, num_2):
    factorial_math = math.factorial(num_2)
    return f"Факторіал другого введеного числа {factorial_math}"

num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter another number: "))

print(sqrt_math(num_1, num_2))
print(pow(num_1, num_2))
print(log_math(num_1, num_2))
print(factorial(num_1, num_2))

'''

Створіть програму, в якій використовується модуль math для розв’язання певних математичних виразів.
 Весь код має бути організований у функціях(def). 
 Користувач вводить 2 цілих числа і програма повинна обрахувати:
квадратний корінь першого введеного числа.
піднесення першого введеного числа до степеня другого введеного числа.
логарифм другого введеного числа за основою першого введеного числа.
факторіал другого введеного числа.
	
Для цього імпортуйте з модуля math такі функції як sqrt(), pow(), log() та factorial().

'''