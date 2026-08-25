"""
Pandas kütüphanesinde veri seçme çalışması
"""

import pandas as pd
from numpy.random import randn

df = pd.DataFrame(
    randn(3, 3), index=["A", "B", "C"], columns=["Column1", "Column2", "Column3"]
)

result = df
result = df["Column1"]
result = type(df["Column1"])  # Series çünkü serilerin birleşimi DataFrame
result = df[["Column1", "Column2"]]

# loc["row", "column"] | loc["row"] |loc[":", "column"]
result = df.loc["A"]
result = df.loc[:, "Column1":"Column3"]  # Aralıktaki sütunlar
result = df.loc["B":"C", :"Column2"]

result = df.iloc[2]  # Yine de indeks ile çalışmak için

result = df.loc["A", "Column2"]  # Elemana erişme

df["Column4"] = pd.Series(randn(3), ["A", "B", "C"])  # Column Ekleme
df["Column5"] = df["Column1"] + df["Column3"]

df2 = df.drop("Column5", axis=1)  # Column Silme | Yukarıdan aşağıya olduğunu belirtmek için axis=1
print(df2)  # DataFrame üzerinde işlem yapılmadı aslında inplace = True yaparsak yapar

print(df)

print(result)
