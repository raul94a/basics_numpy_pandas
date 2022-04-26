import numpy as np
import matplotlib.pyplot as plt
from pyparsing import line
np.random.seed(42)
x = np.random.randn(100)
bins = np.linspace(-5,5,20)
# print(bins)
counts = np.zeros_like(bins)
# print(counts)
i = np.searchsorted(bins,x)
# print(i)
np.add.at(counts,i,1)
# print(x,bins)
plt.hist(bins,x,histtype='step')
print('x',x.max())
print('bins',bins.max())
print('counts',counts)
print('i', i)
plt.savefig('img/binning.png')
