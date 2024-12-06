from pprint import pprint 							# импорт библиотеки работы с файлами

open('products.txt', 'a').close() 					# создание файла, если он отсутствует

class Product:

# инициатор обьектов класса продуктов		
	def __init__(self, name, weight, category):
		self.name = name
		self.weight = weight
		self.category = category


	def __str__(self):
		return f'{self.name}, {self.weight}, {self.category}'
		
		
class Shop(Product):

# инициатор объектов класса магазина
		def __init__(self, name ='', weight='', category = ''):
			Product.__init__(self, name, weight, category) 			# наследуем объекты и атрибуты из класса продуктов
			self.__file_name = 'products.txt' 						# новый объект класса - имя файла

# метод чтения списка продуктов
		def get_products(self):
			self.file = open(self.__file_name, 'r')
			list_ = self.file.read()
			self.file.close()
			return list_
			
# метод добавлени новых продуктов в список			
		def add(self, *products):
			i =0
			for i in range(len(products)): 							# перебор продуктов в наборе
				products_ = str(products[i]) 						# дополнительная переменная дл простоты записи
				self.file = open(self.__file_name, 'r') 			# открытие файла
				if products_ in self.file.read(): 					# поиск продукта в списке
					print(f'\u001b[38;5;196m Продукт <название> уже есть в магазине \033[0m')
				else:
					self.file = open(self.__file_name, 'a') 		# добавление продукта
					self.file.write(f'{products_}\n')
				self.file.close() #открыл, закрыл файл!	
					
									
print(f'\u001b[38;5;40m_____Проверка:_____\033[0m')

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())
