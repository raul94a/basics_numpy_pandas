import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
rainfall = pd.read_csv('jakeVanderPlas/notebooks/data/Seattle2014.csv')['PRCP'].values
print(rainfall)
inches = rainfall / 254 # 1/10mm -> inches 
print(inches.shape)
plt.hist(inches, 40)
plt.title('Counting rainy days')
plt.xlabel('Height(cm)')
plt.ylabel('number')
plt.savefig('img/rainy_days.png')
##si miramos la figura necesitamos masking para obtener los valores d eitneres
##podemos saber el numero de dias sin lluvia
print('Días sin lluvia: ', np.sum(inches == 0))
print('Días con lluvia: ', np.sum(inches > 0))
print('Días con más de 0.5 Inches de lluvia: ', np.sum(inches > 0.5))
print('Días con menos de 0.1 Inches: ', np.sum((inches < 0.2) & (inches > 0)))
#no obstante, ¿Cómo se seleccionan estos valores deseados? Se va a mostrar como seleccionar los días lluviosos
days_with_rain = inches[inches != 0]
#y ahora podemos establecer cual es la media de los dias de lluvia
print('Media de los dias de lluvia: ', np.mean(days_with_rain))