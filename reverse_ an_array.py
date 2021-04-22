import numpy as np
#reversing an array normally using reverse method
arr = [1,2,3,4,5]
arr.reverse()
print(arr)
#reversing an array using reversed method
arr1=[1,2,3,4,5,6,7,8,9,10]
print(list(reversed(arr1)))
#reversing using flip method in numpy
arr2=np.array(['p','r','a','b','h','a','s','a','l','e','t','i'])
print(np.flip(arr2))



