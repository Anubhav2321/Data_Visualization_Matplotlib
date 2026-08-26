import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5, 6]
y = [10, 20, 15, 30, 25, 40]

plt.plot(x, y)

plt.fill_between(x, y, alpha=0.3)

plt.title("Filled Area Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.grid(True)

plt.show()