import re 										# импортируем вспомогательную функцию по замене элементов строк

class WordsFinder:
	
	file_names = [] 							# создаем пустой список файлов
	all_words = {} 								# создаем пустой словарь слов
	dict_find = {}
	dict_count = {}
				
	def __init__(self, *args):
		self.file_names = args 					# используем args для множества файлов

# получение словаря "файл: список слов"		
	def get_all_words(self):
			
			for element in self.file_names:
				
				with open(element, 'r', encoding = 'utf-8') as file_:
					GetWord_1 = file_.read().lower()
					GetWord_2 = re.sub(r"[,.=!?;: - ]", ' ', GetWord_1) # исключаем регулярные знаки
					GetWord_3 = GetWord_2.replace('  ', ' ') 			# чистим от двух пробелов
					GetWord_4 = GetWord_3.split() 									# разделяем и властвуем
					self.all_words[element] = GetWord_4 							# создаем словарь
			return self.all_words

										
# функция поиска искомого слова в строке	
	def find(self, word):
		word = word.lower()
		for name, words in self.get_all_words().items():
			try:
				self.pos = words.index(word)
				self.dict_find[name] = self.pos + 1
			except ValueError:
				self.dict_find[name] = 'None'
		return self.dict_find

				
# функция подсчета количества повторов искомого слова в строке		
	def count(self, word):
		word = word.lower()
		for name, words in self.get_all_words().items():
			try:
				number = words.count(word)
				self.dict_count[name] = number
			except ValueError: 											# мало ли какая еще ошибка
				self.dict_count[name] = 'None'
		return self.dict_count

	
finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words(), '\n') 									# Все слова
print(finder2.find('TEXT')) 											# 3 слово по счёту
print(finder2.count('teXT')) 											# 4 слова teXT в тексте всего
"""
finder1 = WordsFinder('Rudyard Kipling - If.txt')
print()
print(finder1.get_all_words(), '\n')
print(finder1.find('If'))
print(finder1.count('if'))

finder3 = WordsFinder('test_file.txt', 'Rudyard Kipling - If.txt')
print()
print(finder3.get_all_words(), '\n')
print(finder3.find('for'))
print(finder3.count('for'))
"""