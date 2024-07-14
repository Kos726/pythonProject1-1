# Вариант 1: с использованием "in"
def single_root_words_v1(root_word, *other_words):
	same_words= []
	r_w_l = root_word.lower()  							# понижаем регистр главного слова
	for i in range(len(other_words)):
		o_w_l = other_words[i].lower() 					# понижаем регистр слов открытого множества
		if (r_w_l in o_w_l) == True:					# поиск корня в словах множества, если "ок" > ответ
			same_words.append(other_words[i])
		elif (o_w_l in r_w_l) == True:					# поиск корня слов из множества в главном, если "ок" > ответ
			same_words.append(other_words[i])
	return same_words
	
# Вариант 2: с использованием "find"
def single_root_words_v2(root_word, *other_words):
	same_words= []
	r_w_l = root_word.lower()  							# понижаем регистр главного слова
	for i in range(len(other_words)):
		o_w_l = other_words[i].lower() 					# понижаем регистр слов открытого множества
		fnd_owl = o_w_l.find(r_w_l) 					# поиск корня в словах множества
		fnd_rwl = r_w_l.find(o_w_l) 					# поиск корня слов из множества в главном
		if fnd_owl >= 0 or fnd_rwl >= 0: 				# если индекс поиска >=0, то > ответ
			same_words.append(other_words[i])
	return same_words
	
# Вариант 3: с использованием "count"
def single_root_words_v3(root_word, *other_words):
	same_words= []
	r_w_l = root_word.lower()		  							# понижаем регистр главного слова
	for i in range(len(other_words)):
		o_w_l = other_words[i].lower() 							# понижаем регистр слов открытого множества
		if o_w_l.count(r_w_l) > 0 or r_w_l.count(o_w_l) > 0: 	# если индекс поиска >=0, то > ответ
			same_words.append(other_words[i])
	return same_words	

print()
print('Результаты с использованием функции "in":')
result1 = single_root_words_v1('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words_v1('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)

print('\n Результаты с использованием функции "find": ')
result1 = single_root_words_v2('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words_v2('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)

print('\n Результаты с использованием функции "count": ')
result1 = single_root_words_v3('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words_v3('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)