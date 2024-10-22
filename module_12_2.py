import unittest
from Runner import Runner, Tournament


class TournamentTest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.all_results = {}

	def setUp(self):
		# Прямой порядок, скорость ниже дистанции
		self.runner_1 = Runner('Усэйн', 10)
		self.runner_2 = Runner('Андрей', 6)
		self.runner_3 = Runner('Ник', 3)
		# Обратный порядок, скорость выше дистанции
		self.runner_4 = Runner('Усэйн-2', 95)
		self.runner_5 = Runner('Андрей-2', 97)
		self.runner_6 = Runner('Ник-2', 100)

	@classmethod
	def tearDownClass(cls):
		for value in cls.all_results.values():
			print(f'{value}')
		
	def test_challenge_1(self):
		self.test_1_results = {}
		self.challenge_1 = Tournament(90, self.runner_1, self.runner_3)
		self.result_1 = self.challenge_1.start()
		self.test_1_results[1] = self.result_1.get(1).name
		self.test_1_results[2] = self.result_1.get(2).name
		self.all_results['test challenge 1'] = self.test_1_results
		self.assertTrue('Ник' in str(self.result_1.get(2).name), "Ошибка")
		time_1 = 1 / self.runner_1.speed
		time_3 = 1 / self.runner_3.speed
		if time_1 < time_3:
			winner = self.runner_1
		else:
			winner = self.runner_3
		print('Проверка на корректность кода логики определения победителя')
		self.assertEqual(winner, str(self.result_1.get(1).name))

	def test_challenge_2(self):
		self.test_2_results = {}
		self.challenge_2 = Tournament(90, self.runner_2, self.runner_3)
		self.result_2 = self.challenge_2.start()
		self.test_2_results[1] = self.result_2.get(1).name
		self.test_2_results[2] = self.result_2.get(2).name
		self.all_results['test challenge 2'] = self.test_2_results
		self.assertTrue('Ник' in str(self.result_2.get(2).name), "Ошибка")
		time_2 = 1 / self.runner_2.speed
		time_3 = 1 / self.runner_3.speed
		if time_2 < time_3:
			winner = self.runner_2
		else:
			winner = self.runner_3
		print('Проверка на корректность кода логики определения победителя')
		self.assertEqual(winner, str(self.result_2.get(1).name))

	def test_challenge_3(self):
		self.test_3_results = {}
		self.challenge_3 = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
		self.result_3 = self.challenge_3.start()
		self.test_3_results[1] = self.result_3.get(1).name
		self.test_3_results[2] = self.result_3.get(2).name
		self.test_3_results[3] = self.result_3.get(3).name
		self.all_results['test challenge 3'] = self.test_3_results
		self.assertTrue('Ник' in str(self.result_3.get(3).name), "Ошибка")
		time_1 = 1 / self.runner_1.speed
		time_2 = 1 / self.runner_2.speed
		time_3 = 1 / self.runner_3.speed
		if time_1 < time_2 and time_1 < time_3:
			winner = self.runner_1
		elif time_2 < time_1 and time_2 < time_3:
			winner = self.runner_2
		else:
			winner = self.runner_3
		print('Проверка на корректность кода логики определения победителя')
		self.assertEqual(winner, str(self.result_3.get(1).name))

	# Тесты с обратным порядком. повторяют тесты прямого порядка, но параметры другие
	def test_challenge_4(self):
		self.test_4_results = {}
		self.challenge_4 = Tournament(90, self.runner_4, self.runner_6)
		self.result_4 = self.challenge_4.start()
		self.test_4_results[1] = self.result_4.get(1).name
		self.test_4_results[2] = self.result_4.get(2).name
		self.all_results['test challenge 4'] = self.test_4_results
		self.assertTrue('Ник-2' in str(self.result_4.get(2).name), "Ошибка")
		time_1 = 1 / self.runner_4.speed
		time_3 = 1 / self.runner_6.speed
		if time_1 < time_3:
			winner = self.runner_4
		else:
			winner = self.runner_6
		print('Проверка на корректность кода логики определения победителя')
		self.assertEqual(winner, str(self.result_4.get(1).name))

	def test_challenge_5(self):
		self.test_5_results = {}
		self.challenge_5 = Tournament(90, self.runner_5, self.runner_6)
		self.result_5 = self.challenge_5.start()
		self.test_5_results[1] = self.result_5.get(1).name
		self.test_5_results[2] = self.result_5.get(2).name
		self.all_results['test challenge 5'] = self.test_5_results
		self.assertTrue('Ник-2' in str(self.result_5.get(2).name), "Ошибка")
		time_2 = 1 / self.runner_5.speed
		time_3 = 1 / self.runner_6.speed
		if time_2 < time_3:
			winner = self.runner_5
		else:
			winner = self.runner_6
		print('Проверка на корректность кода логики определения победителя')
		self.assertEqual(winner, str(self.result_5.get(1).name))

	def test_challenge_6(self):
		self.test_6_results = {}
		self.challenge_6 = Tournament(90, self.runner_4, self.runner_5, self.runner_6)
		self.result_6 = self.challenge_6.start()
		self.test_6_results[1] = self.result_6.get(1).name
		self.test_6_results[2] = self.result_6.get(2).name
		self.test_6_results[3] = self.result_6.get(3).name
		self.all_results['test challenge 6'] = self.test_6_results
		self.assertTrue('Ник-2' in str(self.result_6.get(3).name), "Ошибка")
		time_1 = 1 / self.runner_4.speed
		time_2 = 1 / self.runner_5.speed
		time_3 = 1 / self.runner_6.speed
		if time_1 < time_2 and time_1 < time_3:
			winner = self.runner_4
		elif time_2 < time_1 and time_2 < time_3:
			winner = self.runner_5
		else:
			winner = self.runner_6
		print('Проверка на корректность кода логики определения победителя')
		self.assertEqual(winner, str(self.result_6.get(1).name))


if __name__ == '__main__':
	unittest.main()
