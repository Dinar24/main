# Домашнее задание по теме "Форматирование строк".

"""
Задание:
Создайте новый проект или продолжайте работу в текущем проекте.
Напишите код, который форматирует строки для следующих сценариев.
Укажите переменные, которые должны быть вставлены в каждую строку:
"""

# Использование %
team1 = 'Мастера кода'
team2 = 'Волшебники данных'


def num(team1_num=0, team2_num=0):  # количество участников команды
    print('В команде %s участников: %s !' % (team1, team1_num))
    print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))

# Использование format:

score1 = 0
score2 = 0


def time(team1_time=0, team2_time=0, tasks_total=0):  # количество решенных задач
    time1 = team1_time
    time2 = team2_time

    print('Команда {} решила задач: {}!'.format(team2, score2))
    print('{} решили задачи за {} сек. !'.format(team2, time2))


# Использование f-строк

def challenge_result(tasks_total=0, time_avg=0):
    print(f'Команды решили {score1} и {score2} задач')
    if score1 > score2:
        print(f'Резултат битвы: победа команды {team1} !')
    else:
        print(f'Резултат битвы: победа команды {team2} !')

    print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секудны на задачу')


num(team1_num=6, team2_num=6)
score1 = 40
score2 = 42
time(team1_time=1552.512, team2_time=2153.31451)
# time_avg = 45.2
challenge_result(tasks_total=82, time_avg=45.2)

import os
import time

directory = "."
for root, dirs, files in os.walk(directory):
    for file in files:
        file_path = os.path.join(root, file)
        file_time = os.path.getmtime(file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(file_time))
        file_size = os.path.getsize(file)
        parent_dir = os.path.dirname(os.getcwd())
        print(f'Обнаружен файл: {file}, Путь: {file_path}, Размер: {file_size} байт, Время изменения: {formatted_time},'
              f' Родительская директория:{parent_dir}')