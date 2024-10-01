from random import randint
import queue, time
from threading import Thread


class Table:
	def __init__(self, number):
		self.number = number
		self.guest = None

	
class Guest(Thread):
	def __init__(self, name):
		super().__init__()
		self.name = name

	def run(self):
		model_waiting = randint(3, 10)
		time.sleep(model_waiting)


class Cafe:
	def __init__(self, *tables):
		self.queue = queue.Queue() # очередь
		self.tables = tables
	
	def guest_arrival(self, *guests):
		# self.guests = guests  - строка лишняя, так как объекты не создаются, а передаются
		for guest in guests:
			for table in self.tables:
				if table.guest is None:
					guest.start()
					print(f'{guest.name} сел(-а) за стол номер {table.number}')
					table.guest = guest
					break
			else:
				print(f'{guest.name} в очереди')
				self.queue.put(guest)

	def discuss_guests(self):
		while not self.queue.empty() or any([table.guest for table in self.tables]):
			for table in self.tables:
				if table.guest is not None and not table.guest.is_alive():
					print(f'{table.guest.name} за столом {table.number} покушал(-а) и ушёл(ушла)')
					print(f'Стол номер {table.number} свободен')
					table.guest = None
				if not self.queue.empty() and table.guest is None:
					table.guest = self.queue.get()
					print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
					table.guest.start()


# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()