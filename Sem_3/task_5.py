"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом. При
нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод
чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел
будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится
специальный символ, выполнение программы завершается. Если специальный символ
введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к
полученной ранее сумме и после этого завершить программу.
"""

sum_res = 0
off = False
while off is not True:
    numbers = input('Введите числа через пробел или "q" чтобы выйти: ').split()
    res = 0
    for el in numbers:
        if el in ['q', 'Q']:
            off = True
            break
        else:
            res += int(el)
    sum_res += res
    print(f'Сумма чисел: {sum_res}')
