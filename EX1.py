import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    is_frosen = False

    @unittest.skipIf(is_frosen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        qwerty_1 = Runner('Лёша')
        for _ in range(10):
            qwerty_1.walk()
        dist1 = qwerty_1.distance
        self.assertEqual(dist1, 50)

    @unittest.skipIf(is_frosen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        qwerty_2 = Runner('Юрка')
        for _ in range(10):
            qwerty_2.run()
        dist2 = qwerty_2.distance
        self.assertEqual(dist2, 100)

    @unittest.skipIf(is_frosen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        qwerty_3 = Runner('Соня')
        qwerty_4 = Runner('Семён')
        for _ in range(10):
            qwerty_3.run()
            qwerty_4.walk()
        self.assertEqual(qwerty_3.distance, qwerty_4.distance,)