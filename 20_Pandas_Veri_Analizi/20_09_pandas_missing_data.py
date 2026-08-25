"""
Pandas kütüphanesinde bozuk, eksik datalar üzerinde çalışma
"""

import numpy as np
import pandas as pd

data = np.random.randint(10, 100, 15).reshape(5, 3)

df = pd.DataFrame(
    data, index=["a", "c", "e", "f", "h"], columns=["column1", "column2", "column3"]
)

df = df.reindex(["a", "b", "c", "d", "e", "f", "g", "h"])

result = df

result = df.drop("column1", axis=1)  # axis= 1 -> kolon
result = df.drop("a")  # Default 0 -> satır

result = df.isnull()  # NaN True döndürür.
result = df.notnull()  # NaN False döndürür.

result = df.isnull().sum()  # column'daki null değerleri sayısı
result = df["column1"].isnull().sum()  # column1'deki null değerleri sayısı

print(result)

####################################################################################################

new_column = [np.nan, 30, np.nan, 51, np.nan, 30, np.nan, 10]  # Column ekleme
df["column4"] = new_column

result = df[df["column1"].isnull()]  # Column1'in NaN olan satırları gelir

print(result)

####################################################################################################
# NaN değeri varsa satırda, sütunda -> sil

result = df.dropna()  # Satırda
result = df.dropna(how="any")  # Herhangi bir NaN'da siler
result = df.dropna(how="all")  # Tüm satır NaN ise siler
result = df.dropna(subset=["column1", "column2"], how="all")  # Column'a göre NaN arama
result = df.dropna(thresh=2)  # En az 2 NaN değilse silme

print(result)

####################################################################################################
# NaN doldurma

result = df.fillna(value="no input")  # NaN değerlerini "no input" ile doldurur
result = df.fillna(value=1)  # NaN değerlerini 1 ile doldurur

result = df.sum()  # Her column'daki sayıların toplamı
result = df.sum().sum()  # Column'ların da toplam değeri
result = df.size  # Eleman sayısı
result = df.isnull().sum()  # NaN sayısı column column
result = df.isnull().sum().sum()  # NaN sayısı toplam


def ortalama(df):
    toplam = df.sum().sum()
    #   adet = df.size - df.isnull().sum().sum() Derste yapılan buydu
    #   adet = df.notnull().sum().sum()  # Kendi çözümüm
    adet = df.count().sum()  # AI Performans önerisi
    return toplam / adet


result = df.fillna(ortalama(df))

print(result)
