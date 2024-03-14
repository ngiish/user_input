# import numpy as np 
# # Creating an array using np.array() method 
# arr = np.array([10, 20, 30, 40, 50], ndmin= 5) 
# a = np.array([10, 20, 30, 40, 50], dtype = bool) 
# # Printing 
# print(arr)
# print(a)
import numpy as np
a = np.arange(5,81,9)
a = a.reshape(3,3)
print('Original array is:')
print(a)
print('\n')
print('Modified array is:')
for x in np.nditer(a):
   print(x)