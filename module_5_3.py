class House: 															# создаем класс  House с двумя обьектами
	def __init__(self, name, number_of_floors):
			if not isinstance(number_of_floors, (int, House)):
				raise TypeError(
					"\n___!!!___Значение должно быть целочисленным___!!!___")
			self.name = name 											# создаем в классе объект для названия дома
			self.number_of_floors = number_of_floors 					# создаем в классе объект количества этажей
		
	def __len__(self): 													# подсчет значения
		return self.number_of_floors
		
	def __str__(self): 													# возвращение строки для вывода
		return f'Название: {self.name}, количество этажей: {self.number_of_floors}'
		
	def __eq__(self, other): 											# проверка равенства
		return int(self.number_of_floors) == int(self.number_of_floors)
	
	def __add__(self, value): 											# прибавление значения
		if not isinstance(value, (int, House)):
			raise ArithmeticError(
				"\n___!!!___Значение должно быть целочисленным___!!!___")
		value_ = value if isinstance(value, int) else print("значение переменной value = str")	
		self.number_of_floors = self.number_of_floors + value_
		return self
		
	def __iadd__(self, value): 											# подстановка значения
		if not isinstance(value, (int, House)):
			raise ArithmeticError(
				"\n___!!!___Значение должно быть целочисленным___!!!___")
		value_ = value if isinstance(value, int) else print("значение переменной value = str")
		self.number_of_floors += value_
		return self
		
	def __radd__(self, value): 											# обратное прибавление
		if not isinstance(value, (int, House)):
			raise ArithmeticError(
				"\n___!!!___Значение должно быть целочисленным___!!!___")
		value_ = value if isinstance(value, int) else print("значение переменной value = str")	
		self.number_of_floors = value_ + self.number_of_floors
		return self		
				
	def __gt__(self, other):
		return int(self.number_of_floors) > int(other.number_of_floors)		
	def __ge__(self, other):
		return int(self.number_of_floors) >= int(other.number_of_floors)		
	def __lt__(self, other):
		return int(self.number_of_floors) < int(other.number_of_floors)		
	def __le__(self, other):
		return int(self.number_of_floors) <= int(other.number_of_floors)		
	def __ne__(self, other):
		return int(self.number_of_floors) != int(other.number_of_floors)		
				
	def go_to(self, new_floor): 										# создаем функцию с параметром выбора этажа
		if int(new_floor) < 1 or int(new_floor) > self.number_of_floors:
			print('Такого этажа не существует')
		else:
			floor_i = 0 												# создаем вспомогательную переменную для "перебора" этажей
			while floor_i < int(new_floor): 							# "перебор" этажей
				floor_i += 1
				print(floor_i)

		
h1 = House('ЖК Эльбрус', 10) 		# присваиваем имени класс с конкретными значениями оюбектов
h2 = House('ЖК Акация', 20)
#h1.go_to(5) 											# подставляем параметр этажа для вывода по выделенному дому
#h2.go_to(10)

#____str____
print("___str___")
print(h1)
print(h2)

#__len__
print("\n___len___")
print(len(h1))
print(len(h2))

print("\n___eq___")
print(h1 == h2) # __eq__

print("\n___add___")
h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

print("\n___iadd___")
h1 += 10 # __iadd__
print(h1)

print("\n___radd___")
h2 = 10 + h2 # __radd__
print(h2)

print('\n___compare____')	
print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
