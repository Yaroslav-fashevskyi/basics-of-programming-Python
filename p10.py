print("Будь ласка, введіть три оцінки за проект (від 1 до 10):")
execution_time = int(input("Оцінка за час виконання: "))
quality = int(input("Оцінка за якість роботи: "))
requirements_compliance = int(input("Оцінка за відповідність вимогам: "))


if not all(1 <= grade <= 10 for grade in [execution_time, quality, requirements_compliance]):
    print("Всі оцінки повинні бути в діапазоні від 1 до 10.")
else:

    if execution_time >= 7 and quality >= 7 and requirements_compliance >= 7:
        print("Проект успішно виконано")


    if (execution_time < 7) or (quality < 7) or (requirements_compliance < 7):
        count_above_5 = sum(grade > 5 for grade in [execution_time, quality, requirements_compliance])
        if count_above_5 >= 2:
            print("Проект потрібно доопрацювати")


    if (execution_time < 5) + (quality < 5) + (requirements_compliance < 5) >= 2:
        print("Проект провалено")

'''
Напишіть програму, яка запитує три оцінки за проект користувача: час виконання,
 якість роботи та відповідність вимогам (введи оцінки від 1 до 10, уточніть це користувачу). Виконайте наступні перевірки:
Якщо всі оцінки більше або дорівнюють 7 — вивести "Проект успішно виконано".
Якщо одна або більше оцінок менша за 7, але хоча б дві з них більше 5 — вивести "Проект потрібно доопрацювати".
Якщо дві або більше оцінок менші за 5 — вивести "Проект провалено".'''