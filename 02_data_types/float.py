# ============================================================
# FLOAT (float) in Python
# ============================================================
# Floats represent real numbers with a decimal point.
# Internally stored as 64-bit double-precision (IEEE 754),
# which gives ~15-17 significant decimal digits of precision.
# ============================================================

# --- Basic float assignments ---
a = 3.14
b = -0.5
c = 0.0

print(a, b, c)           # 3.14 -0.5 0.0
print(type(a))            # <class 'float'>

# --- Scientific notation ---
speed_of_light = 3e8      # 3 × 10^8 = 300000000.0
tiny = 1.5e-4             # 0.00015

print(speed_of_light)     # 300000000.0
print(tiny)               # 0.00015

# --- Arithmetic operations ---
print(a + b)              # 2.64
print(a * 2)              # 6.28
print(a / 2)              # 1.57
print(a ** 2)             # 9.8596
print(a // 1)             # 3.0  (floor division still returns float)

# --- Floating-point precision gotcha ---
print(0.1 + 0.2)          # 0.30000000000000004 (NOT exactly 0.3!)
print(0.1 + 0.2 == 0.3)   # False

# To handle precision, use round() or the decimal module
print(round(0.1 + 0.2, 1))          # 0.3
print(round(0.1 + 0.2, 1) == 0.3)   # True

# --- Creating floats from other types ---
print(float(5))           # 5.0    (int to float)
print(float("3.14"))      # 3.14   (string to float)
print(float("inf"))       # inf    (positive infinity)
print(float("-inf"))      # -inf   (negative infinity)
print(float("nan"))       # nan    (not a number)

# --- Special float values ---
import math

print(math.inf)           # inf
print(math.nan)           # nan
print(math.isnan(float("nan")))  # True
print(math.isinf(float("inf"))) # True

# --- Useful methods and functions ---
x = 3.7
print(round(x))           # 4       (rounds to nearest int)
print(round(x, 0))        # 4.0     (rounds but returns float when ndigits given)
print(math.floor(x))      # 3       (always rounds down)
print(math.ceil(x))       # 4       (always rounds up)
print(math.trunc(x))      # 3       (truncates toward zero)

# --- float method: is_integer() ---
print((4.0).is_integer())   # True  (no fractional part)
print((4.5).is_integer())   # False

# --- float to fraction representation ---
print((0.75).as_integer_ratio())  # (3, 4) means 3/4 = 0.75
