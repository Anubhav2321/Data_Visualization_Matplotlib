import matplotlib.pyplot as plt 
day =["Mon", "Tue", "Wed", "Thu", "Fri"]

python = [20, 34, 30, 35, 27]
java = [25, 32, 34, 20, 25]
sql = [15, 20, 25, 30, 35]
react = [10, 15, 20, 25, 30]
mongodb = [5, 10, 15, 20, 25]
plt.stackplot(day , python , java , sql , react , mongodb , labels=['Python', 'Java', 'SQL', 'React', 'MongoDB'])
plt.legend()
plt.title("Stack Plot")
plt.xlabel("Days")
plt.ylabel("Number of Students")
plt.show()

