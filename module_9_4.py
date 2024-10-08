# Lamda-функция:
print('lambda-функция:')
first = 'Мама мыла раму'
second = 'Рамёна мала было'

Matching_letters = list(map(lambda x, y: x == y, first, second))
print(Matching_letters)
print()

# Замыкание:
print('Замыкание')


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:
            for i in data_set:
                file.write(f'{i}\n')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['A', 'это', 'уже', 'число', 5, 'в', 'списке'])
with open('example.txt', 'r', encoding='utf-8') as file:
    print(file.read())
print()

# Метод __call__
from random import choice

print('Метод __call__')


class MysticBall:

    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())