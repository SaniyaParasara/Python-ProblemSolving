# UNIT 5 - Q5: Write a program to perform basic data analysis using Pandas
#               DataFrame.
# SCENARIO: HR analyst explores an employee table: size, statistics, highest
#           salary, department-wise average, filtering and sorting.

import pandas as pd

df = pd.DataFrame({
    "EmpID":  [101, 102, 103, 104, 105, 106],
    "Name":   ["Amit", "Riya", "Karan", "Neha", "Dev", "Sana"],
    "Dept":   ["IT", "HR", "IT", "Finance", "HR", "IT"],
    "Salary": [55000, 48000, 62000, 51000, 45000, 70000],
    "Age":    [28, 32, 25, 40, 35, 30],
})

print("head(3):\n", df.head(3), "\n")
print("tail(2):\n", df.tail(2), "\n")
print("shape:", df.shape, "| size:", df.size, "| columns:", list(df.columns))
print("dtypes:\n", df.dtypes, "\n")
print("describe:\n", df.describe(), "\n")
print("Max salary:", df["Salary"].max(), "| Min age:", df["Age"].min())
print("Highest paid:", df.loc[df["Salary"].idxmax(), "Name"], "\n")

print("IT employees:\n", df[df["Dept"] == "IT"], "\n")
print("Salary > 50000 and Age < 35:\n", df[(df.Salary > 50000) & (df.Age < 35)], "\n")
print("Dept-wise average salary:\n", df.groupby("Dept")["Salary"].mean(), "\n")
print("Employees per dept:\n", df["Dept"].value_counts(), "\n")

df["Bonus"] = df["Salary"] * 0.10                       # new column
print("Sorted by Salary (desc):\n", df.sort_values("Salary", ascending=False)[["Name", "Salary", "Bonus"]])
df2 = df.set_index("EmpID")
print("\nloc[103]:\n", df2.loc[103])
