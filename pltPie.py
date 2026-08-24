import matplotlib.pyplot as plt

subject =["Java", "Python", "C++", "JavaScript"]
marks = [85, 95, 65, 40]

plt.pie(marks, labels=subject, autopct='%1.1f%%',)

plt.title("Marks Distribution in Subjects")
plt.show()