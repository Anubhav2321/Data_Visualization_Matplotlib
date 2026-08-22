import numpy as np
import matplotlib.pyplot as plt

# Number of data points
n = 50

# Generate random X and Y values
x = np.random.rand(n) * 100
y = np.random.rand(n) * 100

# Generate random market size for each point
market_size = np.random.rand(n) * 1000 + 50

# Create scatter plot with different marker sizes
plt.scatter(x, y, s=market_size, alpha=0.6)

# Add title and axis labels
plt.title("Scatter Plot of Random X and Y Values")
plt.xlabel("X Values")
plt.ylabel("Y Values")

# Add grid
plt.grid(True)

# Display the plot
plt.show()