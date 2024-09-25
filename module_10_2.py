from threading import Thread
import time


# Создание класса
class Knight(Thread):
	def __init__(self, name, power):
		super().__init__()
		self.name = name
		self.power = power
	
	def run(self):
		enemy = 100		
		# step = enemy / self.power
		day = 1
		days = 0
		print(f'{self.name}, на нас напали!')	
		while enemy >= 0:
			enemy = enemy - self.power
			time.sleep(day)
			days = days + day
			if enemy == 0:
				print(f'{self.name} одержал победу спустя {days} дней (дня)!')
				break
			print(f'{self.name} сражается {days} дня (дней), осталось {enemy} воинов.')


# Определение объектов
# Исполнение 1
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Исполнение 2
knights = {'Sir Lancelot': 10, 'Sir Galahad': 20}

print(f'Запуск потоков и остановка текущего')
print(f'__Исполнение 1 кода запуска___')
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print(f'\n__Исполнение 2 кода запуска___')
threads = []
for name in knights.keys():
	power = knights.get(name)
	thread = Knight(name, power)
	thread.start()
	threads.append(thread)

for thread in threads:
	thread.join()
