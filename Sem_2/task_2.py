"""
Для списка реализовать обмен значений соседних элементов, т.е. значениями
обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве
элементов последний сохранить на своем месте. Для заполнения списка элементов
необходимо использовать функцию input().
"""

my_l = input('Введите элементы списка: ').split()
my_l[:-1:2], my_l[1::2] = my_l[1::2], my_l[:-1:2]
print(my_l)