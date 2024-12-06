# Вариант исполнения 1
def all_variants_1(text):
	# start, end, step = 0, 0, 1  #  <=  эта запись лишняя для данного исполнения
	for step in range(len(text)):
		for start in range(len(text)):
			end = start + step + 1
			if end <= len(text):
				yield text[start: end]
		step += 1	


# Вариант исполнения 2
def all_variants_2(text):
	start, end, step = 0, 1, 1
	while step <= len(text):
		step += 1	
		while end <= len(text):
			yield text[start: end]
			start, end = start + 1, end + 1
		start, end = 0, step	


# Вариант исполнения 3
def all_variants_3(text):
	start, end, step = 0, 0, 1	
	while step <= len(text):
		for start in range(len(text)):
			end += 1
			if end <= len(text):
				yield text[start: end]
			start += 1
		end, step = step, step + 1
						

a1 = all_variants_1("abc")
a2 = all_variants_2("abc")
a3 = all_variants_3("abc")

print(f'\n___Вариант_исполнения_1____')
for i in a1:
	print(i)
	
print(f'\n___Вариант_исполнения_2____')
for i in a2:
	print(i)
	
print(f'\n___Вариант_исполнения_3____')	
for i in a3:
	print(i)		
