import numpy as np

a = np.full((2,3), 1)
print(a)

b = np.full((3,2), 2)
print(b)

# Matrix Multiplication
print(np.matmul(a, b))

# Determinant
c = np.identity(3)
print(np.linalg.det(c))

# For more info
# https://numpy.org/doc/stable/reference/routines.linalg.html