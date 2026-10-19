# 46. Write a Python program to create a DataFrame from CSV or Excel files.

import pandas as pd
import os

# Create a sample CSV file
with open("students.csv", "w") as f:
    f.write("Name,Age,Marks\nSaniya,22,85\nRahul,24,78\nPriya,23,92\n")

df_csv = pd.read_csv("students.csv")
print("Data from CSV:\n", df_csv)
print("\nFirst 2 rows:\n", df_csv.head(2))

# Excel (requires: pip install openpyxl)
try:
    df_csv.to_excel("students.xlsx", index=False)
    df_excel = pd.read_excel("students.xlsx")
    print("\nData from Excel:\n", df_excel)
    os.remove("students.xlsx")
except ImportError:
    print("Install openpyxl to work with Excel files")
os.remove("students.csv")
