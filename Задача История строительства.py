# Домашняя работа по уроку "Различие атрибутов класса и экземпляра"

# Задача "История строительства"
# Для решения этой задачи будем пользоваться решением к предыдущей задаче "Перегрузка операторов".
#
# В классе House создайтеатрибут houses_history = [], который будет хранить названия созданных обьектов.
#
# Правильней вписывать здание в историю сразу при создании обьекта, тем более можно удобно обращаться к атрибутам класса
# используя ссылку на сам класс - cls.
# Дополните метод __new__ так, чтобы:
# Название обьекта добавлялось в список cls.houses_history.
# Названия строяния можно взять из args по индексу
#
# Также переопределите метод __del__(self) в котором будет выводиться строка:
# "<название> снесён, но он останется в истории"
#
# Создайте несколько обьектов класса House и проверьте работу методов __del__ и __new__,
# а также значение атрибута houses_history.


class House:
    houses_history = []     # атрибут будет хранить названия созданных объектов

    def __new__(cls, *args, **kwargs): # ,*args, **kwargs
        cls.houses_history.append(args[0])
        print(*cls.houses_history)
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
       self.name = name
       self.number_of_floors = number_of_floors

    def __len__(self):
         return self.number_of_floors
    def __str__(self):
       title = str(f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')
       return title

    def __eq__(self, other):    # 1
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):    # 2
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def __del__(self):
        print(self.name, ' снесён, но он останется в истории')

hightower = House('Башня', 12)
warehouse = House('Склад', 4)

print(hightower)
print(warehouse)

del warehouse
print(House.houses_history[0], '- первое здание')
print(House.houses_history[-1], '- последнее здание')
del hightower
print(House.houses_history, '- список зданий')