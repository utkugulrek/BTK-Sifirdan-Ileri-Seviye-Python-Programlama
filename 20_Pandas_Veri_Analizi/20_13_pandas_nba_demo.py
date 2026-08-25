"""
Pandas için hazırlanmış 11 sorulu NBA veri analizi uygulama çalışması
Problemler optimum performans ile çözülmeye çalışıldı
"""

import pandas as pd

df = pd.read_csv("datasets/nba.csv")

# 1- İlk 10 kaydı getiriniz.
result = df.head(10)

# 2- Toplam kaç kayıt vardır ?
result = len(df.index)

# 3- Tüm oyuncuların toplam maaş ortalaması nedir ?
result = df["Salary"].mean()

# 4- En yüksek maaşı ne kadardır ?
result = df["Salary"].max()

# 5- En yüksek maaşı alan oyuncu kimdir ?
result = df.loc[df["Salary"].idxmax(), "Name"]
# 6- Yaşı 20-25 arasında olan oyuncuların isim ve oynadıkları takımları azalan şekilde sıralı getiriniz.
result = df[(df["Age"] >= 20) & (df["Age"] < 25)][["Name", "Team", "Age"]].sort_values(
    "Age"
)
result = df[["Name", "Team", "Age"]][lambda x: x["Age"].between(20, 24)].sort_values(
    by="Age"
)  # Daha performanslı yöntem

# 7- "John Holland" isimli oyuncunun oynadığı takım hangisidir ?
result = df[df["Name"] == "John Holland"]["Team"].iloc[0]
result = df.loc[df["Name"] == "John Holland", "Team"].values[0]  # Daha performanslı

# 8- Takımlara göre oyuncuların ortalama maaş bilgisi nedir ?
result = (
    df.groupby("Team")["Salary"]
    .mean()
    .round(2)
    .sort_values(ascending=False)
    .reset_index()
)

# 9- Kaç farklı takım mevcut ?
result = len(df.groupby("Team"))
result = df["Team"].nunique()  # Daha performanslı

# 10- Her takımda kaç oyuncu oynamaktadır ?
result = df["Team"].value_counts()

# 11- İsmi içinde "and" geçen kayıtları bulunuz.
result = df[df["Name"].str.contains("and", case=False, na=False)]

print(result)
