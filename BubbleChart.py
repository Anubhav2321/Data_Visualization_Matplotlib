import numpy as np
import matplotlib.pyplot as plt

n = 50
x = np.random.rand(n) * 100
y = np.random.rand(n) * 100

size = np.random.rand(n) * 1000 + 50

plt.scatter(x, y, s=size, alpha=0.5)

plt.title("Bubble Chart")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.grid(True)
plt.show()