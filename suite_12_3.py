import unittest
from module_12_1_test_for_testSuit import RunnerTest  # импортируем тест RunnerTest
from module_12_2_test_for_testSuit import TournamentTest  # импортируем тест TournamentTest

runner_test = unittest.TestSuite()  # создаем сборку для тест-кейсов

runner_test.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))  # добавляем тест-кейс в набор
runner_test.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))  # добавляем тест-кейс в набор

runner_ = unittest.TextTestRunner(verbosity=2)
runner_.run(runner_test)
