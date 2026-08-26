"""
Matplotlib kütüphanesine giriş çalışmaları
İlgili örnek için tırnakları kaldırmak yeterli
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Örnek 1: İlk tablolar ve Stil
"""
x = [1, 2, 3, 4]  # y eksenine yazdırır tek liste verirsek
y = [1, 4, 9, 16]

plt.plot(x, "o--g")
plt.plot(x, y, color="red", linewidth=5)  # soldakini x, sağdakini y eksenine verir

plt.axis([0, 6, 0, 20])  # 0-20 y | 0-6 x

plt.title("Grafik Başlığı")
plt.xlabel("x ekseni")
plt.ylabel("y ekseni")

plt.show()
"""

# Örnek 2: Birden fazla grafik tek düzlemde
"""
x = np.linspace(0, 2, 100)

plt.plot(x, x, label="linear", color="green")
plt.plot(x, x**2, label="quadratic", color="yellow")
plt.plot(x, x**3, label="cubic", color="blue")

plt.xlabel("x label")
plt.ylabel("y label")

plt.title("Simple Plot")

plt.legend()  # Doğruların adlarını gösterir
plt.show()
"""

# Örnek 3: Birden fazla grafik farklı düzlemlerde alt alta
"""
x = np.linspace(0, 2, 100)
fig, axs = plt.subplots(3)

axs[0].plot(x, x, color="blue")
axs[0].set_title("linear")
axs[1].plot(x, x**2, color="yellow")
axs[1].set_title("quadratic")
axs[2].plot(x, x**3, color="black")
axs[2].set_title("cubic")

plt.tight_layout()  # Başlıklar grafikler ile iç içe girmesin diye

plt.show()
"""

# Örnek 4: Grafikleri yan yana ve alt alta oluşturma
"""
x = np.linspace(0, 2, 100)
fig, axs = plt.subplots(2, 2)

fig.suptitle("Grafik Başlığı")

axs[0, 0].plot(x, x, color="blue")
axs[0, 1].plot(x, x**2, color="yellow")
axs[1, 0].plot(x, x**3, color="green")
axs[1, 1].plot(x, x**4, color="red")

plt.show()
"""

# Örnek 5: 20. bölümdeki nba.csv dosyası
"""
df = pd.read_csv("../20_Pandas_Veri_Analizi/datasets/nba.csv")

df = df.drop(["Number"], axis=1).groupby("Team").mean(numeric_only=True)

df.head().plot(subplots=True)  # Otomatik düzlem ekleme
plt.legend()

plt.show()
"""
