import matplotlib.pyplot as plt 

marks = [45, 66 ,75, 75, 95, 58, 42, 67, 71, 89, 92, 45, 57, 68, 75, 83, 95, 40, 55, 57, 75, 69, 58]
plt.hist(marks , bins=5)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.grid(True)
plt.show()