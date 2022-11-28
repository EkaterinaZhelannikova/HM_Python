"""
Создать список и заполнить его элементами различных типов данных. Реализовать
скрипт проверки типа данных каждого элемента. Использовать функцию type() для
проверки типа. Элементы списка можно не запрашивать у пользователя, а указать
явно, в программе.
"""

my_int = 7
my_float = 10.13
my_str = 'cat'
my_list = [3, 'wow', 1.6]
my_dict = {'Hello': 'Привет'}
my_tuple = (1, 'cat', 2.34)
a = None
final_list = [my_int, my_float, my_str, my_list, my_dict, my_tuple, a]
for el in final_list:
    print(f'{el} is {type(el)}')
