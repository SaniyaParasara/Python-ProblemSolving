# 47. Write a Python program to handle missing data using dropna and fillna methods.

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name": ["Saniya", "Rahul", "Priya", "Amit"],
    "Age": [22, np.nan, 23, 25],
    "Marks": [85, 78, np.nan, np.nan],
})
print("Original:\n", df)
print("\nMissing values:\n", df.isnull().sum())

print("\nAfter dropna():\n", df.dropna())
print("\nfillna(0):\n", df.fillna(0))
print("\nFill with column mean:\n", df.fillna(df.mean(numeric_only=True)))
print("\nForward fill:\n", df.ffill())
