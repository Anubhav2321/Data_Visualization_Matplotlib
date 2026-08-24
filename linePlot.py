import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# Create line plot
plt.plot(x, y)

# Add labels and title
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Simple Line Plot")

# Show grid
plt.grid(True)

# Display the graph
plt.show()
