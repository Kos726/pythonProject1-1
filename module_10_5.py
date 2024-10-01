import multiprocessing
from datetime import datetime


def read_info(name):
	all_data = []
	with open(name, 'r', encoding='UTF-8') as file_:
		string_full = True
		while string_full:
			string_ = file_.readline()
			if len(string_) == 0:
				string_full = False
			else:
				all_data.append(string_)


file_names = [f'./file {number}.txt' for number in range(1, 5)]
print(file_names)

# '''
print(f'\n___Линейный метод___')
time_start_1 = datetime.now()
for file in file_names:
	read_info(file)
	time_end_1 = datetime.now()
	time_res_1 = time_end_1 - time_start_1
print(time_res_1, '(линейный)')

# '''
print(f'\n___Мультипроцессорный метод___')
if __name__ == '__main__':
	with multiprocessing.Pool(processes=4) as pool:
		time_start_2 = datetime.now()
		pool.map(read_info, file_names)
	time_end_2 = datetime.now()
	time_res_2 = time_end_2 - time_start_2
	print(time_res_2, '(мультипроцессорный)')
# '''
