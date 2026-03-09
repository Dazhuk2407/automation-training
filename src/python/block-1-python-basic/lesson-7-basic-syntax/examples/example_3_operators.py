"""
Lesson 7: Example 3 - Operators
Демонстрація всіх типів операторів в Python
"""

print("=" * 50)
print("ARITHMETIC OPERATORS")
print("=" * 50)

x, y = 10, 3

print(f"x = {x}, y = {y}")
print(f"x + y = {x + y}       (addition)")
print(f"x - y = {x - y}       (subtraction)")
print(f"x * y = {x * y}       (multiplication)")
print(f"x / y = {x / y:.2f}     (division)")
print(f"x // y = {x // y}      (floor division)")
print(f"x % y = {x % y}       (modulo)")
print(f"x ** y = {x ** y}     (exponentiation)")

print("\n" + "=" * 50)
print("COMPARISON OPERATORS")
print("=" * 50)

a, b = 10, 5

print(f"a = {a}, b = {b}")
print(f"a == b → {a == b}     (equal to)")
print(f"a != b → {a != b}     (not equal to)")
print(f"a > b → {a > b}       (greater than)")
print(f"a < b → {a < b}       (less than)")
print(f"a >= b → {a >= b}     (greater or equal)")
print(f"a <= b → {a <= b}     (less or equal)")

print("\n" + "=" * 50)
print("LOGICAL OPERATORS")
print("=" * 50)

p, q = True, False

print(f"p = {p}, q = {q}")
print(f"p and q → {p and q}   (both must be True)")
print(f"p or q → {p or q}     (at least one True)")
print(f"not p → {not p}       (negation)")

print("\n" + "=" * 50)
print("COMPOUND OPERATIONS")
print("=" * 50)

# Compound assignment
x = 10
print(f"x = {x}")
x += 5
print(f"x += 5 → {x}")
x -= 3
print(f"x -= 3 → {x}")
x *= 2
print(f"x *= 2 → {x}")
x //= 3
print(f"x //= 3 → {x}")

print("\n" + "=" * 50)
print("OPERATOR PRECEDENCE")
print("=" * 50)

# Приклад пріоритету операторів
result = 2 + 3 * 4
print(f"2 + 3 * 4 = {result}  (3*4 first, then +2)")

result = (2 + 3) * 4
print(f"(2 + 3) * 4 = {result}  (parentheses have priority)")

result = 10 - 5 + 2
print(f"10 - 5 + 2 = {result}  (left to right)")

