# 38. Write a Python program to demonstrate encapsulation and abstraction using classes.

from abc import ABC, abstractmethod

# Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance                # Private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(300)
print("Balance:", acc.get_balance())

# Abstraction
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car starts with a key")

Car().start()
