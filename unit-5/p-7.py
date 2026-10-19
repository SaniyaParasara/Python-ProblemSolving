# UNIT 5 - Q7: Write a program to handle missing data using dropna() and
#               fillna() methods.
# SCENARIO: A survey / sales sheet has blank cells. Before analysis, rows with
#           too many blanks are removed and others are filled with mean/zero.

import pandas as pd, numpy as np

df = pd.DataFrame({
    "Name":   ["Amit", "Riya", "Karan", "Neha", "Dev"],
    "Marks":  [82, np.nan, 67, np.nan, 55],
    "City":   ["Rajkot", "Surat", None, "Vadodara", "Rajkot"],
    "Attend": [90, 85, np.nan, 70, np.nan],
})
print("Original:\n", df, "\n")
print("isnull().sum():\n", df.isnull().sum(), "\n")

print("dropna()  (any NaN row):\n", df.dropna(), "\n")
print("dropna(subset=[Marks]):\n", df.dropna(subset=["Marks"]), "\n")
print("dropna(thresh=3):\n", df.dropna(thresh=3), "\n")

f = df.copy()
f["Marks"]  = f["Marks"].fillna(f["Marks"].mean())       # mean
f["City"]   = f["City"].fillna("Unknown")                # text
f["Attend"] = f["Attend"].fillna(0)                      # constant
print("fillna() cleaned:\n", f, "\n")

print("Forward fill:\n", df[["Marks", "Attend"]].ffill(), "\n")
print("fillna with dict:\n", df.fillna({"Marks": 0, "City": "NA", "Attend": 50}))
