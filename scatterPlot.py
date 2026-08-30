import numpy as np
import matplotlib.pyplot as plt

n = 50

x = np.random.rand(n) * 100
y = np.random.rand(n) * 100

market_size = np.random.rand(n) * 1000 + 50

plt.scatter(x, y, s=market_size, alpha=0.6)

plt.title("Scatter Plot of Random X and Y Values")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.grid(True)

plt.show()