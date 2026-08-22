import numpy as np

result = np.array([1, 3, 5, 7, 9])
result = np.arange(1, 10)  # 1...9
result = np.arange(10, 100, 3)  # 10 13 16 19... 94 97
result = np.zeros(10)  # 0. 0.0 .0.  10 tane float | 1. 1. 1. da var .ones
result = np.linspace(
    0, 100, 5
)  # 0-100 arasını 5 eşit parçaya ayırır -> 0. 25. 50. 75. 100.
result = np.random.randint(0, 10)  # random 0-9 sayı
result = np.random.randint(1, 10, 3)  # 3 tane random sayılı liste verir
result = np.random.rand(
    5
)  # 0-1 arasında 5 rastgele sayı .randn ise negatifi de dâhil eder

np_array = np.arange(50)
np_multi = np_array.reshape(5, 10)
print(np_multi.sum(axis=1))  # Satırların toplamı

rnd_numbers = np.random.randint(1, 100, 10)
print(rnd_numbers)
result = rnd_numbers.max()  # Listedeki max değeri verir .min min değeri verir
result = rnd_numbers.mean()  # Listenin ortalaması
result = rnd_numbers.argmax()  # En büyük değerin indeksi


print(result)
