from memory_profiler import profile
from sys import getsizeof
from numpy import array
from copy import deepcopy
"""
Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры памяти,
оптимизировать, вновь выполнить замеры и ОПИСАТЬ СЛОВАМИ, что вы сделали и
чего удалось добиться
"""

"""Реализовать формирование списка, используя функцию range().
В список должны войти четные числа от 100 до 1000 (включая границы).
"""

my_list1 = [el for el in range(100, 1001) if el % 2 == 0]

my_list2 = array(range(100, 1001, 2))

"""
Список заполняется с помощью генератора.
memory = 3704 bytes
"""
print(f'{getsizeof(my_list1)} bytes')

"""
Создается массив при помощи библиотеки numpy, которая значительно экономит 
место:
memory ~ 1916 bytes
"""
print(f'{getsizeof(my_list2)} bytes')

# -----------------------------------------------------------------------------

"""Функции, заполняющие список значениями от 0 до 100. Выполняющие копирование
списка и умножающие каждый элемент на себя."""

@profile
def func_1():
    """Выделяет дополнительную пaмять, не освобождается"""
    x = [num for num in range(100000)]
    y = list(map(lambda i: i * i, deepcopy(x)))
    return y


func_1()
"""
Line #    Mem usage    Increment  Line Contents
=============================================================
    37     34.5 MiB     34.5 MiB  @profile
    38                            def func_1():
    39                            '''Выделяет дополнительную пaмять, не освобождается'''
    40     38.6 MiB      4.1 MiB  x = [num for num in range(100000)]
    41     43.6 MiB      5.1 MiB  y = list(map(lambda i: i * i, deepcopy(x)))
    42     43.6 MiB      0.0 MiB   return y
"""


@profile
def func_2():
    """Выделяет допольнительную память, освобождается"""
    x = [num for num in range(100000)]
    y = list(map(lambda i: i * i, deepcopy(x)))
    del x
    y = None
    return y


func_2()
""""
Line #    Mem usage    Increment  Line Contents
=============================================================
    58     36.8 MiB     36.8 MiB  @profile
    59                            def func_2():
    60                            '''Выделяет допольнительную память, освобождается'''
    61     39.2 MiB      2.3 MiB  x = [num for num in range(100000)]
    62     44.5 MiB      5.3 MiB  y = list(map(lambda i: i * i, deepcopy(x)))
    63     41.9 MiB     -2.6 MiB  del x
    64     38.2 MiB     -3.7 MiB  y = None
    65     38.2 MiB      0.0 MiB  return y
"""
