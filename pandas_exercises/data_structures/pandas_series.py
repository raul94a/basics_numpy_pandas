import numpy as np
import pandas as pd

#create a series with arrays

series_one = pd.Series([0,11,21,37])
print('series one', '\n',series_one)
series_two = pd.Series(np.arange(10))
print('series two', '\n' ,series_two)
#creation from dic
series_three = pd.Series({'Jaén': 654564, 'Málaga': 1256987, 'Sevilla':2200000, 'Cádiz': 1758111})
print('series three', '\n', series_three)
#index accessing
print('Jaén has a population of ', series_three['Jaén'] ,' people.')
#boolean masking
print(series_three[series_three.values > 2000000])
#slicing with sorting
print(series_three.sort_values(ascending=False)['Sevilla': 'Málaga'])
