"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента, и
возвращает сумму наибольших двух аргументов.
"""

def my_func(arg_1, arg_2, arg_3):
    num_list = [arg_1, arg_2, arg_3]
    num_list.remove(min(num_list))
    return sum(num_list)

print(f'Сумма двух наибольших чисел = {my_func(8, 3, 5)}')