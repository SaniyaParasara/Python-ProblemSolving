# UNIT 4 - Q8: Write a program to demonstrate encapsulation and abstraction
#               using classes.
# SCENARIO: ATM / bank: the balance is private (encapsulation) and changed only
#           through deposit/withdraw. Different account types implement an
#           abstract interest() method (abstraction).

from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, holder, balance):
        self.holder = holder              # public
        self._branch = "Rajkot"           # protected (convention)
        self.__balance = balance          # private (name-mangled)

    def deposit(self, amt):
        if amt > 0:
            self.__balance += amt
    def withdraw(self, amt):
        if 0 < amt <= self.__balance:
            self.__balance -= amt
        else:
            print("Invalid / insufficient funds")
    def get_balance(self):
        return self.__balance

    @abstractmethod
    def interest(self):                   # abstract method
        pass

class Savings(BankAccount):
    def interest(self): return self.get_balance() * 4 / 100
class Current(BankAccount):
    def interest(self): return 0

acc = Savings("Amit", 10000)
acc.deposit(2000); acc.withdraw(500); acc.withdraw(99999)
print("Balance :", acc.get_balance(), "| Interest:", acc.interest())
print("Direct private access ->", hasattr(acc, "__balance"))
print("Name-mangled          ->", acc._BankAccount__balance)
try:
    BankAccount("X", 1)
except TypeError as e:
    print("Abstract class error:", e)
print("Current interest:", Current("Riya", 5000).interest())
