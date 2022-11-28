"""
Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому
времени года относится месяц (зима, весна, лето, осень). Напишите решения через
list и через dict.
"""

month = int(input('Введите номер месяца: '))
# list
seasons_l = ['Зима', 'Весна', 'Лето', 'Осень']
if month in (1, 2, 12):
    print(seasons_l[0])
elif month in (3, 4, 5):
    print(seasons_l[1])
elif month in (6, 7, 8):
    print(seasons_l[2])
elif month in (9, 10, 11):
    print(seasons_l[3])
else:
    print('Такого месяца не существует')
# dict
seasons_d = {
    'Зима': (1, 2, 12),
    'Весна': (3, 4, 5),
    'Лето': (6, 7, 8),
    'Осень': (9, 10, 11)
}
for key in seasons_d.keys():
    if month in seasons_d[key]:
        print(key)
