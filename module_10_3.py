from random import randint
import threading, logging, time
from threading import Thread, Lock


lock = Lock()


class Bank:
	def __init__(self):
		self.balance = 0
		# print('init')

	def deposit(self):
		# print('deposit')
		transaction = 1
		while transaction <= 100:
			value_ = randint(50, 500)
			self.balance = self.balance + value_
			if self.balance > 500 and lock.locked() == True:
				lock.release()
			# print('deposit', transaction, value_)
			else:
				print(f'Пополнение: {value_}. Баланс: {self.balance}.')
				# print('___deposit transaction___', transaction)
			transaction = transaction + 1
			time.sleep(0.001)

	def take(self):
		transaction = 1
		while transaction <= 100:
			value_ = randint(50, 500)
			print(f'Запрос на снятие {value_}')
			if value_ <= self.balance:
				balance = self.balance - value_
				print(f'Снятие {value_}. Баланс: {self.balance}')
			elif value_ > self.balance:
				print(f'Запрос отклонён, недостаточно средств')
				lock.acquire()
			transaction = transaction + 1
			time.sleep(0.001)
			# print('___take transaction___', transaction - 1)


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
