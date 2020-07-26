import matplotlib.pyplot as plt

jobs =[60,70,90,50]
languages=["java","c++","python","HTML"]

# plt.plot(languages,jobs)
# plt.show()
plt.pie(jobs,labels=languages)
plt.legend()
plt.show()
