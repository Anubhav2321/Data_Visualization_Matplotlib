import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]
size = [100, 200, 300, 400, 500]

plt.scatter(x, y, s=size)

plt.title("Simple Bubble Chart")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.show()