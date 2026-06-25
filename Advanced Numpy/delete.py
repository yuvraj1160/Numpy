# To remove a value from flatten array

"""
np.delete(array, index , axis = none)
flatten array
"""

import numpy as np

arr = np.array( [1, 2, 3, 4, 5, 6] )
new_arr = np.delete(arr, 0)
print(new_arr)