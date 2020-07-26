import numpy as np
data = np.loadtxt("numpydata.txt",dtype=np.int)
print(data)

my_array= np.arange(1,20,1)
print(my_array)

np.savetxt("myowndata",my_array)