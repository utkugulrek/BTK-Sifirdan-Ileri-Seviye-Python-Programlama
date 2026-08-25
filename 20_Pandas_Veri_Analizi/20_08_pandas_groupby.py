"""
Pandas kütüphanesinde groupby çalışması
"""

import numpy as np
import pandas as pd

personeller = {
    "Çalışan": [
        "Ahmet Yılmaz",
        "Can Ertürk",
        "Hasan Korkmaz",
        "Cenk Saymaz",
        "Ali Turan",
        "Rıza Ertürk",
        "Mustafa Can",
    ],
    "Departman": [
        "İnsan Kaynakları",
        "Bilgi İşlem",
        "Muhasebe",
        "İnsan Kaynakları",
        "Bilgi İşlem",
        "Muhasebe",
        "İnsan Kaynakları",
    ],
    "Yaş": [30, 25, 45, 50, 23, 34, 42],
    "Semt": ["Kadıköy", "Tuzla", "Maltepe", "Tuzla", "Maltepe", "Tuzla", "Kadıköy"],
    "Maaş": [5000, 3000, 4000, 3500, 2750, 6500, 4500],
}

df = pd.DataFrame(personeller)

result = df["Maaş"].sum()  # Toplam maaş
result = df.groupby("Departman").groups  # Departman gruplarını ve üyelerinin indeksleri
result = df.groupby(["Departman", "Semt"]).groups  # İkisine de sahip olanlar

semtler = df.groupby("Semt")

for name, group in semtler:
    print(name)
    print(group)

print("-" * 75)

for name, group in df.groupby("Departman"):
    print(name)
    print(group)

print("-" * 75)

result = df.groupby("Semt").get_group("Kadıköy")

print("-" * 75)

result = df.groupby("Departman").sum()  # Tüm toplamları

result = df.groupby("Departman")["Maaş"].mean()  # Maaş ortalaması departmanların

result = df.groupby("Semt")["Çalışan"].count()  # Semtte yaşayan çalışan sayısı

result = df.groupby("Departman")["Yaş"].max()  # Departmanlardaki max yaşlar

result = df.groupby("Departman")["Maaş"].max()["Muhasebe"]  # Muhasebede alınan max maaş

result = df.groupby("Departman")["Maaş"].agg(
    [np.sum, np.mean, np.max, np.min]
)  # Departmanlardaki maaş işlemleri

result = (
    df.groupby("Departman")["Maaş"]
    .agg([np.sum, np.mean, np.max, np.min])
    .loc["Muhasebe"]
)  # Muhasebeye özel maaş işlemleri

print(result)
