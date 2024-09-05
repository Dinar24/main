# Домашняя работа по уроку "Спецтальные методы классов"

# Задача "Магичесие здания":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче "Атрибуты и методы обьекта".
#
# Необходимо дополнить класс House следующими специальными методами:
# 1 __len__(self) - должен возвращать кол-во этажей здания
# 2 __str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>"


class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
            title = str(f'Название: {self.name}, кол-во этажей: {self.number_of_floors} ')
            return title

hightower = House('Башня', 12)
warehouse = House('Склад', 4)

print(hightower)
print(warehouse)


print(len(hightower))
print(len(warehouse))