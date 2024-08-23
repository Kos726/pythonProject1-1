class House: # создаем класс  House с двумя обьектами
	houses_history = []
	def __new__(cls, *args, **kwargs):
		cls.houses_history.append(args[0]) # добавляем элементы в список
		return object.__new__(cls)

	def __init__(self, name, number_of_floors):
			if not isinstance(number_of_floors, (int, House)):
				raise TypeError("\n___!!!___Значение должно быть целочисленным___!!!___")
			self.name = name # создаем в классе объект для названия дома
			self.number_of_floors = number_of_floors # создаем в классе объект количества этажей
		
	def __len__(self): # подсчет значения
		if not isinstance(self.number_of_floors, int):
			raise TypeError("\n___!!!___Значение должно быть целочисленным___!!!___")	
		return self.number_of_floors
		
	def __str__(self): # возвращение строки для вывода
		return f'Название: {self.name}, количество этажей: {self.number_of_floors}'
		
	def __eq__(self, other): # проверка равенства
		if not isinstance(self.number_of_floors, int):
			raise TypeError("\n___!!!___Значение должно быть целочисленным___!!!___")			
		return int(self.number_of_floors) == int(self.number_of_floors)
	
	def __add__(self, value): # прибавление значения
		if not isinstance(value, (int, House)):
			raise ArithmeticError("\n___!!!___Значение должно быть целочисленным___!!!___")
		value_ = value if isinstance(value, int) else print("значение переменной value = str")	
		self.number_of_floors = self.number_of_floors + value_
		return self
		
	def __iadd__(self, value): #подстановеа значенич
		if not isinstance(value, (int, House)):
			raise ArithmeticError("\n___!!!___Значение должно быть целочисленным___!!!___")
		value_ = value if isinstance(value, int) else print("значение переменной value = str")
		self.number_of_floors += value_
		return self
		
	def __radd__(self, value): # обратное прибпвление
		if not isinstance(value, (int, House)):
			raise ArithmeticError("\n___!!!___Значение должно быть целочисленным___!!!___")
		value_ = value if isinstance(value, int) else print("значение переменной value = str")	
		self.number_of_floors = value_ + self.number_of_floors
		return self		
				
	def __gt__(self, other):
		if not isinstance(self.number_of_floors, int):
			raise TypeError("\n___!!!___Значение должно быть целочисленным___!!!___")			
		return int(self.number_of_floors) > int(other.number_of_floors)
				
	def __ge__(self, other):
		if not isinstance(self.number_of_floors, int):
			raise TypeError("\n___!!!___Значение должно быть целочисленным___!!!___")			
		return int(self.number_of_floors) >= int(other.number_of_floors)
				
	def __lt__(self, other):
		if not isinstance(self.number_of_floors, int):
			raise TypeError("\n___!!!___Значение должно быть целочисленным___!!!___")			
		return int(self.number_of_floors) < int(other.number_of_floors)
				
	def __le__(self, other):
		if not isinstance(self.number_of_floors, int):
			raise TypeError("\n___!!!___Значение должно быть целочисленным___!!!___")			
		return int(self.number_of_floors) <= int(other.number_of_floors)
				
	def __ne__(self, other):
		if not isinstance(self.number_of_floors, int):
			raise TypeError("\n___!!!___Значение должно быть целочисленным___!!!___")			
		return int(self.number_of_floors) != int(other.number_of_floors)		
				
	def go_to(self, new_floor): # создаем функцию с параметром выбора этажа
		if not isinstance(self.number_of_floors, int):
			raise TypeError("\n___!!!___Значение должно быть целочисленным___!!!___")
			if int(new_floor) < 1 or int(new_floor) > self.number_of_floors:
				print('Такого этажа не существует')
		else:
			floor_i = 0 # создаем вспомогательную переменную для "перебора" этажей
			while floor_i < int(new_floor): # "перебор" этажей
				floor_i += 1
				print(floor_i)
	def __del__(self): # деструктор
		print(f'{self.name} снесен, но он останется в истории')

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
