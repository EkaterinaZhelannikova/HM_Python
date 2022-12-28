# --------------------- Дескрипторы атрибутов ---------------------------------


class TypeProperty:

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr

    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]

    def __set__(self, instance, value):
        instance.__dict__[self.my_attr] = type(value)


class Worker:
    name = TypeProperty()
    surname = TypeProperty()
    position = TypeProperty()
    wage = TypeProperty()
    bonus = TypeProperty()

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self.wage + self.bonus


OBJ = Worker('Игорь', 'Иванов', 'инженер', 80000, 20000)
print(OBJ.__dict__)
print(OBJ.__class__.__class__)
