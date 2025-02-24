en_text = input("Введіть будь-який текст на англійській мові: ")

clean_en_text = en_text.replace(" ",'')
print(clean_en_text)
print("Кількість всіх символів: ",len(clean_en_text))
letters_text = ' '.join(en_text) .title()
clean_a = letters_text.replace("A",'*')
clean_e = clean_a.replace("E",'*')
clean_i = clean_e.replace("I",'*')
clean_o = clean_i.replace("O",'*')
clean_u = clean_o.replace("U",'*')
clean_y = clean_u.replace("Y",'*')
clean_full = clean_y.replace(" ",'')


print(clean_full)




'''
Створіть програму, яка запитує у користувача будь-який текст на англійській мові і:
Видаляє всі зайві пробіли (на початку, в кінці, між словами);
Виводить кількість символів у цьому рядку;
Перетворює всі голосні літери ('a', 'e', 'i', 'o', 'u', ‘y’) на зірочку (*);
Виводить результат у верхньому регістрі.

'''