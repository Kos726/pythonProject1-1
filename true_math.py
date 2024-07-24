from math import inf # подключение матемтической библиотеки

def divide(first, second):
	if int(second) != 0:
		result = float(first) / float(second)
		return result
	else:
		return inf # значение из библиотеки, эквивалентно float("inf")
