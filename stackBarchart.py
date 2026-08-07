import matplotlib.pyplot as plt

# Data
students = ["Rahul", "Anubhav", "Amit", "Priya"]

math = [20, 25, 18, 22]
science = [25, 30, 22, 28]
english = [30, 25, 27, 30]

# Create stacked bar chart
plt.bar(students, math, label="Math")
plt.bar(students, science, bottom=math, label="Science")

# Calculate bottom for English
bottom_english = [math[i] + science[i] for i in range(len(students))]

plt.bar(students, english, bottom=bottom_english, label="English")

# Title and labels
plt.title("Student Marks - Stacked Bar Chart")
plt.xlabel("Students")
plt.ylabel("Marks")

# Show legend
plt.legend()

# Display chart
plt.show()