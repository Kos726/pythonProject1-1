from unittest import TestCase
import Runner


class RunnerTest(TestCase):
	
	def test_walk(self):
		test_volume = 50
		test_name = "NoName_1"
		import_runner_ = Runner.Runner(test_name)
		test_walk_ = [import_runner_.walk() for i in range(10)]
		self.assertEqual(import_runner_.distance, test_volume)  # 1-функ., кот. тестим, 2-с чем сравниваем

	def test_run(self):
		test_volume = 100
		test_name = "NoName_2"
		import_runner_ = Runner.Runner(test_name)
		test_run_ = [import_runner_.run() for i in range(10)]
		self.assertEqual(import_runner_.distance, test_volume)  # 1-функ., кот. тестим, 2-с чем сравниваем
		
	def test_challenge(self):
		test_name_1 = "NoName_1"
		test_name_2 = "NoName_2"
		import_runner_1 = Runner.Runner(test_name_1)
		import_runner_2 = Runner.Runner(test_name_2)
		test_walk_ = [import_runner_1.walk() for i in range(10)]
		test_run_ = [import_runner_2.run() for i in range(10)]
		self.assertNotEqual(import_runner_1.distance, import_runner_2.distance)

"""
if __name__ == '__main__':
	unittest.main()"""
