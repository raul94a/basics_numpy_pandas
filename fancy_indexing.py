from sqlite3 import Row
import numpy as np


random = np.random.RandomState(49)
x = random.randint(100, size=10) ##array of ten elements [42 45 40 54 12 69  5 49 18 36]
indexes = [2,7,9]
print(x[indexes]) # [40,49,36]
#you can create a new dimension array with fancy indexing
indexes = np.array([[2,9],[9,2]])
print(x[indexes]) # [[40,36],[36,40]]
#what while working with matrix?
x = np.arange(8).reshape((2,4))
print(x)
column = np.array([1,2])
row = np.array([0,1])
print(x[row,column]) #[1,6]

#this is also affected by broadcasting
print(x[row[:,np.newaxis], column]) #[[1,2],[5,6]]
print(row[:,np.newaxis] * column) 


#COMBINED FANCY INDEXING
print('-----------COMBINED FANCY INDEXING--------------')
x = np.arange(12).reshape((3,4))
row = np.array([0,1,2])
mask = np.array([1,0,1,0], dtype=bool)
print(mask)
print(x[row[:,np.newaxis],np.array([True,False,True,False])])
