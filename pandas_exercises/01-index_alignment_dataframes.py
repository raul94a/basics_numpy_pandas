# The objective of this exercise is to discover how index and column alignment works 
# when working with dataframes.

# When combining two different dataframes, shared indexes and columns will align. Let's see
# how it works! 
import pandas as pd
import numpy as np
#A random state with a predefined seed. 
rng = np.random.RandomState(42)

#2x2 dataFrame, 4 records, each one between (0,20)
A = pd.DataFrame(rng.randint(0,20,(2,2)), columns=list('AB'))
print(A)
B = pd.DataFrame(rng.randint(0,10,(3,3)),columns=list('BAC'))
print(B)

#If the sum of dataframes is made, indexes and column will be aligned. Each coincidence
#will be performed with the corresponding mathematical operation.
#Unaligned indexes and/or columns will be displayed with NaN
# print(A+B)
#As the previous print demonstrate, B column of DF1 will be aligned with column B of DF2 as equal as indexes
#we can use ufuncs in order to perform mathematical operations
print(A.add(B))
##### In the case we want to maintain the new dataframe but without NaN artifacts, we can use the argument fill_value of ufunc
##### in this case we are going to convert a DataFrame into a stack an then, recon the mean of that stack
### What is a Stack?
###### A stack is a data structure where values are «stacked». let see the output
stackA = A.stack()
print(stackA)
stackA_mean = stackA.mean()
print(stackA_mean)#12.25
df_sum = A.add(B, fill_value=stackA_mean)
print(df_sum)
# print(A.subtract(B, fill_value=stackA_mean))