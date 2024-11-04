import sqlite3

list_products_file_name = "database_module_14_bot.db"
list_users_file_name = "database_module_14_bot.db"


def initiate_db():
	connection = sqlite3.connect(list_products_file_name)
	cursor = connection.cursor()

	# В таблице  будем использовать ссылку к картинкам вместо BLOB
	cursor.execute('''
				CREATE TABLE IF NOT EXISTS Products(
				id INTEGER PRIMARY KEY,
				title TEXT NOT NULL,
				description TEXT,
				price INTEGER NOT NULL,
				photo TEXT   
				)
				''')

	cursor.execute("CREATE INDEX IF NOT EXISTS idx_title ON Products (title)")

	connection.commit()
	connection.close()
	print('Таблица products создана')

	connection = sqlite3.connect(list_users_file_name)
	cursor = connection.cursor()

	# В таблице  будем использовать ссылку к картинкам вместо BLOB
	cursor.execute('''
					CREATE TABLE IF NOT EXISTS Users(
					id INTEGER PRIMARY KEY,
					username TEXT NOT NULL,
					email TEXT,
					age INTEGER NOT NULL,
					balance INTEGER NOT NULL   
					)
					''')

	cursor.execute("CREATE INDEX IF NOT EXISTS idx_username ON Users (username)")

	connection.commit()
	connection.close()
	print('Таблица users создана')


def get_all_products(id_product_number=0, local_product=False):
	connection = sqlite3.connect(list_products_file_name)
	cursor = connection.cursor()

	# Подсчет общего количества продуктов
	try:
		if local_product is False:
			cursor.execute("SELECT COUNT(*) FROM Products")
			count_products = cursor.fetchone()[0]
			print('Всего Продуктов:', count_products)
			return count_products

		elif local_product is True:
			cursor.execute("SELECT title, description, price, photo FROM Products WHERE id = ?",
						(id_product_number + 1, )
						)
			params_product = cursor.fetchone()
			product = [param for param in params_product]
			print(product)
			return product
	except:
		print('Таблица не создана или перемещена')

	connection.commit()
	connection.close()


def add_users(username, email, age):
	connection = sqlite3.connect(list_users_file_name)
	cursor = connection.cursor()
	cursor.execute(
		"INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
		(username, email, age, 1000)
		)
	connection.commit()
	connection.close()


def is_included(username):
	connection = sqlite3.connect(list_users_file_name)
	cursor = connection.cursor()
	check_user = cursor.execute("SELECT username FROM Users WHERE username = ?",
								(username, ))
	if check_user.fetchone() is not None:
		check = True
	else:
		check = False
	connection.commit()
	connection.close()
	return check


if __name__ == '__main__':
	initiate_db()
	for i in range(get_all_products()):
		get_all_products(id_product_number=i, local_product=True)
