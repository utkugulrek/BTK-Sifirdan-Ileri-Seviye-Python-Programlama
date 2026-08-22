import numpy as np

numbers1 = np.random.randint(10, 100, 6)
numbers2 = np.random.randint(10, 100, 6)

print(numbers1)
print(numbers2)

result = numbers1 + numbers2
print(result)

result = numbers1 + numbers2 + 10
print(result)

result = np.sin(numbers1)
result = np.cos(numbers1)
print(result)

result = np.sqrt(numbers1)
result = np.log(numbers1)
print(result)

mnumbers1 = numbers1.reshape(2, 3)
mnumbers2 = numbers2.reshape(2, 3)

result = np.vstack((mnumbers1, mnumbers2))  # Dikey birleştirme Vertical
result = np.hstack((mnumbers1, mnumbers2))  # Yatay birleştirme Horizontal

print(result)

result = numbers1 > 5  # Tüm elemanları 5'ten büyük mü? True | False
result = numbers1 % 2 == 0  # Tüm elemanlar çift mi?
print(result)

print(numbers1[result])  # Koşulu sağlayan elemanlar
