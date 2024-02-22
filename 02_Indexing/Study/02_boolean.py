import numpy as np
array1 = np.array([2, 3, 5, 6, 7, 18, 123, 123,4 1242,42 5,25 3, 53])

array1 > 4

array1 % 2 == 0

booleans = np.array([True, True, False, False, True])
np.where(booleans)

filter = np.where(array1 > 4)

filter

array1(filter)