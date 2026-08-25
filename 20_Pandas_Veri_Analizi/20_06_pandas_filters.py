"""
Pandas kütüphanesinde veri, kolon, sütün filtreleme çalışması
"""

import numpy as np
import pandas as pd

data = np.random.randint(10, 100, 75).reshape(15, 5)
df = pd.DataFrame(data, columns=["Column1", "Column2", "Column3", "Column4", "Column5"])

result = df

# Verilere Erişme
result = df.columns  # Column bilgileri
result = df.head()  # İlk 5 satır | 10 dersen 10
result = df.tail()  # Son 5 satır | 10 dersen 10

result = df["Column1"].head()  # Column1'in ilk 5 kaydı
result = df[["Column1", "Column5"]].head()
result = df[5:15][["Column1", "Column3"]]

# Verileri Filtreleme
result = df > 50  # True False
result = df[result]  # Büyükleri aldı küçükler NaN

result = df["Column1"] > 50  # Column1'de 50'den büyük olan
result = df[result]  # Column1'de 50'den büyük olan satırların her sütununu getir

result = df[(df["Column1"] > 50) & (df["Column4"] < 70)]

# .query()
result = df.query("Column1 >= 50 & Column2 % 2 == 0 ")
result = df.query("Column1 >= 50 & Column2 % 2 == 0 ")[["Column1", "Column2"]]

print(result)
