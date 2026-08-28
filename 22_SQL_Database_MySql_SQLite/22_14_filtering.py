"""Filtreleyerek veri getirme WHERE -> get_products() ve get_by_id() içerisinde"""

import mysql.connector


# Filtreleme İşlemleri Eklendi
def get_products():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        use_pure=True,
        database="node-app",
    )
    cursor = connection.cursor()

    # cursor.execute("SELECT * FROM products WHERE id=1")  # id=1 olan kayıtlar
    # cursor.execute("SELECT * FROM products WHERE name='Samsung S8'")
    # cursor.execute("SELECT * FROM products WHERE name='Samsung S8' AND price=3000")
    # cursor.execute("SELECT * FROM products WHERE name='Samsung S8' OR price>=3000")
    # cursor.execute("SELECT * FROM products WHERE name LIKE '%Samsung S8%'")  # içinde geçen
    # cursor.execute("SELECT * FROM products WHERE name LIKE 'Samsung S8%'")  # başında olsun
    # cursor.execute("SELECT * FROM products WHERE name LIKE '%Samsung S8'")  # sonunda olsun

    products = cursor.fetchall()

    for product in products:
        print(f"Name: {product[0]} | Price: {product[1]}")


# Kullanıcının verdiği id göre filtreleme
def get_by_id(id):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        use_pure=True,
        database="node-app",
    )
    cursor = connection.cursor()

    sql = "SELECT * FROM products WHERE id=%s"
    params = (id,)

    cursor.execute(sql, params)

    product = cursor.fetchone()

    print(f"ID: {product[0]} | Name: {product[1]} | Price {product[2]}")


# get_products()
get_by_id(int(input("ID giriniz: ")))
