"""Kullanıcıdan alınan veriyi Database'e veri ekleme INSERT INTO"""

import mysql.connector


def insert_product(name, price, image_url, description):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        use_pure=True,
        database="node-app",
    )
    cursor = connection.cursor()

    sql = "INSERT INTO products(name, price, imageUrl, description) VALUES (%s, %s, %s, %s)"
    values = (name, price, image_url, description)

    cursor.execute(sql, values)

    try:
        connection.commit()  # Burada gönderilir net olarak database'e
        print(f"{cursor.rowcount} tane kayıt eklendi.")
        print(f"Son eklenen kaydın ID: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("Hata", err)
    finally:
        connection.close()  # Bağlantı ile iş bitince kapat
        print("Database bağlantısı kapandı.")


def insert_products(liste):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        use_pure=True,
        database="node-app",
    )
    cursor = connection.cursor()

    sql = "INSERT INTO products(name, price, imageUrl, description) VALUES (%s, %s, %s, %s)"
    values = liste

    cursor.executemany(sql, values)  # Birden fazla kayıt eklerken

    try:
        connection.commit()  # Burada gönderilir net olarak database'e
        print(f"{cursor.rowcount} tane kayıt eklendi.")
        print(f"Son eklenen kaydın ID: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("Hata", err)
    finally:
        connection.close()  # Bağlantı ile iş bitince kapat
        print("Database bağlantısı kapandı.")


# Neden liste oluşturuldu? Tek tek her yaptığımızda her seferinde bağlantı oluşturuluyor.
liste = []
while True:
    name = input("Ürün Adı: ")
    price = input("Ürün Fiyatı: ")
    image_url = input("Ürün Resmi: ")
    description = input("Ürün Açıklaması: ")

    liste.append((name, price, image_url, description))

    result = input("Devam etmek istiyor musunuz? (e/h)")
    if result == "h":
        print("Kayıtlarınız veri tabanına aktarılıyor...")
        print(liste)
        insert_products(liste)
        break


# insert_product(name, price, image_url, description)
