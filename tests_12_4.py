import unittest
import logging
import rt_with_exceptions


class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        print('test_walk запущен')
        try:
        	test_volume = 50
        	test_name = "NoName_1"
        	test_speed = 5
        	import_runner_ = rt_with_exceptions.Runner(test_name, test_speed)
        	test_walk_ = [import_runner_.walk() for i in range(10)]
        	self.assertEqual(import_runner_.distance, test_volume)  # 1-функ., кот. тестим, 2-с чем сравниваем
        	logging.info('"test_walk"выполнен успешно')
        except ValueError as err:
        	logging.warning("Неверная скорость для Runner", exc_info=True)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        print('test_run запущен')
        test_volume = 100
        #test_name = "NoName_2"
    	test_name = [3]
        try:
        	import_runner_ = rt_with_exceptions.Runner(test_name)
        	test_run_ = [import_runner_.run() for i in range(10)]
        	self.assertEqual(import_runner_.distance, test_volume)  # 1-функ., кот. тестим, 2-с чем сравниваем
        	logging.info('"test_run"выполнен успешно')
        except TypeError as err:
        	logging.debug("Неверная скорость для Runner", exc_info=True)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        test_name_1 = "NoName_1"
        test_name_2 = "NoName_2"
        import_runner_1 = rt_with_exceptions.Runner(test_name_1)
        import_runner_2 = rt_with_exceptions.Runner(test_name_2)
        test_walk_ = [import_runner_1.walk() for i in range(10)]
        test_run_ = [import_runner_2.run() for i in range(10)]
        self.assertNotEqual(import_runner_1.distance, import_runner_2.distance)

if __name__ == '__main__':
	logging.basicConfig(level=logging.INFO, filemode='w', filename= "_test_log.log", format="%(asctime)s | %(levelname)s | %(message)s")
	unittest.main()
