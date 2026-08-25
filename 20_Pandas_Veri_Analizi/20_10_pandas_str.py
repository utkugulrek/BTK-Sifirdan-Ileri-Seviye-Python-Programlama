"""
Pandas kütüphanesinde string çalışması
"""

import pandas as pd

data = pd.read_csv("datasets/nba.csv")

# data = data.dropna()
data.dropna(inplace=True)  # Orijinal data üzerine değişiklik yapma

# print(data.columns) columns isimleri
data["Name"] = data["Name"].str.upper()  # İsimleri büyütür
# data["index"] = data["Name"].str.find("A")
# data = data.Name.str.contains("JORDAN")   Jordan içeren indeksler True
# data = data[data.Name.str.contains("JORDAN")]  # İlk 10 Jordan'ı yazar
# data = data.Team.str.replace(" ", "-")

data[["FirstName", "LastName"]] = (
    data["Name"].loc[data["Name"].str.split().str.len() == 2].str.split(expand=True)
)

print(data.head(10))
