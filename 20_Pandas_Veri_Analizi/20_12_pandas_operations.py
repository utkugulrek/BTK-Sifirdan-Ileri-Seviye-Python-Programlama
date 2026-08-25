"""
Bazı özel Pandas metotları ile ilgili çalışma
"""

import numpy as np
import pandas as pd

data = {
    "Column1": [1, 2, 3, 4, 5],
    "Column2": [10, 20, 13, 20, 25],
    "Column3": ["abc", "bcaa", "ade", "cb", "dea"],
}


def kareal(x):
    return x * x


df = pd.DataFrame(data)

result = df
result = df["Column2"].unique()  # Kolondaki unique elemanları seçer
result = df["Column2"].nunique()  # Kolondaki unique sayısı (number unique)
result = df["Column2"].value_counts()  # Her elemanın tekrar sayısı

result = df["Column1"] * 2  # Kolonu 2 ile çarpar
result = df["Column1"].apply(kareal)  # Column1'deki değerler sırasıyla fonksiyona gönderilir
# .apply obje olarak çağırılır metot olarak değil. O yüzden parametre yok
df["Column4"] = df["Column3"].apply(len)

result = len(df.columns)  # Kolonların sayısı
result = df.index  # İndeks bilgileri
result = len(df.index)  # İndeks sayısı
result = df.info  # DataFrame hakkında info

result = df.sort_values("Column2")  # Column2'ye göre küçükten büyüğe sıralama
result = df.sort_values("Column2", ascending=False) # Büyükten küçüğe
result = df.sort_values("Column3")  # Column3'e göre alfabetik sıralama

print(result)

####################################################################################################

data_2 = {
    "Ay": ["Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan"],
    "Kategori": ["Elektronik","Elektronik","Elektronik","Kitap","Kitap","Kitap","Giyim","Giyim","Giyim"],
    "Gelir": [20, 30, 15, 14, 32, 42, 12, 36, 52]
}


df_2 = pd.DataFrame(data_2)
# İndeksi Ay'lar, Kolonu Kategori'ler olan tablo oluşturma
df_2 = df_2.pivot_table(index="Ay", columns="Kategori", values="Gelir")

print(df_2)
