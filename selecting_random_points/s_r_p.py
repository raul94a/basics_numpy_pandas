import numpy as np
import matplotlib.pyplot as plt


rand = np.random.RandomState(42)
mean = [0,0]
cov = [[1,2],[2,5]]
X = rand.multivariate_normal(mean,cov,100)
print(X.shape)

# plt.scatter(X[:,0], X[:,1])
##fancy indexing
indices = np.random.choice(X.shape[0], 20, replace=False)
print(indices)
selection = X[indices]
print(selection.shape)
print(selection)
plt.scatter(X[:, 0], X[:, 1], alpha=0.3)
plt.scatter(selection[:, 0], selection[:, 1], s=150, facecolor='none', edgecolors='red')
plt.savefig('img/random_points.png')
