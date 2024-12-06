class House:											# создаем класс  House с двумя обьектами
	def __init__(self, name, number_of_floors):
		self.name = name 								# создаем в классе объект для названия дома
		self.number_of_floors = number_of_floors 		# создаем в классе объект количества этажей
		
	def __len__(self): 									# подсчет значения
		return self.number_of_floors
		
	def __str__(self): 									# возвращение строки для вывода
		return f'Название: {self.name}, количество этажей: {self.number_of_floors}'
		
	def go_to(self, new_floor): 						# создаем функцию с параметром выбора этажа
		if int(new_floor) < 1 or int(new_floor) > self.number_of_floors:
			print('Такого этажа не существует')
		else:
			floor_i = 0 								# создаем вспомогательную переменную для "перебора" этажей
			while floor_i < int(new_floor): 			# "перебор" этажей
				floor_i += 1
				print(floor_i)

h1 = House('ЖК Эльбрус', 10) 		# присваиваем имени класс с конкретными значениями оюбектов
h2 = House('ЖК Акация', 20)
#h1.go_to(5) 											# подставляем параметр этажа для вывода по выделенному дому
#h2.go_to(10)

#____str____
print(h1)
print(h2)

#__len__
print(len(h1))
print(len(h2))
