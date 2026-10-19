# 45. Write a Python program to perform basic data analysis using Pandas DataFrame.

import pandas as pd

data = {
    "Name": ["Saniya", "Rahul", "Priya", "Amit", "Neha"],
    "Age": [22, 24, 23, 25, 22],
    "Marks": [85, 78, 92, 66, 88],
    "City": ["Surat", "Pune", "Surat", "Delhi", "Pune"],
}
df = pd.DataFrame(data)

print(df)
print("\nShape:", df.shape)
print("\nInfo:"); df.info()
print("\nStatistics:\n", df.describe())
print("\nMean marks:", df["Marks"].mean())
print("Max marks:", df["Marks"].max())
print("\nStudents with marks > 80:\n", df[df["Marks"] > 80])
print("\nSorted by marks:\n", df.sort_values("Marks", ascending=False))
print("\nAverage marks by city:\n", df.groupby("City")["Marks"].mean())
