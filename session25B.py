import numpy as np
brd_array = np.array([[1,2,3],
                      [4,5,6],
                      [7,8,9]])

print(brd_array)
print(brd_array.shape)

vector= np.array([1,2,3])
print(vector)

Y = np.empty_like(brd_array)
print(Y)

A =np.array([[1,2],[3,4]])
B = np.array([[6,7],[8,9]])

matrix =np.dot(A,B)
print(matrix)

linmatrix = np.linalg.det(A)
print(linmatrix)