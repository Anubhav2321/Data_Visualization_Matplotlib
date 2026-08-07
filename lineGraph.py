import matplotlib.pyplot as plt 

subject =["English", "math", "science", "history", "computer"]
marks = [85, 90, 78, 92, 88]
plt.plot(subject, marks, marker="o")
plt.title("Student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.grid(True)
plt.show()