# Домашняя работа по уроку "Атрибуты и методы обьекта."

# Задача "Developer - не только разработчик":

# Реалезуйте класс House, обьекты которого будут создаваться следующим образом:
# House('ЖК Эльбрус', 30)
# Обьект этого класса должен обладать следующими атрибутами:
# self_name - имя, self.number_of_floors - кол-во этажей
# Также должен обладать методом go_to(new_floor), где new_floor - номер этажа(int), на который нужно приехать.
# Метод go_to выводит на экран(в консоль) значения от 1 до new_floor(включительно).
# Если же new_floor больше чем self.number_of_floors или меньше 1, то вывести строку "Такогоэатажа не существует".
# Пункты задачи:
# 1 Создайте класс House.
# 2 Внутри класса House определите метод в который передатите название и кол-во этажей
# 3 Внутри метода __init__ создайте атрибуты обьекта self.name и self.number_of_floors, присвойте им переданные значения.
# 4 Создайте метод go_to с параметром new_floor и напишите логику внутри него на основе описания задачи.
# 5 Создайте обьект класса House с произвольным названием и количеством этажей.
# 6 Вызовите метод у этого обьекта с произвольным числом.

class House:
    def __init__ (self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        floor = 0
        print(f'Здание{self.name} имеет {self.number_of_floors} этажей \nПоднимаемся на{new_floor}-й')
        if new_floor < 1 or new_floor > self.number_of_floors:
            print(f'{new_floor} - такого этажа не существует')
        else:
            for floor in range(new_floor):
                print(floor +1)


hightower = House('Башня', 12)
warehouse = House('Склад', 4)

hightower.go_to(9)
warehouse.go_to(-1)