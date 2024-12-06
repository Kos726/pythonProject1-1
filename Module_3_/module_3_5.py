# Пример рекурсии
def get_multiplied_digits(number):
	str_number = str(number)					# превращаем цифровое значение в строку
	first = int(str_number[0])					# срез первого знака числа
	if len(str_number) <= 1:					# проверка на количество знаков в числе, если <=1, возврат значения
		return first
	elif len(str_number) > 1:					# проверка на количество знаков в числе, если >1, вычисления
		return first * get_multiplied_digits(int(str_number[1:]))		# Произведение чисел знаков числа

result = get_multiplied_digits(40203)
print(result)
