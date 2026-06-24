# To insert a value at specific position in array

"""
np.insert(array, index, value, axis=none)
array - original array
index - position
value - value which u want to insert
axis - none for 1D
axis - 0 , row wise 
1 column wise 
"""

import numpy as np

arr = np.array( [1, 2, 3, 4, 5, 6] )
new_arr = np.insert(arr , 6 , 7 )
print(arr)
print(new_arr)