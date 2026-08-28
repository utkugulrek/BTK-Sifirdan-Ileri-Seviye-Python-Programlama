"""Çekilen verileri sıralamak ORDER BY -> get_products() içerisinde"""

import mysql.connector


# Sıralama işlemleri
def get_products():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        use_pure=True,
        database="node-app",
    )
    cursor = connection.cursor()

    # cursor.execute("SELECT * FROM products ORDER BY name")  # Alfabetik
    # cursor.execute("SELECT * FROM products ORDER BY price")  # Düşük Fiyattan Yükseğe
    # cursor.execute("SELECT * FROM products ORDER BY price DESC")  # Yükseten Düşüğe
    cursor.execute("SELECT * FROM products ORDER BY name, price")  # Sırayla

    try:
        products = cursor.fetchall()

        for product in products:
            print(f"Name: {product[1]} | Price: {product[2]}")

    except mysql.connector.Error as err:
        print("Hata", err)
    finally:
        connection.close()
        print("Database bağlantısı kapandı.")


get_products()
