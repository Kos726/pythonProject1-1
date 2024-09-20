import time
from datetime import datetime
from threading import Thread


def write_words(word_count, file_name):
	with open(file_name, 'w', encoding="UTF-8") as file_:
		for i in range(word_count):
			file_.write(f'Какое-то слово № {i+1}\n')
	print(f'Завершилась запись в файл {file_name}')
	time.sleep(0.1)


time_start = datetime.now()

result_1 = write_words(10, 'example1.txt')
result_2 = write_words(30, 'example2.txt')
result_3 = write_words(200, 'example3.txt')
result_4 = write_words(100, 'example4.txt')

time_end = datetime.now()
time_res = time_end - time_start
print(time_res)

time_start = datetime.now()
result_5 = Thread(target=write_words, args=(10, 'example5.txt'))
result_6 = Thread(target=write_words, args=(30, 'example6.txt'))	
result_7 = Thread(target=write_words, args=(200, 'example7.txt'))	
result_8 = Thread(target=write_words, args=(100, 'example5.txt'))

result_5.start()
result_6.start()
result_7.start()
result_8.start()

result_5.join()
result_6.join()
result_7.join()
result_8.join()

time_end = datetime.now()
time_res = time_end - time_start
print(time_res)
