import numpy as np

sigma = np.array([[1, .5, .2], [.5, 2, .3], [.2, .3, 2]])
print('Sigma array:')
print(sigma)
C = np.linalg.cholesky(sigma)
Z = np.random.normal(0,1,(3, 10**6))

# Compute correlated normal random variables
X = np.dot(C, Z) # note, that "C" is equiv. to Matlab's "C'"

# Check that the Cholesky decomposition works
print(np.cov(X))
