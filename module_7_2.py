import io
from pprint import pprint

#___Автосписок из задания___	
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
#_______________________________

#Программа
print(f'___Программа по поиску позиции начала строки____')
file_name_ = input(f' Введите название файла для сохранения списка: ')
file_name = file_name_ + '.txt'
open(file_name, 'a').close()

print(f'\n Выбирите вариант создания списка: \n          1 - использовать автосписок\n          2 - собственный список' )
var_list = int(input())

if not isinstance(var_list, int):
 	raise TypeError("\n Значение должно быть целочисленным. Повторите ввод")
elif int(var_list) <= 0 or int(var_list) > 2:
 	print('Вы ввели некоректный символ, повторите')	
elif int(var_list) == 1:
	print(f'Используем автосисок "info" ')
	info_ = info

elif int(var_list) == 2:
	print(f'Создайте список, для этого наберите любую фразу, нажмите "Enter" ')
	#info_ = info_user
	num = 0
	strings_ = []
	input_strings = True
	while input_strings == True:
		num += 1
		string = input(f'Строка {num}: ')
		strings_.append(string)
		variant = input(f'Если желаетe ввести новую строку, нажмите 1, если выйти - 2: ')
		if int(variant) == 1:
			input_strings = True
		elif int(variant) == 2:
			input_strings = False
		elif isinstance(variant, str):
			raise TypeError("\n Значение должно быть целочисленным. Повторите ввод")
		else:
			print(f'Вы ввели некоректный символ, повторите ввод')
	info_ = strings_

print(f'Используемый список: \n {info_}')

# основной учебный блок
def custom_write(file_name, strings):
	strings_positions = {}
	number = 1
	with open(file_name, 'w', encoding = 'UTF-8') as file_:
		for string in strings:
			strings_positions[(number, file_.tell())] = string
			file_.write(string + '\n')
			number += 1
	return strings_positions

# модифицированное задание: в качестве первого аргумента задана переменная "file_name", в качестве второго "info_"

result = custom_write(file_name, info_)
for elem in result.items():
	print(elem)
