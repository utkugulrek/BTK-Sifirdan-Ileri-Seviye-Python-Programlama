"""İlk MySQL bağlantısı kurma, database oluşturma ve tablo oluşturma"""

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    use_pure=True,  # caching_sha2_password hatasını önlemek için
)

print(mydb)


mycursor = mydb.cursor()

# mycursor.execute("CREATE  DATABASE mydatabase") # Var olan db oluşturursan hata verir
mycursor.execute("SHOW DATABASES")  # Mevcut database'leri alma

for x in mycursor:
    print(x)


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    use_pure=True,
    database="mydatabase",  # Hangi db'nin kullanılacağı
)

mycursor = mydb.cursor()

# Olan tabloyu oluşturmaya çalışmak da hata verir
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
