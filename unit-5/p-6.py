# UNIT 5 - Q6: Write a program to create a DataFrame from CSV or Excel files.
# SCENARIO: Branch offices send monthly sales as CSV / Excel sheets; the head
#           office loads them into DataFrames to analyse together.
# (pip install pandas openpyxl)

import pandas as pd, os

# create sample source files
sales = pd.DataFrame({"Product": ["Pen", "Book", "Bag", "Bottle"],
                      "Qty": [100, 50, 20, 40], "Price": [10, 120, 650, 90]})
sales.to_csv("sales.csv", index=False)
sales.to_excel("sales.xlsx", sheet_name="Jan", index=False)

# ---- from CSV ----
df_csv = pd.read_csv("sales.csv")
print("From CSV:\n", df_csv, "\n")
print("Selected columns:\n", pd.read_csv("sales.csv", usecols=["Product", "Qty"]), "\n")

# ---- from Excel ----
df_xl = pd.read_excel("sales.xlsx", sheet_name="Jan")
df_xl["Total"] = df_xl["Qty"] * df_xl["Price"]
print("From Excel with Total:\n", df_xl, "\n")

# ---- from list / tuple (extra) ----
print(pd.DataFrame([[1, "A"], [2, "B"]], columns=["ID", "Grade"]), "\n")
print(pd.DataFrame([(1, "X"), (2, "Y")], columns=["ID", "Code"]), "\n")

df_xl.to_csv("report.csv", index=False)                  # save back
print("report.csv saved:", os.path.exists("report.csv"))
for f in ("sales.csv", "sales.xlsx", "report.csv"):
    os.remove(f)
