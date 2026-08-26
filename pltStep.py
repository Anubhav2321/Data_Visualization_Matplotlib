import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 20, 35, 35]

plt.step(x, y)

plt.title("Step Plot")
plt.xlabel("Time")
plt.ylabel("Value")

plt.grid(True)
plt.show()