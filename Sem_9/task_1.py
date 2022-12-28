"""Функция нахождения суммы чисел n + nn + nnn"""


def sum_num(n):
    temp = str(n)
    n1 = temp + temp
    n2 = temp + temp + temp
    total = n + int(n1) + int(n2)
    return total
