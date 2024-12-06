class Horse:
					
		def __init__(self): # тут определяем два атрибута со значениями по-умолчанию
			self.x_distance = 0
			self.sound = 'Frrr'
	
		def run(self, dx): # а тут определяем метод=функцию воздействия на атрибут
			self.x_distance = dx + self.x_distance	

class Eagle:

	def __init__(self): # тут определяем два атрибута со значениями по-умолчанию
		self.y_distance = 0
		self.sound = 'I train, eat, sleep, and repeat'
		
	def fly(self, dy): # а тут определяем метод=функцию воздействия на атрибут
		self.y_distance = dy + self.y_distance			
	
class Pegasus(Horse, Eagle): # наследуем два класса

#наследование как подмена атрибутов одного класса атрибутами других классов
	def __init__(self):
		Horse.__init__(self) # "подменяем" init пегаса init лошади
		Eagle.__init__(self) # "подменяем" init пегаса init орла
	
	def move(self, dx, dy): # данный метод "обрабатывает" вложенные методы из других классов 
			super().run(dx) #  применяем наследуемый метод run
			super().fly(dy) # применяем наследуемый метод fly
			
	def get_pos(self): # т.к. мы привнесли в класс пегаса классы лошади и орла, то заново определять атрибуты не требуется
		return  self.x_distance, self.y_distance	
		
	def voice(self): #аналогично методу выше
		print(f'{self.sound}')


print('Проверка:')

p1 = Pegasus()
#print(Pegasus.mro())
print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
