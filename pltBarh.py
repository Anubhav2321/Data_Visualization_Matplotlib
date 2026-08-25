import matplotlib.pyplot as plt 

product =["Laptop", "Mobile", "Tablet", "Desktop", "PS5", "Xbox", "Switch", "VR Headset"]
sales =[150, 300, 200, 100, 250, 180, 220, 90]

plt.barh(product, sales, color='orange')
plt.title("Product Sales - Horizontal Bar Chart")
plt.xlabel("Sales")
plt.ylabel("Products")
plt.show()
