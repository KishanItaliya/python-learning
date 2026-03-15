# ============================================================
# LIST (list) in Python
# ============================================================
# Lists are ordered, mutable collections that can hold items
# of any type (including mixed types).
# Defined with square brackets [].
# ============================================================

# --- Creating lists ---
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, None]
empty = []

print(fruits)              # ['apple', 'banana', 'cherry']
print(type(fruits))        # <class 'list'>

# --- Indexing and slicing ---
print(fruits[0])           # apple    (first element)
print(fruits[-1])          # cherry   (last element)
print(numbers[1:4])        # [2, 3, 4]
print(numbers[::2])        # [1, 3, 5]  (every 2nd element)

# --- Lists are MUTABLE (can be modified in place) ---
fruits[1] = "blueberry"
print(fruits)              # ['apple', 'blueberry', 'cherry']

# --- Adding elements ---
fruits.append("date")      # adds to the end
print(fruits)              # ['apple', 'blueberry', 'cherry', 'date']

fruits.insert(1, "banana") # inserts at index 1
print(fruits)              # ['apple', 'banana', 'blueberry', 'cherry', 'date']

fruits.extend(["elderberry", "fig"])  # adds multiple items
print(fruits)

# --- Removing elements ---
fruits.remove("blueberry") # removes first occurrence
print(fruits)

popped = fruits.pop()      # removes and returns last item
print(popped)              # fig

popped = fruits.pop(1)     # removes and returns item at index 1
print(popped)              # banana

del fruits[0]              # deletes by index
print(fruits)

# --- Sorting ---
nums = [3, 1, 4, 1, 5, 9, 2, 6]
nums.sort()                # sorts in-place (ascending)
print(nums)                # [1, 1, 2, 3, 4, 5, 6, 9]

nums.sort(reverse=True)    # sorts descending
print(nums)                # [9, 6, 5, 4, 3, 2, 1, 1]

# sorted() returns a NEW sorted list without modifying the original
original = [5, 2, 8, 1]
new_sorted = sorted(original)
print(original)            # [5, 2, 8, 1]  (unchanged)
print(new_sorted)          # [1, 2, 5, 8]

# --- Other useful operations ---
nums = [1, 2, 3, 4, 5]
print(len(nums))           # 5
print(sum(nums))           # 15
print(min(nums))           # 1
print(max(nums))           # 5
print(nums.count(3))       # 1   (how many times 3 appears)
print(nums.index(4))       # 3   (index where 4 is found)

# --- List comprehension (powerful & Pythonic way to create lists) ---
squares = [x ** 2 for x in range(1, 6)]
print(squares)             # [1, 4, 9, 16, 25]

evens = [x for x in range(10) if x % 2 == 0]
print(evens)               # [0, 2, 4, 6, 8]

# --- Copying a list ---
a = [1, 2, 3]
b = a          # NOT a copy! b points to the same list
b.append(4)
print(a)       # [1, 2, 3, 4]  — a is also changed!

# Proper ways to copy:
c = a.copy()
d = a[:]
e = list(a)

# --- Nested lists (2D list / matrix) ---
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0])           # [1, 2, 3]   (first row)
print(matrix[1][2])        # 6           (row 1, column 2)

# --- Membership test ---
print("apple" in ["apple", "banana"])    # True
print(10 not in [1, 2, 3])              # True

# --- Unpacking a list ---
first, second, *rest = [10, 20, 30, 40, 50]
print(first)               # 10
print(second)              # 20
print(rest)                # [30, 40, 50]
