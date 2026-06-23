# To access the no. of elements in a array

"""
array[start : stop : step]

arr[start : end] , start to end - 1
negative step -1 reverse 
"""

import numpy as np 

arr = np.array([10 , 20 , 30 , 40 , 50])

print(arr[0:4])  #index 0 to 3
print(arr[::-1]) #reverse order
print(arr[::2])  #evry second element
