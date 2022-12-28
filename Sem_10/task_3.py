# Создать метакласс для паттерна Синглтон
from threading import Lock
import copy


class Singleton(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Matrix(metaclass=Singleton):

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str('\n'.join('\t'.join([str(i) for i in j])
                             for j in self.matrix))


lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
M_OBJ = Matrix(lst)
M_OBJ_1 = Matrix()
print(M_OBJ)
print()
print(M_OBJ_1)
print()
print(M_OBJ is M_OBJ_1)
