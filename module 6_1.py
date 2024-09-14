# Родительский класс Animal
class Animal:
    def __init__(self, name):
        self.alive = True   # Живое по умолчанию
        self.fed = False    # Не накормлено по умолчанию
        self.name = name    # Имя животного

    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f"{self.name} съел {food.name}")
                self.fed = True  # Животное накормлено
            else:
                print(f"{self.name} не стал есть {food.name}")
                self.alive = False  # Животное погибло
        else:
            print(f"{self.name} не может есть {food}")

# Родительский класс Plant
class Plant:
    def __init__(self, name):
        self.edible = False  # Не съедобно по умолчанию
        self.name = name     # Имя растения

# Класс Mammal, наследник от Animal
class Mammal(Animal):
    pass  # Другие специфические атрибуты и методы можно добавить здесь

# Класс Predator, наследник от Animal
class Predator(Animal):
    pass  # Другие специфические атрибуты и методы можно добавить здесь

# Класс Flower, наследник от Plant
class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = False  # Цветок несъедобен

# Класс Fruit, наследник от Plant
class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True  # Фрукт съедобен

# Тестирование
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

# Вывод информации
print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)

# Попытка поесть
a1.eat(p1)  # Волк с Уолл-Стрит пытается съесть Цветик семицветик (несъедобно)
a2.eat(p2)  # Хатико съедает Заводной апельсин (съедобно)

# Состояние после еды
print(a1.alive)
print(a2.fed)
