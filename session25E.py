import numpy as np

array = np.genfromtxt("temperature.csv", delimiter=",",dtype=np.float)
print(array)

print(array[0])
print(array[1])