import sqlite3

list_products_file_name = "products.db"


def initiate_db(name_=list_products_file_name):
	connection = sqlite3.connect(name_)
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
	print('Таблица создана')


def get_all_products(id_product_number=0, local_product=False, name_=list_products_file_name):
	connection = sqlite3.connect(name_)
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
						(id_product_number + 1, ))
			params_product = cursor.fetchone()
			product = [param for param in params_product]
			print(product)
			return product
	except:
		print('Таблица не создана или перемещена')

	connection.commit()
	connection.close()


if __name__ == '__main__':
	initiate_db()
	for i in range(get_all_products()):
		get_all_products(id_product_number=i, local_product=True)
