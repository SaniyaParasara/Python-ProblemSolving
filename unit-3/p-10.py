# UNIT 3 - Q10: Write a program to extract specific information from a text
#                file using regular expressions.
# SCENARIO: HR department extracts names, emails, phone numbers and dates from
#           a bulk resume/contact file; an admin scans a server log for IPs.

import re, os

data = """Name: Amit Shah, Email: amit.shah@gmail.com, Phone: 9876543210, DOJ: 12-03-2022
Name: Riya Patel, Email: riya_p@yahoo.com, Phone: 9123456780, DOJ: 01-07-2023
Name: Karan Mehta, Email: karan@college.edu, Phone: 8899776655, DOJ: 25-11-2021
Server IP 192.168.1.10 failed login at 10:45:12
"""
with open("contacts.txt", "w") as f:
    f.write(data)

with open("contacts.txt") as f:
    content = f.read()

names  = re.findall(r"Name: ([A-Za-z ]+),", content)
emails = re.findall(r"[\w.]+@[\w.]+\.\w+", content)
phones = re.findall(r"\b[6-9]\d{9}\b", content)
dates  = re.findall(r"\d{2}-\d{2}-\d{4}", content)
ips    = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", content)
times  = re.findall(r"\d{2}:\d{2}:\d{2}", content)

print("Names  :", names)
print("Emails :", emails)
print("Phones :", phones)
print("Dates  :", dates)
print("IPs    :", ips, "| Times:", times)

print("\nGmail users:", [e for e in emails if e.endswith("gmail.com")])
print("Joined in 2022 or later:", [d for d in dates if int(d[-4:]) >= 2022])

with open("extracted.txt", "w") as out:          # save result
    for n, e, p in zip(names, emails, phones):
        out.write(f"{n} | {e} | {p}\n")
print("\nSaved to extracted.txt:\n" + open("extracted.txt").read())
os.remove("contacts.txt"); os.remove("extracted.txt")
