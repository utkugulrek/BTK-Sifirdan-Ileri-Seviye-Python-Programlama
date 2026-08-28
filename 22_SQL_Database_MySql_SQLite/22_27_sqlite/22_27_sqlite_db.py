"""SQLite kullanımı"""

import sqlite3

connection = sqlite3.connect("chinook.db")  # Varsa bağlanır yoksa oluşturur

cursor = connection.cursor()

cursor.execute("SELECT * FROM customers")

result = cursor.fetchall()

for r in result:
    print(r)

connection.close()
