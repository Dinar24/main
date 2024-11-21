import asyncio
import time


async def start_strongman(name, power):
    """
    Асинхронная функция имитирует соревнование по поднятию шаров Атласа
    :param name: Имя силача
    :param power: Его подъемная мощность (прямопропорциональна времени выполнения)

    """
    print(f'Силач {name}, начал соревнование.')
    start = time.time()
    for i in range(1, 6):
        await asyncio.sleep(10 / power)
        print(f'Силач {name}, поднял {i} шар')
    end = time.time()
    print(f'Силач {name} закончил соревнование. Время выполнения упражнения: {round(end - start, 2)}')


async def start_tournament():
    """
    Асинхронная функция в которой создается 3 задачи(task1, task2, task3) для функции start_strongman

    """
    task1 = asyncio.create_task(start_strongman('Pasha', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))

    # Каждую задачу ввожу в состояние ожидания
    await task1
    await task2
    await task3

# Запуск асинхронной функции методом run
asyncio.run(start_tournament())
