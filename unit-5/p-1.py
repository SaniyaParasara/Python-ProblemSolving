# UNIT 5 - Q1: Write a program to demonstrate different types of errors and
#               exceptions in Python.
# SCENARIO: An input-processing script (e.g. ATM or calculator) meets bad input
#           and system problems; knowing the error types helps debug quickly.
#
# 1. Syntax error  : mistake in grammar - detected before running
#                    e.g.  print("hi"          -> SyntaxError
# 2. Runtime error : happens while the program runs (exceptions)
# 3. Logical error : program runs but gives wrong output

# ---- Syntax error shown safely using compile() ----
try:
    compile("print(\"hi\"", "<demo>", "exec")
except SyntaxError as e:
    print("SyntaxError  :", e.msg)

# ---- Logical error ----
a, b = 80, 90
print("Wrong average  :", a + b / 2, "<- logical error (missing brackets)")
print("Correct average:", (a + b) / 2)

# ---- Runtime errors (built-in exceptions) ----
cases = {
    "ZeroDivisionError":  lambda: 10 / 0,
    "ValueError":         lambda: int("abc"),
    "TypeError":          lambda: "5" + 5,
    "IndexError":         lambda: [1, 2, 3][5],
    "KeyError":           lambda: {"a": 1}["b"],
    "NameError":          lambda: undefined_name,
    "AttributeError":     lambda: (5).append(1),
    "FileNotFoundError":  lambda: open("missing.txt"),
    "ImportError":        lambda: __import__("no_such_module"),
}
for name, fn in cases.items():
    try:
        fn()
    except Exception as e:
        print(f"{name:<18}-> {type(e).__name__}: {str(e)[:50]}")

# exception hierarchy
print("\nZeroDivisionError MRO:", [c.__name__ for c in ZeroDivisionError.__mro__])
