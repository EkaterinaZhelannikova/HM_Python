"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор
натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент
с тем же значением должен разместиться после них
"""

my_list = [7, 5, 3, 3, 2]
print(f'"Рейтинг" {my_list}')
number = int(input('Введите новый элемент рейтинга: '))
for element in my_list:
    if number in my_list:
        my_list.insert(my_list.index(number), number)
        break
    else:
        if number > element:
            my_list.insert(my_list.index(element), number)
            break
        elif number < my_list[len(my_list) - 1]:
            my_list.append(number)
            break
print(my_list)