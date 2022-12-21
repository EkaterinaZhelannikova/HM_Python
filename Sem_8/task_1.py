"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
[[], [], []]
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода add() для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
"""
import copy


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str('\n'.join('\t'.join([str(i) for i in j])
                             for j in self.matrix))

    def __add__(self, other):
        res = copy.deepcopy(self.matrix)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                res[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(res)


list_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(Matrix(list_1))
print()
print(Matrix(list_1) + Matrix(list_2))
