"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно
данные. При этом английские числительные должны заменяться на русские. Новый
блок строк должен записываться в новый текстовый файл.
"""

rus = ('Один', 'Два', 'Три', 'Четыре')

with open("task_4.txt", encoding='utf-8') as my_f:
    lines = my_f.readlines()

numbers = [int(line[-2]) for line in lines if line != '\n']
numbers_rus = "\n".join(f'{rus[n - 1]} - {n}' for n in numbers)

with open("task_4_rus.txt", 'w', encoding='utf-8') as new_f:
    new_f.write(numbers_rus)
