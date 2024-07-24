# импорт модулей с переименованием функций
from true_math import divide as divide_true
from fake_math import divide as divide_fake

print('\n_____Проверка по заданию_____')

result1 = divide_fake(69, 3)
result2 = divide_fake(3, 0)
result3 = divide_true(49, 7)
result4 = divide_true(15, 0)

print(result1)
print(result2)
print(result3)
print(result4)

print('\n____Ручной ввод произвольных значений____')
try:
	a, b = input('\n Введите через пробел два произвольных числа а и b, после нажмите Enter: ' ).split()
	print()
	print(f' Отношение числа а = {a} к числу b = {b} равно: ')
	print('                   Вариант из модуля math_fake: ', divide_fake(a, b))
	print('                   Вариант из модуля math_true: ', divide_true(a, b))
except BaseException:
		print('\n!!! Вы задали только одну переменную или ввели некоректный символ, повторите ввод')