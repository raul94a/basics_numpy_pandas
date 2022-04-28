import pandas as pd
import numpy as np
rng = np.random.RandomState(42)

#Series and dataframes can align indexes

#generate a random matrix 4x4
random_matrix = rng.randint(100, size=(4,4))
df = pd.DataFrame(random_matrix, columns=list('ABCD'))
#because of broadcasting rules, the substraction of df with an df-indexed-row is row-wise
#of course, algebracally it makes sense
##what is happening here is an alignment between df and the df[0] => returns row of index 0
print(df - df.iloc[0])

#but what if we want to perform a column-wise operation instead of row-wise?
#We have to make a explicit column selection AND (mandatory) SET THE AXIS TO 0
print(df)
print(df.subtract(df['A'], axis=0))