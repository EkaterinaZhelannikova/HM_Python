"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет
оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней
величины дохода сотрудников.
"""

with open('task_3.txt', encoding='utf-8') as my_f:
    workers = my_f.readlines()

sum_salary = 0

for worker in workers:
    name, salary = worker.split()
    salary = float(salary)
    sum_salary += salary
    if salary < 20000:
        print(name)

print('Средняя величина дохода: ', round(sum_salary / len(workers), 2))

