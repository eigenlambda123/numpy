import numpy as np
a = np.array([[1,2,3,4,5,6,7], [8,9,10,11,12,13,14]])

# ALL 0s matrix
print(np.zeros(5))
print(np.zeros((2,2)))
print(np.zeros((3,3)))

# ALL 1s matrix
print(np.ones(5))
print(np.ones((2,2)))
print(np.ones((3,3)))

# ANY OTHER numbers
# ((rows, columns), value)
print(np.full((2, 2), 99))


# ANY OTHER numbers (full_like)
print(np.full_like(a, 4))

# Random Decimal numbers
print(np.random.rand(3, 3)) # 3x3
print(np.random.rand(4, 2, 3)) # 4x2x3
print(np.random.random_sample(a.shape)) # same shape as 'a'

# Random Integers
# (range, size=(col, row))
print(np.random.randint(7, size=(3,3)))
print(np.random.randint(5,10, size=(3,3)))

# Identity Matrix
print(np.identity(3))

# Repeat Array
arr = np.array( [[1,2,3]])
r1 = np.repeat(arr, 3, axis=0)
print(r1)

# For Lot More
# https://docs.scipy.org/doc/numpy-1.13.0/user/basics.indexing.html
