# ============================================================
# BOOLEAN (bool) in Python
# ============================================================
# Booleans represent one of two values: True or False.
# bool is a subclass of int — True is 1, False is 0.
# Used extensively in conditions, loops, and logic.
# ============================================================

# --- Basic boolean values ---
a = True
b = False

print(a, b)               # True False
print(type(a))             # <class 'bool'>

# --- bool is a subclass of int ---
print(isinstance(True, int))   # True
print(True + True)             # 2   (1 + 1)
print(True * 10)               # 10
print(False + 5)               # 5

# --- Comparison operators return booleans ---
print(10 > 5)              # True
print(10 == 5)             # False
print(10 != 5)             # True
print(10 <= 10)            # True

# --- Logical operators: and, or, not ---
print(True and False)      # False (both must be True)
print(True or False)       # True  (at least one True)
print(not True)            # False (flips the value)

# --- Chained comparisons ---
x = 15
print(10 < x < 20)        # True  (same as: 10 < x and x < 20)

# --- Truthy and Falsy values ---
# Python treats certain values as False in a boolean context:
#   False, 0, 0.0, 0j, "", [], (), {}, set(), None, range(0)
# Everything else is Truthy.

print(bool(0))             # False
print(bool(""))            # False
print(bool([]))            # False
print(bool(None))          # False

print(bool(1))             # True
print(bool("hello"))       # True
print(bool([1, 2]))        # True
print(bool(-1))            # True  (any non-zero number is truthy)

# --- Using booleans in if statements ---
name = "Kishan"
if name:
    print(f"Hello, {name}!")     # prints because non-empty string is truthy
else:
    print("Name is empty")

# --- The bool() function ---
print(bool(42))            # True
print(bool(0))             # False
print(bool("False"))       # True  (non-empty string — the word "False" is truthy!)

# --- Short-circuit evaluation ---
# 'and' returns the first falsy value, or the last value if all truthy
print(1 and 2 and 3)       # 3
print(1 and 0 and 3)       # 0

# 'or' returns the first truthy value, or the last value if all falsy
print(0 or "" or "hello")  # "hello"
print(0 or "" or [])       # []
