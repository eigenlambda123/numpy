import numpy as np

# Matrix

# My solution
p = np.zeros((5,5))
# [[0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]]
p[0,:] = 1
p[4,:] = 1
p[:, 0] = 1
p[: ,4] = 1
p[2, 2] = 9
print(p)

# Solution
output = np.ones((5,5)) # 5x5
# [[1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]]

z = np.zeros((3,3)) # 3x3
z[1,1] = 9 # replace middle
output[1:4, 1:4] = z # replace the 3x3 matrix in range(1:4)
print(output)

# [[1. 1. 1. 1. 1.]
#  [1. 0. 0. 0. 1.]
#  [1. 0. 9. 0. 1.]
#  [1. 0. 0. 0. 1.]
#  [1. 1. 1. 1. 1.]]








# Indexing

# Create the grid using numpy.array
grid = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
    [26, 27, 28, 29, 30]
])

# index [11, 12, 16 ,17]
print(grid[2:4, 0:2])

# index [2, 8, 14 ,20]
print(grid[[0,1,2,3], [1,2,3,4]])

# index [4, 5, 24 ,25, 29, 30]
print(grid[[0, -2, -1], 3:])

