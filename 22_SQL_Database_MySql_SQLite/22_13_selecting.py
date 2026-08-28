"""Verileri getirme çalışması SELECT"""

import mysql.connector


def get_products():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        use_pure=True,
        database="node-app",
    )
    cursor = connection.cursor()

    # cursor.execute("SELECT * FROM products")  # * -> Tüm kolonları getir
    cursor.execute("SELECT name, price FROM products")  # Kullanılan kolonlar çekilir

    products = cursor.fetchall()  # Birden fazla kayıt istediğimizde .fetchall()
    # product = cursor.fetchone()  # 1 kayıt getirir .fetchone()

    for product in products:
        # print(f"Name: {product[1]} | Price: {product[2]}")  # Tüm kolonlar olsaydı
        print(f"Name: {product[0]} | Price: {product[1]}")


get_products()
