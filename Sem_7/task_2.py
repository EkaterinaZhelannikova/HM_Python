"""
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина),
width (ширина). Значения данных атрибутов должны передаваться при создании
экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета
массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длинаширинамасса асфальта для покрытия одного кв метра
дороги асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу метода.
"""


class Road:
    # масса асфальта для покрытия 1 кв/м
    _weight_sqm: int = 25
    # толщина полотна
    _thickness: int = 5

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        return self._length * self._width \
               * self._thickness * self._weight_sqm / 1000


r = Road(20, 5000)
print(r.mass())
