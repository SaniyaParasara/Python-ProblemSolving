# 7. Write a program to create a dictionary and demonstrate dictionary methods and iteration.

# Create a dictionary
d = {"name": "Saniya", "age": 22, "city": "Rajkot"}

# Display the dictionary
print("Dictionary:", d)

# Update the value of an existing key
d.update({"age": 23})

# Add a new key-value pair
d["course"] = "Python"

# Iterate through the dictionary and display keys and values
for key, value in d.items():
    print(key, ":", value)
