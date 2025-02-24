text = input("Введіть рядок (слаг): ")
result = ""
i = 0

while i < len(text):
    if text[i] == '-':
        if i == 0 or text[i-1] != '-':
            result += '-'
    else:
        result += text[i]
    i += 1
print("Результат:", result)
