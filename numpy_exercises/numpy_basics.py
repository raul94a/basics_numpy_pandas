import math
import numpy as np
#declarando un array en numpy
#comporatamiento si se añade un string => todo el array se convierte en String
x = np.array([1,2,2])
print(x)
multidimension = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(multidimension)
#setear una dimension minima
array_dos_dim = np.array([[]], ndmin=2)
#tipos
#soporte para numeros complejos
array_tipado = np.array([1.j, 2.j], dtype=complex)
print(array_tipado)
otro_tipo = np.array([(1,3),(5,90)],dtype=[('a','<i4'),('b','<i4')])
print(otro_tipo['a']) #ouput: [1 5]
print(otro_tipo['b']) # [3 90]
#dtypes
#float32,
#otra forma
print(np.array([range(i, i + 3) for i in [2,4,6]])) ## [[2,3,4],[4,5,6],[6,7,8]]

#generating arrays
print(np.zeros(50,dtype=int))
print(np.ones((10, 2), dtype=int))
print(np.full((3,5), math.pi))

#llenado con sequencias 0 - 20 de tres en tres
print(np.arange(0,20,3))
#llenado con un numero de valores espaciados 'evenly' entre un min y un max
begin = 0
end = 100
number_of_elements_to_show = 49
print(np.linspace(begin,end,number_of_elements_to_show, dtype=np.float32))

#numpy random => crea un array 3x3 uniformemente distribuido entre 0 y 1 (y cada valor multiplicado por 600)
print(np.random.random((3,3)) * 600)

#randint => entre un min y un max crea una matriz de dimensiones (x,y)
min = 5
max= 1000
x = 5
y = 9
print(np.random.randint(min,max,(x,y)))
#matrices identidad
print(np.eye(4))
#array con dos numeros que dependen del o que haya en esa parte de la memoria
print(np.empty(2))
#####   DATA TYPES IN NUMPY ######
# bool_ Boolean (True or False) stored as a byte
# int_ Default integer type (same as C long; normally either int64 or int32)
# intc Identical to C int (normally int32 or int64)
# intp Integer used for indexing (same as C ssize_t; normally either int32 or int64)
# int8 Byte (–128 to 127)
# int16 Integer (–32768 to 32767)
# int32 Integer (–2147483648 to 2147483647)
# int64 Integer (–9223372036854775808 to 9223372036854775807)
# uint8 Unsigned integer (0 to 255)
# uint16 Unsigned integer (0 to 65535)
# uint32 Unsigned integer (0 to 4294967295)
# uint64 Unsigned integer (0 to 18446744073709551615)
# float_ Shorthand for float64
# float16 Half-precision float: sign bit, 5 bits exponent, 10 bits mantissa
# float32 Single-precision float: sign bit, 8 bits exponent, 23 bits mantissa
# float64 Double-precision float: sign bit, 11 bits exponent, 52 bits mantissa
# complex_ Shorthand for complex128
# complex64 Complex number, represented by two 32-bit floats
# complex128 Complex number, represented by two 64-bit floats