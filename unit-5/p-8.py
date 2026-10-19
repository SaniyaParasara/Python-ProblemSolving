# UNIT 5 - Q8: Write a program to plot line, bar, histogram and pie charts
#               using Python.
# SCENARIO: A shop owner prepares a monthly review: sales trend (line),
#           product comparison (bar), marks / age spread (histogram) and
#           category share (pie).
# (pip install matplotlib)

import matplotlib
matplotlib.use("Agg")           # remove this line to open windows on your PC
import matplotlib.pyplot as plt
import numpy as np

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales  = [12, 15, 14, 18, 22, 25]

plt.figure(figsize=(6, 4))
plt.plot(months, sales, marker="o", color="green", linestyle="--")
plt.title("Line Chart - Monthly Sales"); plt.xlabel("Month"); plt.ylabel("Sales (thousands)")
plt.grid(True); plt.savefig("line.png"); plt.close()

products, qty = ["Pen", "Book", "Bag", "Bottle"], [100, 60, 25, 45]
plt.figure(figsize=(6, 4))
plt.bar(products, qty, color=["red", "blue", "green", "orange"])
plt.title("Bar Chart - Product Quantity"); plt.ylabel("Units")
plt.savefig("bar.png"); plt.close()

marks = np.random.default_rng(0).normal(60, 15, 150)
plt.figure(figsize=(6, 4))
plt.hist(marks, bins=10, color="skyblue", edgecolor="black")
plt.title("Histogram - Marks Distribution"); plt.xlabel("Marks"); plt.ylabel("Students")
plt.savefig("hist.png"); plt.close()

plt.figure(figsize=(5, 5))
plt.pie([40, 25, 20, 15], labels=["IT", "HR", "Finance", "Sales"],
        autopct="%1.1f%%", explode=(0.1, 0, 0, 0), startangle=90)
plt.title("Pie Chart - Department Share")
plt.savefig("pie.png"); plt.close()

print("Saved: line.png, bar.png, hist.png, pie.png")
print("On your PC replace plt.savefig(...) with plt.show() to view the graph.")
