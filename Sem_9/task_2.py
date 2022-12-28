"""Функция, сравнивающая списки"""


def my_func(*args):
    my_list = [0, 1, 2, 3, 4, 5]
    new_list = [i for i in range(6)]
    return my_list == new_list
