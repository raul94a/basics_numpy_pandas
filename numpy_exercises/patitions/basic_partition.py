import numpy as np
#a partition allows us to have the smallest K values 'sorted' into an array
rand = np.random.RandomState(50)
x = rand.randint(0,100, (30))
#the left part of the array (10 first elements) are the smallest values of the list. 
# The right part is an unorderer, corresponding with de 20 largest numbers
print(np.partition(x,10))

#also, we can obtain the indices
indices = np.argpartition(x,10)
#with fancy indexing and slicing we can get the first 10 smallest numbers of the array
mask = x[indices[:10] ] > 10
#also we can search elements via boolean masking (show elements greater than 10)
print(x[indices[:10]][mask])
