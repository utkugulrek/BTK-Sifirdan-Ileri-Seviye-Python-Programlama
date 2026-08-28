"""Veri güncelleme UPDATE -> update_product()"""

import mysql.connector


def update_product(id, name, price):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        use_pure=True,
        database="node-app",
    )
    cursor = connection.cursor()

    sql = "UPDATE products SET name = 'Samsung S10'"  # Hepsini günceller
    sql = "UPDATE products SET name = 'Samsung S10' WHERE id = 5"
    sql = "UPDATE products SET name = 'Samsung S10', price = 5000 WHERE id = 1"

    sql = "UPDATE products SET name = %s, price = %s WHERE id = %s"
    values = (name, price, id)

    # cursor.execute(sql)
    cursor.execute(sql, values)

    try:
        connection.commit()  # Burada gönderilir net olarak database'e
        print(f"{cursor.rowcount} tane kayıt güncellendi.")
    except mysql.connector.Error as err:
        print("Hata", err)
    finally:
        connection.close()  # Bağlantı ile iş bitince kapat
        print("Database bağlantısı kapandı.")


def get_products():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        use_pure=True,
        database="node-app",
    )
    cursor = connection.cursor()

    cursor.execute("SELECT name, price, id FROM products")
    products = cursor.fetchall()

    for product in products:
        print(f"ID: {product[2]} | Name: {product[0]} | Price: {product[1]}")


id = input("Güncellemek istediğiniz ürünün ID numarası: ")
name = input("Güncel Ürün İsmi: ")
price = input("Güncel Fiyat: ")

update_product(id, name, price)
get_products()
