"""Kayıt silme DELETE"""

import mysql.connector


def delete_product(id):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        use_pure=True,
        database="node-app",
    )
    cursor = connection.cursor()

    sql = "DELETE FROM products"  # Tüm kayıtları siler
    sql = "DELETE FROM products WHERE id = 6"
    sql = "DELETE FROM products WHERE name LIKE '%s7%'"

    sql = "DELETE FROM products WHERE id = %s "
    params = (id,)

    # cursor.execute(sql)
    cursor.execute(sql, params)

    try:
        connection.commit()  # Burada gönderilir net olarak database'e
        print(f"{cursor.rowcount} tane kayıt silindi.")
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


id = input("Silmek istediğiniz ürünün ID numarası: ")

delete_product(id)
get_products()


# ÖNEMLİ NOT!
# sql = "DELETE FROM products WHERE id = "+id  # diyerek de yollayabiliriz
# ancak bu üstteki yöntem ile SQL Injection riskine önlem alınmaz!
