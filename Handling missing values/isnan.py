# To find the missing values from array

import numpy as np 

arr = np.array ([1,2,np.nan , 4 , np.nan ,6])
print(np.isnan(arr))

# Not compaired directly
print(np.nan == np.nan)
