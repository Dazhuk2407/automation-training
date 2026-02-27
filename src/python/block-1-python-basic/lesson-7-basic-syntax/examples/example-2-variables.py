"""
Lesson 7: Example 2 - Variables and Assignment
Демонстрація роботи зі змінними та присвоюванням
"""

# === ОСНОВНІ ТИПИ ЗМІННИХ ===

# String - текст
name = "Alice"
greeting = "Hello, World!"
multiline = """This is
a multiline
string"""

# Integer - ціле число
age = 25
count = -10
year = 2024

# Float - число з комою
height = 5.7
temperature = -5.5
pi = 3.14159

# Boolean - істина/неправда
is_student = True
is_employed = False
has_experience = True

# None - відсутність значення
result = None
data = None

print("=== Basic Variables ===")
print(f"Name: {name}, Type: {type(name)}")
print(f"Age: {age}, Type: {type(age)}")
print(f"Height: {height}, Type: {type(height)}")
print(f"Is Student: {is_student}, Type: {type(is_student)}")
print(f"Result: {result}, Type: {type(result)}")

# === МНОЖЕСТВЕННЕ ПРИСВОЮВАННЯ ===
x, y, z = 1, 2, 3
print(f"\n=== Multiple Assignment ===")
print(f"x={x}, y={y}, z={z}")

# === SWAP ЗМІННИХ ===
a, b = 10, 20
print(f"\n=== Before Swap ===")
print(f"a={a}, b={b}")

a, b = b, a
print(f"\n=== After Swap ===")
print(f"a={a}, b={b}")

# === ПРАВИЛА НАЗВУВАННЯ ===
valid_name = "OK"           # ✅ lowercase_with_underscores
_private_var = "OK"         # ✅ приватна змінна
CONSTANT_VALUE = 100        # ✅ константа UPPERCASE
counter = 0                 # ✅ описане ім'я

print(f"\n=== Variable Naming ===")
print(f"valid_name: {valid_name}")
print(f"_private_var: {_private_var}")
print(f"CONSTANT_VALUE: {CONSTANT_VALUE}")

