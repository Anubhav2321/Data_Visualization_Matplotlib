import numpy as np 
import matplotlib.pyplot as plt

data1 = np.random.normal(50, 10, 100)
data2 = np.random.normal(60, 5, 100)
data3 = np.random.normal(70, 17, 100)

data = [data1, data2, data3]
plt.violinplot(data)
plt.title("Violin Plot")
plt.xlabel("Data Sets")
plt.ylabel("Values")
plt.grid(True)
plt.show()