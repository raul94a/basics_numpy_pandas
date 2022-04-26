import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn; seaborn.set()

#need to download required files from jakeVanderPlas repo
data = pd.read_csv('jakeVanderPlas/notebooks/data/president_heights.csv')
heights = np.array(data['height(cm)'])
print(heights)
print('MEDIA: ', heights.mean())
print('DESVIACIÓN TÍPICA: ', heights.std())
print('DESVICACION TIPICA CON NUMPY', np.std(heights)) ##mas eficient
print('ALTURA MINIMA', np.min(heights))
print('ALTURA MAXIMA', np.max(heights))
print('PERCENTIL 25', np.percentile(heights,25))
print('MEDIANA: ', np.median(heights))
print('PERCENTIL 75', np.percentile(heights,75))
##representación gráfica
plt.hist(heights)
plt.title('Height Distribution of US Presidents')
plt.xlabel('Height(cm)')
plt.ylabel('number')
plt.savefig('img/presidents_heights.png')