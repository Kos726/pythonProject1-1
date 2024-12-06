class Vehicle:
	def __new__(cls, *args, **kwargs):
		return object().__new__(cls)

		
	def __init__(self, owner, _model, __color, __engine_power):
		self.owner = owner
		self._model = _model
		self.__engine_power = __engine_power
		self.__color = __color

				
	def get_model(self):			
			return self

						
	def get_horsepower(self):
			return self

						
	def get_collor(self):
			return self

						
	def set_color(self, new_color):
		__COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
		self.new_color = new_color.lower()
		if self.new_color in __COLOR_VARIANTS:
			self.__color = new_color
		else:
			print(f'\u001b[38;5;196m Нельзя сменить цвет на {new_color}')

		
	def print_info(self):
			print(f'\u001b[38;5;32m Модель: {self._model}')
			print(f'\u001b[38;5;32m Мощность двигателя: {self.__engine_power}')
			print(f'\u001b[38;5;32m Цвет транспорта: \u001b[38;5;40m {self.__color}')
			print(f'\u001b[38;5;32m Владелец: \u001b[38;5;40m {self.owner}')		
			
					
class Sedan(Vehicle):
			__PASSENGERS_LIMIT = 5		
				


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
