import matplotlib.pyplot as plt
student =["Anubhva", "Avik","Abhishek", "Soham", "Rohit", "Rajesh", "Rohan"]
marks = [85, 90, 78, 92, 88, 95, 80]
plt.bar(student, marks, color='green')
plt.title("Calculate Students Marks")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.show()