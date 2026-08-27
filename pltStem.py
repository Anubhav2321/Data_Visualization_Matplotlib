import matplotlib.pyplot as plt 

x= [1, 2, 3, 4, 5]
y = [10, 25, 15, 30, 20]
plt.stem(x, y)

plt.title("Stem Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()