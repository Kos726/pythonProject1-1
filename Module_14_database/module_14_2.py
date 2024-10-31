import sqlite3
 
 
connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()
 
cursor.execute('''
               CREATE TABLE IF NOT EXISTS Users(
               id INTEGER PRIMARY KEY, 
               username TEXT NOT NULL, 
               email TEXT NOT NULL, 
               age INTEGER,
               balance INTEGER NOT NULL
               )
               ''')
 
cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")
 
 
"""
cursor.execute("DELETE FROM Users WHERE id = ?", (6, ))
"""
# Подсчет общего количества юзеров
cursor.execute("SELECT COUNT(*) FROM Users")
count_users = cursor.fetchone()[0]
print('Всего юзеров:', count_users)
 
# Подсчет суммы баланса и среднего арефмитического значения
cursor.execute("SELECT SUM(balance) FROM Users")
sum_balance = cursor.fetchone()[0]
print('Сумма балансов:', sum_balance)
print('Среднее арифметическое баланса:', sum_balance/count_users)
 
# Получение среднего арефмитического через встроенную функцию. Для проверки
cursor.execute("SELECT AVG(balance) FROM Users")
avg_balance = cursor.fetchone()[0]
print('*AVG:', avg_balance)
 
connection.commit()
connection.close()
