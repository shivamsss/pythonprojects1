import numpy as np
n1 = np.array([[1,2,3],
               [4,5,6]])
n2 = np.array([[8,9,6],
               [1,2,5]])

Vstack=np.vstack((n1,n2))
print(Vstack)
Hstack=np.hstack((n1,n2))
print(Hstack)
