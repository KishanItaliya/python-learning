# ============================================================
# INTEGER (int) in Python
# ============================================================
# Integers are whole numbers (no decimal point).
# They can be positive, negative, or zero.
# Python integers have unlimited precision — they can be
# as large as your memory allows.
# ============================================================

# --- Basic integer assignments ---
a = 10
b = -25
c = 0

print(a, b, c)          # 10 -25 0
print(type(a))           # <class 'int'>

# --- Arithmetic operations ---
print(a + b)             # -15   (addition)
print(a - b)             # 35    (subtraction)
print(a * b)             # -250  (multiplication)
print(a // 3)            # 3     (floor division — rounds down to nearest int)
print(a % 3)             # 1     (modulus — remainder after division)
print(a ** 3)            # 1000  (exponentiation — 10^3)

# --- Division always returns a float ---
print(a / 3)             # 3.3333...  (true division gives float)
print(type(a / 3))       # <class 'float'>

# --- Creating integers from other types ---
print(int(3.9))          # 3     (truncates decimal, does NOT round)
print(int("42"))         # 42    (string to int)
print(int("1010", 2))   # 10    (binary string to int, base 2)
print(int("ff", 16))    # 255   (hex string to int, base 16)

# --- Different number bases (literals) ---
binary_num = 0b1010      # binary literal
octal_num = 0o12         # octal literal
hex_num = 0xFF           # hexadecimal literal

print(binary_num)        # 10
print(octal_num)         # 10
print(hex_num)           # 255

# --- Useful built-in functions ---
print(abs(-7))           # 7     (absolute value)
print(pow(2, 10))        # 1024  (same as 2 ** 10)
print(divmod(17, 5))     # (3, 2) — returns (quotient, remainder)

# --- Unlimited precision ---
big = 10 ** 100
print(big)               # a 1 followed by 100 zeros (googol)
print(type(big))         # still <class 'int'>

# --- Checking if something is an integer ---
print(isinstance(42, int))       # True
print(isinstance(3.14, int))     # False
