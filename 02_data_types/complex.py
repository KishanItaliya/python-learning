# ============================================================
# COMPLEX NUMBERS (complex) in Python
# ============================================================
# A complex number has a real part and an imaginary part.
# Written as:  a + bj   (Python uses 'j' instead of 'i')
# Useful in engineering, physics, and signal processing.
# ============================================================

# --- Creating complex numbers ---
z1 = 3 + 4j
z2 = complex(2, -5)       # complex(real, imaginary)
z3 = complex("1+2j")      # from string (no spaces allowed inside)

print(z1)                  # (3+4j)
print(z2)                  # (2-5j)
print(z3)                  # (1+2j)
print(type(z1))            # <class 'complex'>

# --- Accessing real and imaginary parts ---
print(z1.real)             # 3.0
print(z1.imag)             # 4.0

# --- Conjugate: flips the sign of the imaginary part ---
print(z1.conjugate())      # (3-4j)

# --- Arithmetic with complex numbers ---
a = 2 + 3j
b = 1 - 1j

print(a + b)               # (3+2j)
print(a - b)               # (1+4j)
print(a * b)               # (5+1j)     [(2)(1) + (2)(-j) + (3j)(1) + (3j)(-j) = 2 -2j +3j +3 = 5+j]
print(a / b)               # (-0.5+2.5j)

# --- Magnitude (absolute value) of a complex number ---
# |a + bj| = sqrt(a^2 + b^2)
print(abs(z1))             # 5.0   (sqrt(9 + 16) = 5)

# --- Using the cmath module for complex math ---
import cmath

print(cmath.phase(z1))     # 0.9272... (angle in radians)
print(cmath.polar(z1))     # (5.0, 0.9272...) — (magnitude, phase)
print(cmath.rect(5, 0.927))  # roughly (3+4j) — polar to rectangular

print(cmath.sqrt(-1))      # 1j  (square root of -1)
print(cmath.exp(1j * cmath.pi))  # roughly (-1+0j) — Euler's formula: e^(iπ) = -1

# --- You CANNOT compare complex numbers with < or > ---
# print(z1 > z2)  # TypeError! Complex numbers are not orderable.
# But you can check equality:
print((1 + 2j) == complex(1, 2))  # True
