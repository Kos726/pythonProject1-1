class House: 												# создаем класс  House с двумя обьектами
	def __init__(self, name, number_of_floors):
		self.name = name 									# создаем в классе объект для названия дома
		self.number_of_floors = number_of_floors 			# создаем в классе объект количества этажей
		
	def go_to(self, new_floor): 							# создаем функцию с параметром выбора этажа
		if int(new_floor) < 1 or int(new_floor) > self.number_of_floors:
			print('Такого этажа не существует')
		else:
			floor_i = 0 									# создаем вспомогательную переменную для "перебора" этажей
			while floor_i < int(new_floor): 				# "перебор" этажей
				floor_i += 1
				print(floor_i)

		
h1 = House('ЖК Горский', 18) 			# присваиваем имени класс с конкретными значениями объектов
h2 = House('Домик в деревне', 2)
h1.go_to(5) 												# подставляем параметр этажа для его вывода по выделенному дому
h2.go_to(10)
