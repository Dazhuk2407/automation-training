"""
Lesson 11: Example 3 - Advanced Functions
"""
# sorted() - сортування
print("sorted([3,1,4,1,5]) =", sorted([3, 1, 4, 1, 5]))
print("sorted([3,1,2], reverse=True) =", sorted([3,1,2], reverse=True))
# zip() - об'єднати
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
print("\nzip(['Alice','Bob'],  [25,30,35]):")
for name, age in zip(names, ages):
    print(f"  {name}: {age}")
# all() - всі True?
print("\nall([True, True, True]) =", all([True, True, True]))
print("all([True, False, True]) =", all([True, False, True]))
# any() - хоч один True?
print("\nany([False, False, True]) =", any([False, False, True]))
print("any([False, False, False]) =", any([False, False, False]))
# reversed() - реверс
print("\nlist(reversed([1,2,3])) =", list(reversed([1, 2, 3])))
