import numpy as np


before = np.array([[0,1,2,3], [4,5,6,7]])
print(before)

# Reshape
after = before.reshape((8, 1))
print(after)

# Vertically Stacking Vectors
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

print(np.vstack([v1, v2, v2, v2]))

# Horizontal Stack
h1 = np.ones((2,4))
h2 = np.zeros((2,4))

print(np.hstack((h1, h2)))