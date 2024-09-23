import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []  # Список для сохранения всех результатов

    def setUp(self):
        pass  # Убираем ненужные бегуны из setUp, перемещаем в тесты

    def test_race_1(self):
        runners = [
            Runner("Усэйн", speed=10),
            Runner("Ник", speed=8)
        ]
        tournament = Tournament(90, *runners)  # Запуск соревнования на 90 единиц
        results = tournament.start()

        expected = {1: "Усэйн", 2: "Ник"}
        for place, runner in results.items():  # Проверка результатов
            self.assertEqual(str(runner), expected[place])

        self.all_results.append(results)

    def test_race_2(self):
        runners = [
            Runner("Андрей", speed=10),
            Runner("Ник", speed=8)
        ]
        tournament = Tournament(90, *runners)
        results = tournament.start()

        expected = {1: "Андрей", 2: "Ник"}
        for place, runner in results.items():
            self.assertEqual(str(runner), expected[place])

        self.all_results.append(results)  # Сохранение результатов

    def test_race_3(self):
        runners = [
            Runner("Андрей", speed=10),
            Runner("Усэйн", speed=9),
            Runner("Ник", speed=8)
        ]
        tournament = Tournament(90, *runners)
        results = tournament.start()

        expected = {1: "Андрей", 2: "Усэйн", 3: "Ник"}
        for place, runner in results.items():
            self.assertEqual(str(runner), expected[place])

        self.all_results.append(results)  # Сохранение результатов

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            print({place: str(runner) for place, runner in result.items()})  # Вывод результатов в словарь


if __name__ == '__main__':
    unittest.main()
