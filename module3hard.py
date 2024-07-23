#____Задание_____

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

#_____Код______

nmbrs = [] 											# множество numbers для сборки цифр
strg = "" 											# строка string для сборки букв
n = 0 												# вспомогательная переменная для перебора значений

print('\n Применение многоуровневой распаковки данных посредством рекурсии ')

print('\n _______Задача_______\n Вычислить количество символов и сумму цифр, входящих в множество:')
print(f' data_structure = {data_structure}')
		
def calculate_structure_sum(*arg): 			# функция с переменным изменяемым множеством входных параметров
		arg_ = list(arg)								# преобразуем кортеж в список
		global strg										# экспортируем глобальную переменную в функцию
		len_ = len(list(arg_[0]))       				# подсчет длины списка для перебора
		
		if len_ == 0: 									# после исчерпани списка, выводим ответ
			return nmbrs, sum(nmbrs), strg, len(strg), 'Ответ: ', sum(nmbrs)+len(strg)
			
		elif len_ >=1: 									# до исчерпания списка, обсчитываем элементы этого списка
			item_i = arg_[0][n] 						# внутренний i-ый элемент множества

			if isinstance(item_i, int) == True: 		# если попалось число
				nmbrs.append(item_i) 					# кидаем число в список
				arg_[0].pop(n)
				arg = tuple(arg_)
				return calculate_structure_sum(*arg) 	# не менять!!!
				
			elif isinstance(item_i, str) == True: 		#если попалась строка
				t_str = arg_[0].pop(n) 					# переменная с вычленением строкового значения
				arg = tuple(arg_)
				t_strFree = t_str.replace(' ', '') 		# очистка строк от пробелов
				strg = strg + t_strFree # сборка строки
				return calculate_structure_sum(*arg) 	# не менять!!!

			elif isinstance(item_i, dict) == True: 		# если попался словарь
				t_key = list(item_i.keys()) 			# получение списка ключей словаря
				t_value = list(item_i.values()) 		# получение списка значений словаря
				arg_[0].append(t_key) 					# переброска списка клбчей в основной масcив
				arg_[0].append(t_value) 				# переброска списка значений в основной массив
				t_dict = arg_[0].pop(n) 				# исключение словаря из основного массива
				arg = tuple(arg_) 						# перезапись массива в виде кортежа
				return calculate_structure_sum(*arg)
				
			elif isinstance(item_i, tuple) == True: 	# если попался кортеж
				t_tuple = list(item_i) 					# перевод значений кортежа в список
				arg_[0].append(t_tuple) 				# переброска значений в основной массив
				t_tupel_clear = arg_[0].pop(n) 			# вычленение кортежа из основного массива
				arg = tuple(arg_) 						# перезапись массива с новыми значениями
				return calculate_structure_sum(*arg)
			
			elif isinstance(item_i, set) == True: 		# если попалось множество
				t_set = list(item_i) 					# перевод значений множества в список
				arg_[0].append(t_set) 					# переброска значений в основной массив
				t_set_clear = arg_[0].pop(n) 			# вычленение множества из основного массива
				arg = tuple(arg_)  						# перезапись  основного массива
				return calculate_structure_sum(*arg)
														
			elif isinstance(item_i, list) == True: 		# если попался список
				len_l = len(item_i) 					# длина списка
				
				if  len_l > 0: 							# если длина списка
					t_list_item = arg_[0][0].pop(0) 	# распаковка листа, с вычленением элемента списка
					arg_[0].append(t_list_item) 		# добавляем элемент списка в конец основной функции
					t = arg_[0].pop(0) 					# вычлиняем элемент
					arg_[0].append(t)					# отправляем в конец списка
					arg = tuple(arg_)
					return calculate_structure_sum(*arg)
					
				elif len_l == 0:				
					t_2 = arg_[0].pop(0)				# вычлиняем элемент
					return calculate_structure_sum(*arg)
					
result = calculate_structure_sum(data_structure)
																							
print('\n _______Решение_______')
print(f' Множество цифр: {result[0]} >>>> Сумма: {result[1]} \n'
	  f' Множество букв: {result[2]} >>>> Сумма: {result[3]} \n'
	  f' Сумма итого: {result[5]}')

print('\n В слове "Urban2" есть цифра, однако в ответе самого задания,'
	  ' конечная сумма равна 99, что совпадает с моими вычислениями,'
	  '\n т.е. дробление слова на буквы и вычлинение  цифр не проводилось,'
	  ' поэтому в домашней работе так же не исползуется')
