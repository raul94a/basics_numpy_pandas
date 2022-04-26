import numpy as np
x = np.arange(5)
# print(x + 2)
# print(x - 2)
# print(x * 2)
# print(-x)
# print((-x) ** 2)
# print(np.log(x + 1))
# print(np.exp(x))
# print(np.absolute(-x))
# print(np.cos(x), np.sin(x), np.tan(x))
# print(np.power(4,x))

#funciones reductoras
print(x,'=> La suma reductora del array es: ' +  str(np.add.reduce(x)))
print(x,'=> La resta reductora del array es: ' +  str(np.subtract.reduce(x)))
print(x + 1,'=> La multiplicacion reductora del array es: ' +  str(np.multiply.reduce(x + 1)))
#acumuladores
print('###################### ACUMULADORES #############################')
print(x, '=> el resultado de la acumulación de valores (suma) es '  + str(np.add.accumulate(x)))
print(x + 1, '=> el resultado de la acumulación de valores (multiplicacion) es '  + str(np.multiply.accumulate(x + 1)))
print(x, '=> el resultado de la acumulación de valores (resta) es '  + str(np.subtract.accumulate(x)))
## hay funciones específicas para realizar estas tareas: np.sum, np.prod, np.cumsum, np.cumprod