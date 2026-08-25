"""
Pandas kütüphanesine giriş, PandasSeries çalışması
"""

import pandas as pd
import numpy as np

# Data
numbers = [20, 30, 40, 50]
letters = ["a", "b", "c", "d"]
dictionary = {"a": 10, "b": 20, "c": 30, "d": 40}
random_numbers = np.random.randint(10, 100, 6)

# pd.Series()
pandas_series = pd.Series()
pandas_series = pd.Series(numbers)
pandas_series = pd.Series(letters)
pandas_series = pd.Series(5, [0, 1, 2, 3])
pandas_series = pd.Series(5, letters)
pandas_series = pd.Series(dictionary)
pandas_series = pd.Series(random_numbers)

# Erişim
pandas_series = pd.Series(numbers, letters)
print(pandas_series)

result = pandas_series[:2]
result = pandas_series[["a", "d"]]  # Olmayan değerde NaN dönmedi hata verdi
result = pandas_series.sum()
result = pandas_series.max()
result = pandas_series + pandas_series
result = pandas_series >= 50
result = pandas_series[result]

print(result)
print("-" * 75)
####################################################################################################

mercedes2018 = pd.Series([20, 30, 40, 50], ["AMG", "C", "Maybach", "G"])
mercedes2019 = pd.Series([40, 30, 20, 10], ["AMG", "C", "S", "G"])

total = mercedes2018 + mercedes2019
print(total)
