# --------------------- Дескрипторы атрибутов ---------------------------------


class NonNegative:

    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Не может быть отрицательным")
        instance.__dict__[self.my_attr] = value

    def __delete__(self, instance):
        del instance.__dict__[self.my_attr]

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Road:
    _length = NonNegative()
    _width = NonNegative()
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


OBJ = Road(20, 5000)
print(OBJ.mass())

OBJ._length = 10
OBJ._width = 5000
print(OBJ.mass())
print(OBJ.__class__.__class__)
