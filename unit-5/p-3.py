# UNIT 5 - Q3: Write a program to define and raise user-defined exceptions.
# SCENARIO: Bank app raises its own InsufficientBalanceError; election system
#           raises UnderAgeError; login raises InvalidPasswordError.

class BankError(Exception):                      # base custom exception
    pass

class InsufficientBalanceError(BankError):
    def __init__(self, balance, amount):
        self.balance, self.amount = balance, amount
        super().__init__(f"Cannot withdraw Rs.{amount}; balance is Rs.{balance}")

class UnderAgeError(Exception):
    pass

class InvalidPasswordError(Exception):
    def __init__(self, msg="Password must be 8+ chars with a digit"):
        super().__init__(msg)

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError(balance, amount)
    return balance - amount

def check_age(age):
    if age < 18:
        raise UnderAgeError(f"Age {age} < 18, cannot vote")
    return "Eligible"

def check_password(p):
    if len(p) < 8 or not any(c.isdigit() for c in p):
        raise InvalidPasswordError()
    return "Strong"

for fn, args in ((withdraw, (1000, 500)), (withdraw, (1000, 5000)),
                 (check_age, (25,)), (check_age, (16,)),
                 (check_password, ("abc",)), (check_password, ("python123",))):
    try:
        print(fn.__name__, args, "->", fn(*args))
    except BankError as e:                        # catches child classes too
        print("BankError  :", e)
    except (UnderAgeError, InvalidPasswordError) as e:
        print(type(e).__name__, ":", e)

# raising manually / re-raising
try:
    try:
        int("x")
    except ValueError:
        print("Logging error, re-raising...")
        raise
except ValueError as e:
    print("Caught again:", e)
