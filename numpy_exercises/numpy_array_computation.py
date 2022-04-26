import numpy as np
big_array = np.random.randint(1,100,size=10000000)

np.random.seed(0)
def compute_reciprocals(values):
    output = np.empty(len(values))
    for i in range(len(values)):
        output[i] = 1.0 / values[i]
    return output
#esta operación tarda mucho (debido sobre todo a la inferencia de tipos que se debe de realizr)
# print(compute_reciprocals(big_array))
print(1.0 / big_array)
#el ejemplo de arriba, la division, es muy rapido
#paara que sea mas rapido se van a utilizar ufuncs, o lo qu ee slo mismo
#vectorizar los array
# Operator Equivalent ufunc Description
# + np.add Addition (e.g., 1 + 1 = 2)
# - np.subtract Subtraction (e.g., 3 - 2 = 1)
# - np.negative Unary negation (e.g., -2)
# * np.multiply Multiplication (e.g., 2 * 3 = 6)
# / np.divide Division (e.g., 3 / 2 = 1.5)
# // np.floor_divide Floor division (e.g., 3 // 2 = 1)
# ** np.power Exponentiation (e.g., 2 ** 3 = 8)
# % np.mod Modulus/remainder (e.g., 9 % 4 = 1)
# np.abs(array)

#TRIGONOMETRICS
# Trigonometric functions
# NumPy provides a large number of useful ufuncs, and some of the most useful for the
# data scientist are the trigonometric functions. We’ll start by defining an array of
# angles:
# In[15]: theta = np.linspace(0, np.pi, 3)
# Now we can compute some trigonometric functions on these values:
# In[16]: print("theta = ", theta)
# print("sin(theta) = ", np.sin(theta))
# print("cos(theta) = ", np.cos(theta))
# print("tan(theta) = ", np.tan(theta))
# theta = [ 0. 1.57079633 3.14159265]
# sin(theta) = [ 0.00000000e+00 1.00000000e+00 1.22464680e-16]
# cos(theta) = [ 1.00000000e+00 6.12323400e-17 -1.00000000e+00]
# tan(theta) = [ 0.00000000e+00 1.63312394e+16 -1.22464680e-16]


#log and exponencial
# Exponents and logarithms
# Another common type of operation available in a NumPy ufunc are the exponentials:
# In[18]: x = [1, 2, 3]
# print("x =", x)
# print("e^x =", np.exp(x))
# print("2^x =", np.exp2(x))
# print("3^x =", np.power(3, x))
# x = [1, 2, 3]
# e^x = [ 2.71828183 7.3890561 20.08553692]
# 2^x = [ 2. 4. 8.]
# 3^x = [ 3 9 27]
# The inverse of the exponentials, the logarithms, are also available. The basic np.log
# gives the natural logarithm; if you prefer to compute the base-2 logarithm or the
# base-10 logarithm, these are available as well:
# In[19]: x = [1, 2, 4, 10]
# print("x =", x)
# print("ln(x) =", np.log(x))
# print("log2(x) =", np.log2(x))
# print("log10(x) =", np.log10(x))
# x = [1, 2, 4, 10]
# ln(x) = [ 0. 0.69314718 1.38629436 2.30258509]
# log2(x) = [ 0. 1. 2. 3.32192809]
# log10(x) = [ 0. 0.30103 0.60205999 1. ]
# There are also some specialized versions that are useful for maintaining precision
# with very small input:
# In[20]: x = [0, 0.001, 0.01, 0.1]
# print("exp(x) - 1 =", np.expm1(x))
# print("log(1 + x) =", np.log1p(x))
# exp(x) - 1 = [ 0. 0.0010005 0.01005017 0.10517092]
# log(1 + x) = [ 0. 0.0009995 0.00995033 0.09531018]
# When x is very small, these functions give more precise values than if the raw np.log
# or np.exp were used.


#tabla de multiplicar sencilla
x = np.arange(1,11)
print(np.multiply.outer(x,x))
