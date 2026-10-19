# 48. Write a Python program to plot line, bar, histogram and pie charts using Python.

import matplotlib.pyplot as plt

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Line chart
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
axs[0, 0].plot(x, y, marker="o", color="blue")
axs[0, 0].set_title("Line Chart")

# Bar chart
subjects = ["Maths", "Science", "English", "Hindi"]
scores = [85, 90, 78, 88]
axs[0, 1].bar(subjects, scores, color="green")
axs[0, 1].set_title("Bar Chart")

# Histogram
data = [22, 25, 25, 27, 30, 30, 30, 32, 35, 35, 38, 40, 41, 45]
axs[1, 0].hist(data, bins=5, color="orange", edgecolor="black")
axs[1, 0].set_title("Histogram")

# Pie chart
axs[1, 1].pie([40, 30, 20, 10], labels=["A", "B", "C", "D"], autopct="%1.1f%%")
axs[1, 1].set_title("Pie Chart")

plt.tight_layout()
plt.show()
