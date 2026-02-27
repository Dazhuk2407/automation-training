"""
Lesson 11: Example 1 - Basic Built-in Functions
"""
# len() - довжина
print("len([1,2,3]) =", len([1, 2, 3]))
print("len('hello') =", len('hello'))
# type() - тип
print("\ntype(42) =", type(42))
print("type('hello') =", type('hello'))
# isinstance() - перевірка типу
print("\nisinstance(42, int) =", isinstance(42, int))
print("isinstance('hello', str) =", isinstance('hello', str))
# range() - послідовність
print("\nlist(range(5)) =", list(range(5)))
print("list(range(2, 7)) =", list(range(2, 7)))
# enumerate() - індекс + значення
print("\nEnumerate:")
for i, val in enumerate(['a', 'b', 'c']):
    print(f"  {i}: {val}")
