import matplotlib.pyplot as plt

# Data
students = ["Rahul", "Anubhav", "Amit", "Priya"]

math = [20, 25, 18, 22]
science = [25, 30, 22, 28]
english = [30, 25, 27, 30]

plt.bar(students, math, label="Math")
plt.bar(students, science, bottom=math, label="Science")

plt.bar(students, english, bottom=[math[i] + science[i] for i in range(len(students))], label="English")

plt.title("Student Marks - Stacked Bar Chart")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.legend()

plt.show()