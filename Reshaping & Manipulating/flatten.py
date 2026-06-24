# To convert multidimensional array to 1D array

"""
 .ravel() -> view
 .flatten() -> copy
"""

import numpy as np

arr_2d = np.array([[1 , 2, 3], [3, 4, 5]])

arr_1d = (arr_2d.ravel())
Arr_1d = (arr_2d.flatten())
print(arr_1d)
print(Arr_1d)
