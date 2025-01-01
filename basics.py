import numpy as np

# List
a = np.array([1,2,3], dtype='int16') # dtype specify
print(a)

# 2d List
b = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])
print(b)

# Get Dimension
print(a.ndim)
print(b.ndim)

# Get Shape
print(a.shape)
print(b.shape)

# Get Type
print(a.dtype)
print(b.dtype)

# Get Size
print(a.itemsize)
print(b.itemsize)

# Get Total Size
print(a.nbytes)
print(b.nbytes)

# For Lot More Info
# https://jakevdp.github.io/blog/2014/05/09/why-python-is-slow/