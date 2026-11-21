import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr","May","Jun"]
sales = [15000,18000,12000,22000,25000,20000]

fig, axs = plt.subplots(3, 1, figsize=(8,12))

# Line Plot
axs[0].plot(months, sales, marker='o', color='blue')
axs[0].set_title("Line Plot")

# Scatter Plot
axs[1].scatter(months, sales, color='red')
axs[1].set_title("Scatter Plot")

# Bar Plot
axs[2].bar(months, sales, color='green')
axs[2].set_title("Bar Plot")

plt.tight_layout()
plt.show()
