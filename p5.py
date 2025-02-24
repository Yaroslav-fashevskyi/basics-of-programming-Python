UAH_Input = float(input("Введіть суму в грн: "))

EUR_UAH = 46.5
USD_UAH = 41.6

EUR_exchange = UAH_Input/EUR_UAH
USD_exchange = UAH_Input/USD_UAH



print("Введене значення: ",UAH_Input,"грн")
print("1$ =", USD_UAH ,"грн")
print("1€ =", EUR_UAH,"грн")
print(UAH_Input,"грн =",EUR_exchange,"EUR")
print(UAH_Input,"грн =",USD_exchange,"USD")



'''Напишіть програму для конвертації гривні(UAH) в 
американський долар(USD) та євро(EUR) з використанням актуальних курсів обміну. 
Актуальні курси Ви можете знайти в Інтернеті. 
В результаті роботи програма повинна виводити в консоль значення,
 введене користувачем, актуальний курс валют та конвертувати суму.'''