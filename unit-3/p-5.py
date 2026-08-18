# Q5. Write a program to display current date and time using datetime module
from datetime import datetime

now = datetime.now()
print("Current date and time:", now)
print("Date:", now.date())
print("Time:", now.time())
print("Formatted:", now.strftime("%d-%m-%Y %H:%M:%S"))