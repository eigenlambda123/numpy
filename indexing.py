import numpy as np

a = np.array([[1,2,3,4,5,6,7], [8,9,10,11,12,13,14]])
print(a)

# Get Specific Element [r,c]
print(a[1,5])
print(a[1,-2])

# Get Specific Row [r,c]
print(a[0,:])

# Get Specific column [r,c]
print(a[:,0])

# [startindex:endinde:stepsize]
print(a[0, 1:6:2])
print(a[1, 2:6:2])


# 3D EXAMPLE
# Change Specific Element
a[1,5] = 20
print(a)

# Change Entire Column
a[:,2] = 5
print(a)

# Change Entire Column with Specific
a[:,2] = [1,2]
print(a)

# 2d List in a 2D List
b = np.array([[[1,2], [3,4]], [[5,6],[7,8]]])
print(b)

# Get Specific Element (work outside n)
# [Outside, Inside, Specific]
print(b[0,0,0])
print(b[0,0,1])
print(b[0,1,0])
print(b[0,1,1])
print(b[1,0,0])
print(b[1,0,1])
print(b[1,1,0])
print(b[1,1,1])

# Replace
b[:, 1, :] = [[9,9], [8,8]] 
print(b)