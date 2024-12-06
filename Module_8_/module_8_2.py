
message = 'В numbers записан некорректный тип данных:'


def personal_sum(numbers):
	result = 0
	incorrect_data = 0
	
	if isinstance(numbers, int):
		incorrect_data = 1
		print(f' {message} Число. Ошибок: {incorrect_data}')
	elif isinstance(numbers, str):
		incorrect_data = 1
		print(f'{message} Строка. Ошибок: {incorrect_data}')
					
	else:
		for i in numbers:
			try:
				result = result + i
			except TypeError:
				incorrect_data += 1
				result = 0
				if not isinstance(numbers, int):
					print(f'{message} Не число. Ошибок: {incorrect_data}')
		
		return result, incorrect_data		


def calculate_average(numbers):

	try:
		mean_value = personal_sum(numbers)[0]/len(numbers)
		print(f'Все отлично! Ошибок: 0')
		return mean_value
	
	except TypeError:
		incorrect_data = 1
		if isinstance(numbers, int):
			print(f'{message} Число. Ошибок: {incorrect_data}')
			
		elif isinstance(numbers, str):
			print(f'{message} Строка. Ошибок: {incorrect_data}')
		return 0
			
	except ZeroDivisionError:
		print(f'{message} в знаменателе ноль.')
		return 0
		

print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average(["1", "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Список. Всё должно работать
print(f'Результат 5: {calculate_average((42, 15, 36, 13))}')  # Кортеж. Всё должно работать
