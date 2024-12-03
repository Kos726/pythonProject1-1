import sqlite3

population = "database_population.db"


def initiate_db():
	connection = sqlite3.connect(population)
	cursor = connection.cursor()

	# В таблице  будем использовать ссылку к картинкам вместо BLOB
	cursor.execute('''
				CREATE TABLE IF NOT EXISTS Population(
				id INTEGER PRIMARY KEY,
				country TEXT NOT NULL,
				population INTEGER NOT NULL   
				)
				''')

	cursor.execute("CREATE INDEX IF NOT EXISTS idx_country ON Population (country)")

	connection.commit()
	connection.close()
	print('Таблица создана')


def add_params(country, population_):
	connection = sqlite3.connect(population)
	cursor = connection.cursor()
	cursor.execute(
		"INSERT INTO Population (country, population) VALUES (?, ?)",
		(country, population_)
		)
	connection.commit()
	connection.close()

def params_include():
	population_world = ['Китай', 'Индия', 'США', 'Индонезия', 'Бразилия',
						'Пакистан', 'Нигерия', 'Бангладешь', 'Россия', 'Мексика']
	volume = [1398, 1373, 331, 269, 214, 205, 202, 169, 145, 133]
	for i in range(len(population_world)):
		add_params(population_world[i], volume[i])


if __name__ == '__main__':
	initiate_db()
	params_include()
