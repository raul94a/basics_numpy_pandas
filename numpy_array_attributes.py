# Basics of Array Attributes
# R.Albin - Spain, Jaén
from traceback import print_tb
import numpy as np
# we will seed with a set value in order to
# ensure that the same random arrays are generated each time 
# this code is run
np.random.seed(0)

uno = np.random.randint(10, size=6) 
dos = np.random.randint(10, size=(3,4))
tres = np.random.randint(10, size=(3,4,5))
#Atributos del Array
print(dos.size,dos.ndim, dos.nbytes, dos.size, dos.shape, dos.dtype)
#acceso dimension > 1
# print(dos,dos[2,1])
#slicing multidimensional
print(dos)
#obtenemos una matriz de 2x3
print(dos[:2, :3])
#si modificamos el valor de un slice de un array de numpy
#el slice NO es una copia, si no una referencia al mismo object
#por tanto si cambiamos el slice cambiamos el array original
x = dos[:2,:3]
# x[0,0] = 99
#para copiar un array de numpy 
y = dos[:2,:2].copy()
y[0,0] = 99
# print(dos)
# print(y)
#Reshaping de NumpyArrays
grid = np.arange(1,13) #12 elemetos
# print(grid)
#reshape no funciona si el numero de elementos
#no coincide si x * y de reshape != numero elementos
# print(grid.reshape((4,3)))

#ARRAY CONCATENATION
array1 = np.array([2,3,4,5])
array2 = np.array([0,5,6,9,10,11,12,13,14,15,16,17])
array3 = np.concatenate([array1,array2])
print(array3)
#concatenate tambien funciona con arr bidimensionales

#para trabajar con arrays de dimensiones mixtas
# it can be clearer to use the np.vstack
# (vertical stack) and np.hstack (horizontal stack) functions:
x = np.array([1, 2, 3])
grid = np.array([[9, 8, 7],[6, 5, 4]])
# # vertically stack the arrays
print(np.vstack([x, grid]))
# Out[48]: array([[1, 2, 3],
# [9, 8, 7],
# [6, 5, 4]])
# In[49]: # horizontally stack the arrays
y = np.array([[99],[99]])
print(np.hstack([grid, y]))
# Out[49]: array([[ 9, 8, 7, 99],
# [ 6, 5, 4, 99]])
# Similarly, np.dstack will stack arrays along the third axis.

#ARRAY SPLITTING
x = [1,2,3,99,99,3,2,1]
#indices por los que se parte el array
#3 primer array sera de la posicion 0 a 2 ambos inc
#el indice 3 y 4 seran el segudno arra
#del 5 al final sera el tercero
x1,x2,x3 = np.split(x, [3,5])
print(x1,x2,x3)
#en matrices funciona el vsplit y hsplit
bidimensional = np.array([[2,1,2],[3,4,2],[5,6,7],[8,9,10]])
upper,lower = np.vsplit(bidimensional,[3])
print(upper,lower)
upper,lower=np.hsplit(bidimensional,[1])
print(upper,lower)
