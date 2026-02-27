# Приклади роботи зі змінними та типами даних

# Integer
age = 25
count = -10
print(f"Age: {age}, type: {type(age)}")

# String
name = "Alice"
greeting = f"Hello, {name}!"
print(greeting)

# Float
price = 19.99
discount = 0.1
final_price = price * (1 - discount)
print(f"Price: ${final_price:.2f}")

# Boolean
is_student = True
is_employed = False
print(f"Is student: {is_student}, Is employed: {is_employed}")

# Type checking
print(f"Type of age: {type(age)}")
print(f"Is age an integer? {isinstance(age, int)}")

# Type conversion
string_number = "42"
number = int(string_number)
print(f"Converted: {number}, type: {type(number)}")

# Multiple assignment
x, y, z = 1, 2, 3
print(f"x={x}, y={y}, z={z}")

# Swap variables
a, b = 10, 20
a, b = b, a
print(f"After swap: a={a}, b={b}")


