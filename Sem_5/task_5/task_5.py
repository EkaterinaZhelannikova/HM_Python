"""
Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и
выводить ее на экран.
"""


def sum_num():
    try:
        with open('task_5.txt', 'w+') as f_obj:
            line = input('Введите цифры через пробел: ')
            f_obj.writelines(line)
            my_num = line.split()

            print(f'Сумма чисел в файле: {sum(map(int, my_num))}')
    except ValueError:
        print('Неверный ввод')

sum_num()
