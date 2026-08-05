# Practical No. 5

# Question:
# Write a program to demonstrate the use of
# break, continue and pass statements.

# Definition:
# break    -> Terminates the loop immediately.
# continue -> Skips the current iteration and
#             continues with the next iteration.
# pass     -> Does nothing. It is used as a
#             placeholder statement.

# ------------------ BREAK ------------------

print("Break Statement")

for i in range(1, 6):

    if i == 4:
        break      # Stops the loop when i becomes 4

    print(i)

# ---------------- CONTINUE -----------------

print("\nContinue Statement")

for i in range(1, 6):

    if i == 3:
        continue   # Skips number 3

    print(i)

# ------------------ PASS -------------------

print("\nPass Statement")

for i in range(1, 6):

    if i == 3:
        pass       # Does nothing

    print(i)
