"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем
нуля в качестве делителя программа должна корректно обработать эту ситуацию и
не завершиться с ошибкой.
"""


class NullError(Exception):
    def __init__(self, *args):
        self.my_list = []


try:
    divident = int(input('Введите делимое: '))
    divisor = int(input('Введите делитель: '))
    if divisor == 0:
        raise NullError("На ноль делить нельзя!")
except ValueError:
    print("Вы ввели не число")
except NullError as err:
    print(err)
else:
    print(f'Результат деления: {divident / divisor}')
