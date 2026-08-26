"""
Matplotlib kütüphanesinde figure ile ilgili çalışmalar
"""

import matplotlib.pyplot as plt
import numpy as np

# Örnek 1: Axis Kaydırma
"""
x = np.linspace(-10, 9, 20)
y = x**3
z = x**2

figure = plt.figure()

axes_cube = figure.add_axes([0.1, 0.1, 0.8, 0.8])  # soldan kaydırmalar ve % kaç kaplasın

axes_cube.plot(x, y, "b")
axes_cube.set_xlabel("X Axis")
axes_cube.set_ylabel("Y Axis")
axes_cube.set_title("Cube")

axes_square = figure.add_axes(([0.15, 0.6, 0.25, 0.25]))
axes_square.plot(x, z, "g")
axes_square.set_xlabel("X Axis")
axes_square.set_ylabel("Y Axis")
axes_square.set_title("Square")

plt.show()
"""

# Örnek 2: Legend'ın yerini değiştirme
"""
x = np.linspace(-10, 9, 20)
y = x**3
z = x**2

figure = plt.figure()

axes = figure.add_axes([0, 0, 1, 1])

axes.plot(x, z, label="Square")
axes.plot(x, y, label="Cube")
axes.legend(loc=1)  # 1 sağ üst, 2 sol üst, 3 sol alt, 4 sağ alt

plt.show()
"""

# Örnek 3: figure büyüklüğü ve kaydetme
"""
x = np.linspace(-10, 9, 20)
y = x**3
z = x**2

fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(4, 4))  # axes -> axes_1, axes_2 ile de olur

axes[0].plot(x, y, "y")
axes[0].set_title("Square")
axes[0].grid(True)

axes[1].plot(x, z, "b")  # axes_2 olurdu mesela
axes[1].set_title("Cube")

plt.tight_layout()
fig.savefig("figure1_02_.png")
fig.savefig("figure1_02_.pdf")

plt.show()
"""
