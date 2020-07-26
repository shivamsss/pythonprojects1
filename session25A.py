import numpy as np

data=[(1,2),(2,3),(3,4)]
array1 = np.array(data)
print(array1)
print(array1[0:2,1])

print(array1.max())
print(array1.min())
print(array1.sum())

print("Column wise row min and max")
print(array1.max(axis=0))
print(array1.min(axis=0))
print("Row wise row min and max")
print(array1.max(axis=1))
print(array1.min(axis=1))