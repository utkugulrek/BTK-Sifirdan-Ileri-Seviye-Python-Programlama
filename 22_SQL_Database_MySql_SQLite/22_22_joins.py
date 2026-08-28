"""İlişkili tablolarda joins kullanımı"""

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

    sql = "SELECT * FROM products"
    sql = "SELECT * FROM categories"
    # İki tablonun kesişen kayıtları o yüzden INNER JOIN | Tüm kolonlar geliyor 2 category_id
    sql = "SELECT * FROM products INNER JOIN categories ON categories.id=products.category_id"
    # İstenilen kolonlar
    sql = "SELECT products.name, products.price,categories.name FROM products INNER JOIN categories ON categories.id=products.category_id"
    # Sadece Telefon
    sql = "SELECT products.name, products.price,categories.name FROM products INNER JOIN categories ON categories.id=products.category_id WHERE categories.name ='Telefon'"
    # Kısaltma kullanmak
    sql = "SELECT p.name, p.price,c.name FROM products AS p INNER JOIN categories as c ON c.id=p.category_id WHERE c.name ='Telefon'"

    cursor.execute(sql)

    try:
        products = cursor.fetchall()
        for product in products:
            print(product)
    except mysql.connector.Error as err:
        print("Hata", err)
    finally:
        connection.close()
        print("Database bağlantısı kapandı.")


get_products()
