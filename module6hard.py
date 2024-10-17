import math
from termcolor import colored


class Figure:
	def __new__(cls, color, *sides):
		cls.color = color
		cls.sides = sides
		return object().__new__(cls)

	def __init__(self, color, *sides):	
		self.color = color
		self.sides = sides
		self.sides_count = 0
		self.__sides = []  # список сторон (целые числа)
		filled = True  # закрашенный, bool
		
	def get_color(self):  # возвращает список RGB цветов
		return self.color
		
	def __is_valid_color(self, *_color):  # служебный, принимает параметры r, g, b, и проверяет корректность
		# переданных значений перед установкой нового цвета. Корректным цвет: все значения r, g и b - целые числа
		# в диапазоне от 0 до 255 (включительно)
		color_error = [True for i in _color[0] if (i % 2 != 0 and i % 2 != 1) or i < 0 or i > 255]
		return color_error

	def set_color(self, *__color):  # принимает параметры r, g, b - числа
		# и изменяет атрибут __color на соответствующие значения, предварительно проверив их на корректность.
		# Если введены некорректные данные, то цвет остаётся прежним
		if any(self.__is_valid_color(__color)) is True:
			return self.color
		else:
			self.color = __color
			return self.color

	def __is_valid_sides(self, *_sides):  # служебный метод, принимает неограниченное кол-во сторон,
		# возвращает True если все стороны целые положительные числа и кол-во новых сторон совпадает с текущим,
		# False - во всех остальных случаях
		sides_error = [True for i in _sides[0] if (i % 2 != 0 and i % 2 != 1) or i < 0]
		number_sides_error = len(_sides[0]) != self.sides_count
		sides_error.append(number_sides_error)
		return sides_error

	def get_sides(self):  # возвращает значение атрибута __sides
		return self.__sides
	
	def __len__(self):  # возвращает периметр фигуры.
		perimetr = sum([i for i in self.sides])
		return perimetr
	
	def set_sides(self, *new_sides):  # принимает новые стороны, если их количество не равно sides_count,
		# то должен не изменять, в противном случае - менять.
		if any(self.__is_valid_sides(new_sides)) is True:
			self.__sides = [1 for i in range(self.sides_count)]
			return self.__sides
		else:
			self.__sides = [new_sides[i] for i in range(self.sides_count)]
			return self.__sides


class Circle(Figure):
	def __init__(self, color, *sides):
		self.color = color
		self.sides = sides
		self.sides_count = 1
		
	def radius(self):
		return 2 * math.pi / self.sides[0]  # __radius, рассчитать исходя из длины окружности
	
	def get_square(self):
		return math.pi * (self.radius() ** 2)
		
		
class Triangle(Figure):
	def __init__(self, color, *sides):
		self.color = color
		self.sides = sides
		sides_count = 3
		
	def get_square(self):
		a = self.sides[0]
		b = self.sides[1]
		c = self.sides[2]
		p = (a + b + c) / 2  # полупериметр
		square = math.sqrt(p * (p-a)*(p-b)*(p-c))
		return square	


class Cube(Figure):
	def __init__(self, color, *sides):
		self.color = color
		self.sides = sides
		self.sides_count = 12
		
	def get_volume(self):
		a = self.sides[0]
		volume = a * a * a
		return volume


circle1 = Circle((200, 200, 100), 10)  # Цвет, стороны
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((200, 100, 50), 5, 7, 8)


# Проверка на изменение цветов:
print(colored('__Проверка изменения цветов___', 'green'))
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
print(colored('\n Цвет с ошибкой', 'red'))
circle1.set_color(355, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
print(colored('\n__Проверка изменения сторон__', 'green'))
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())
print(colored('\n Стороны с ошибкой', 'red'))
circle1.set_sides(15, 10)  # Не изменится
print(circle1.get_sides())
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())

print(colored('\n___Расчет геометрических параметров___', 'green'))
# Проверка периметра (круга), это и есть длина:
print(f' Периметр окружности: {len(circle1)}')
print(f' Периметр треугольника: {len(triangle1)}')

# Проверка расчета радиуса окружности
print(f' Радиус окружности: {circle1.radius():5.3f}')

# Проверка расчета площади окружности и треугольника
print(f' Площадь окружности: {circle1.get_square():5.3f}')
print(f' Площадь треугольника: {triangle1.get_square():5.3f}')

# Проверка объёма (куба):
print(f' Объем куба: {cube1.get_volume()}')
