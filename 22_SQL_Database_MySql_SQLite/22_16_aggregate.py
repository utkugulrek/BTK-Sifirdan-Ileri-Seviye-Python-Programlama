"""Hesaplama Fonksiyonları -> COUNT(), AVG(), SUM(), MAX(), MIN()"""

import mysql.connector


def get_product_info():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        use_pure=True,
        database="node-app",
    )
    cursor = connection.cursor()

    # sql = "SELECT COUNT(*) FROM products"  # Kayıt sayısı (7,) döndürür
    # sql = "SELECT COUNT(name) FROM products"  # NOTNULL olmayan her kolon aynı *
    # sql = "SELECT AVG(price) FROM products"  # Ortalama
    # sql = "SELECT SUM(price) FROM products"  # Toplam
    # sql = "SELECT MAX(price) FROM products"  # Max
    # sql = "SELECT MIN(price) FROM products"  # Min

    sql = (
        "SELECT name FROM products WHERE price = " "(SELECT MAX(PRICE) FROM products)"
    )  # En pahalı ürünün adını getir

    cursor.execute(sql)

    # fetchone() kullanmak daha mantıklı
    result = cursor.fetchone()

    print(f"result: {result[0]}")


get_product_info()
