import matplotlib.pyplot as plt
#
# data=[0,1,2,3,4,5]
# plt.plot(data)
# plt.show()

X=list(range(1,11))
Y=[n*n for n in X]
Z=[n*n*n for n in X]

plt.plot(X,Y,label="Y")
plt.plot(X,Z,label="Z")



plt.grid(True)
plt.show()