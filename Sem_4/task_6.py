"""
 Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание,
что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении
числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие, при
котором повторение элементов списка будет прекращено.
"""

# итератор, генерирующий целые числа, начиная с указанного

from itertools import count
from itertools import cycle


start_num = int(input('Введите начальное число: '))
stop_num = int(input('Введите конечное число: '))

for el in count(start_num):
    if el > stop_num:
        break
    else:
        print(el)

# итератор, повторяющий элементы некоторого списка, определенного заранее

my_list = [7, 'cat']
repeat = int(input('Введите количество повторений элементов списка: '))
c = 0

for el in cycle(my_list):
    if c == repeat:
        break
    print(el)
    c += 1
