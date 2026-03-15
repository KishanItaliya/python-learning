# ============================================================
# STRING (str) in Python
# ============================================================
# Strings are sequences of characters, enclosed in single (''),
# double (""), or triple (''' ''' / """ """) quotes.
# Strings are IMMUTABLE — once created, they cannot be changed.
# ============================================================

# --- Creating strings ---
s1 = 'Hello'
s2 = "World"
s3 = '''This is a
multi-line string'''
s4 = """Also a
multi-line string"""

print(s1)                  # Hello
print(type(s1))            # <class 'str'>
print(s3)

# --- String concatenation and repetition ---
greeting = s1 + " " + s2
print(greeting)            # Hello World

echo = "ha" * 3
print(echo)                # hahaha

# --- Indexing and slicing (0-based) ---
text = "Python"
print(text[0])             # P       (first character)
print(text[-1])            # n       (last character)
print(text[0:3])           # Pyt     (index 0, 1, 2)
print(text[2:])            # thon    (from index 2 to end)
print(text[::-1])          # nohtyP  (reversed string)

# --- Strings are immutable ---
# text[0] = "J"   # TypeError! You cannot change individual characters.

# --- String length ---
print(len(text))           # 6

# --- Useful string methods ---
msg = "  Hello, World!  "

print(msg.strip())         # "Hello, World!"  (removes leading/trailing whitespace)
print(msg.lstrip())        # "Hello, World!  "
print(msg.rstrip())        # "  Hello, World!"

name = "python programming"
print(name.upper())        # PYTHON PROGRAMMING
print(name.lower())        # python programming
print(name.title())        # Python Programming
print(name.capitalize())   # Python programming

print(name.count("p"))     # 2   (counts occurrences of "p")
print(name.find("gram"))   # 10  (index where "gram" starts, -1 if not found)
print(name.replace("python", "java"))  # java programming

# --- Checking string content ---
print("hello".isalpha())   # True  (only alphabetic characters)
print("123".isdigit())     # True  (only digits)
print("hello123".isalnum())# True  (alphanumeric)
print("   ".isspace())     # True  (only whitespace)
print("Hello".startswith("He"))  # True
print("Hello".endswith("lo"))    # True

# --- Split and Join ---
csv_line = "apple,banana,cherry"
fruits = csv_line.split(",")
print(fruits)              # ['apple', 'banana', 'cherry']

joined = " - ".join(fruits)
print(joined)              # apple - banana - cherry

# --- String formatting ---
name = "Kishan"
age = 25

# f-string (recommended, Python 3.6+)
print(f"My name is {name} and I am {age} years old.")

# .format() method
print("My name is {} and I am {} years old.".format(name, age))

# % formatting (older style)
print("My name is %s and I am %d years old." % (name, age))

# --- Escape characters ---
print("He said \"hello\"")        # He said "hello"
print("Line1\nLine2")             # prints on two lines
print("Tab\there")                # Tab    here
print("Backslash: \\")            # Backslash: \

# --- Raw strings (ignore escape characters) ---
print(r"C:\new_folder\test")      # C:\new_folder\test  (no escape processing)

# --- Membership test ---
print("Py" in "Python")           # True
print("Java" not in "Python")     # True
