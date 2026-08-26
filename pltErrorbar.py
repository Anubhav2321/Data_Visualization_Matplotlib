import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

error = [2, 3, 2, 4, 3]

plt.errorbar(x, y, yerr=error, fmt='o-')

plt.title("Error Bar Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.grid(True)
plt.show()