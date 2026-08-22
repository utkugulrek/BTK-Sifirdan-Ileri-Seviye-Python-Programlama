import numpy as np

# Python List
py_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Numpy Array
np_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])  # Numpy dizisine çevirir


py_multi = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
np_multi = np_array.reshape(3, 3)

print(py_multi)  # .ndim = 1 | .shape = (9,)
print(np_multi)  # .ndim = 2 | .shape = (3, 3)
