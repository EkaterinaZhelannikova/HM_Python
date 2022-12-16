from timeit import timeit
from math import factorial
"""
Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры времени,
оптимизировать, вновь выполнить замеры и ОПИСАТЬ СЛОВАМИ, что вы сделали и
чего удалось добиться
"""

"""Функции, которые принимают три позиционных аргумента, и возвращают сумму
наибольших двух аргументов."""


def my_func1(arg_1, arg_2, arg_3):
    num_list = [arg_1, arg_2, arg_3]
    num_list.remove(min(num_list))
    return sum(num_list)


def my_func2(arg1, arg2, arg3):
    if arg1 > arg3 and arg2 > arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3


"""
В функции my_func1 используется метод remove, который удаляет из списка
минимальный аргумент и обновляет список. 
time ~ 0.24946110000018962
"""
print(timeit('my_func1(4, 5, 8)', globals=globals(), number=1000000))
"""
В функции my_func2 используется условный оператор if, который сравнивает все 
агрументы между собой и возвращет результат. 
Удалось добиться значительного уменьшения времени:
time ~ 0.06576850000055856
"""
print(timeit('my_func2(4, 5, 8)', globals=globals(), number=1000000))

# -----------------------------------------------------------------------------

"""Функции, которые возвращают факториал числа n."""


def fact1(n):
    i = 1
    res = 1
    while i <= n:
        res *= i
        i += 1
    return res


def fact2(n):
    return factorial(n)


"""
В функции fact1 используется цикл while, который выполняет одну и ту же 
последовательность действий, пока не выполнится условие.
time ~ 0.16962169999987964
"""
print(timeit('fact1(4)', globals=globals(), number=1000000))
"""
В функции fact2 используется библиотека math, с помощью которой удалось 
добиться оптимизации кода и значительного уменьшения времени:
time ~ 0.05092010000043956
"""
print(timeit('fact2(4)', globals=globals(), number=1000000))