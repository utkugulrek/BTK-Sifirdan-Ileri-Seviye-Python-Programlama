"""
Pandas kütüphanesinde join merge çalışması
"""

import pandas as pd

customers = {
    "CustomerId": [1, 2, 3, 4],
    "FirstName": ["Ahmet", "Ali", "Hasan", "Canan"],
    "LastName": ["Yılmaz", "Korkmaz", "Çelik", "Toprak"],
}

orders = {
    "OrderId": [10, 11, 12, 13],
    "CustomerId": [1, 2, 5, 7],
    "OrderDate": ["2010-07-04", "2010-08-04", "2010-07-07", "2012-07-04"],
}

df_customers = pd.DataFrame(customers, columns=["CustomerId", "FirstName", "LastName"])
df_orders = pd.DataFrame(orders, columns=["OrderId", "CustomerId", "OrderDate"])

print(df_customers)
print(df_orders)

result = pd.merge(df_customers, df_orders, how="inner")  # Ortaklar
result = pd.merge(
    df_customers, df_orders, how="left"
)  # Tüm müşteriler gelsin NaN yazsın siparişleri
# Alışveriş sitesinde siparişi olmayan kullanıcılar -> Kullanıcı üye oldu ama siparişi yok
result = pd.merge(
    df_customers, df_orders, how="right"
)  # Tüm siparişleri getir NaN koy müşterisine
# Sahipsiz sipariş var mı? Database'den veri mi silindi?
# result = pd.merge(df_customers, df_orders, how="outer")  Tüm kayıtları getirir


print(result)

####################################################################################################

customers_a = {
    "CustomerId": [1, 2, 3, 4],
    "FirstName": ["Ahmet", "Ali", "Hasan", "Canan"],
    "LastName": ["Yılmaz", "Korkmaz", "Çelik", "Toprak"],
}

customers_b = {
    "CustomerId": [4, 5, 6, 7],
    "FirstName": ["Yağmur", "Çınar", "Cengiz", "Can"],
    "LastName": ["Bilge", "Turan", "Yılmaz", "Turan"],
}

df_customers_a = pd.DataFrame(customers_a, columns=["CustomerId", "FirstName", "LastName"])
df_customers_b = pd.DataFrame(customers_b, columns=["CustomerId", "FirstName", "LastName"])

result = pd.concat([df_customers_a, df_customers_b])  # Satırlar alt alta
result = pd.concat([df_customers_a, df_customers_b], axis=1)  # Kolonlar yan yana


print(result)
