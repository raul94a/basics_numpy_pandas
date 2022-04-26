from turtle import color
import numpy as np
import matplotlib.pyplot as plt
import seaborn;seaborn.set();
rand = np.random.RandomState(42)

X = rand.rand(10,2)

plt.scatter(X[:,0], X[:,1], s=120)
plt.savefig('img/scatter_k_nearest.png')
#va a computarse la distancia entre cada par de puntos.

# Now we'll compute the distance between each pair of points.
# Recall that the squared-distance between two points is the sum of the squared differences 
# in each dimension; using the efficient broadcasting ([Computation on Arrays: Broadcasting](
# 02.05-Computation-on-arrays-broadcasting.ipynb)) and aggregation ([Aggregations: Min, Max, and 
# Everything In Between](02.04-Computation-on-arrays-aggregates.ipynb))  routines provided by NumPy 
# we can compute the matrix of square distances in a single line of code:

dist_sq = np.sum((X[:, np.newaxis, :] - X[np.newaxis, :, :]) ** 2, axis=-1)
# print(dist_sq)
differences = X[:, np.newaxis, :] - X[np.newaxis, :, :]
# print(X[:, np.newaxis, :], '\n', X[np.newaxis,:,:])
# print( X[:, np.newaxis, :].shape)
# print(differences)
sq_differences = differences ** 2
# print(differences)
dist_sq = sq_differences.sum(-1)
print(dist_sq.shape,'\n',dist_sq)
K = 2
nearest_partition = np.argpartition(dist_sq,K + 1, axis=1)
print(nearest_partition)

for i in range(X.shape[0]):
    for j in nearest_partition[i, :K+1]:
        # print(X[i], j)
        plt.plot(*zip(X[j], X[i]), color='black')
plt.savefig('img/knearest.png')
