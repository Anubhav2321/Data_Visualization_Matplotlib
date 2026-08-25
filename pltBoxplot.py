import matplotlib.pyplot as plt
marks =[45, 50, 78, 96, 88, 92, 75, 80, 32, 12, 65, 70, 85, 90, 100, 55, 60, 72, 82, 95]

plt.boxplot(marks)
plt.title("Boxplot of Student Marks")
plt.ylabel("Marks")
plt.show()