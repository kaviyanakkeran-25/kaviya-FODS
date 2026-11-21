import matplotlib.pyplot as plt

# Example dataset
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [15000, 18000, 12000, 22000, 25000, 20000]

# 2. Bar Plot
plt.figure(figsize=(8,5))   # create another figure
plt.bar(months, sales, color='orange')
plt.title("Monthly Sales - Bar Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(axis='y')
plt.show()   # show bar plot

