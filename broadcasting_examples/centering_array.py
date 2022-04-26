import numpy as np
x = np.random.random((10,3))
xmean = x.mean(0)
print(xmean)
x_centered = x - xmean
print(x_centered)
print('mean 0 of x_centered should be now nearly 0', x_centered.mean(0))