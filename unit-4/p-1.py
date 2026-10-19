# UNIT 4 - Q1: Write a program to create a class and object in Python.
# SCENARIO: A library system represents each book as an object with title,
#           author and price, and behaviour such as discount calculation.

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def discount_price(self, percent):
        return self.price - self.price * percent / 100

    def display(self):
        print(f"{self.title} by {self.author} - Rs.{self.price}")

b1 = Book("Python Basics", "Guido", 500)       # objects
b2 = Book("Data Science", "Wes", 800)
b1.display()
b2.display()
print("Discounted price of b1:", b1.discount_price(10))
print("Type:", type(b1), "| Attribute:", b2.title)
b1.price = 550                                  # modify attribute
print("Updated:", b1.price, "| Has author?", hasattr(b1, "author"))
