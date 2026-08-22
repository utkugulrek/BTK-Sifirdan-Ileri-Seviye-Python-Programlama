import numpy as np

numbers = np.array([0, 5, 10, 15, 20, 25, 50, 75])

result = numbers[::-2]

numbers2 = np.array([[0, 5, 10], [15, 20, 25], [50, 75, 85]])
result = numbers2[0, 2]  # İlk satırın 3. elemanı
result = numbers2[:, 2]  # Her satırın 3. elemanı listesi
result = numbers2[:, 0: 2]  # Her satırın içinde 0 ile 2. indeks arasındaki elemanların matrisi
result = numbers2[-1,:]  # Çok boyutlu olduğu için , koyuyoruz 

arr1 = np.arange(0, 10)
arr2 = arr1.copy()  # Farklı adres tanımlanır arr2 için ve bilgiler o adrese kopyalanır farklı adresleri gösterir diziler

print(result)
