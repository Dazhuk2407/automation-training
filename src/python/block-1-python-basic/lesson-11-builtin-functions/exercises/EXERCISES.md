# Вправи - Lesson 11: Built-in Functions

## 🏋️ Завдання 1: len(), type(), isinstance() (EASY)

Створіть файл `exercise_1_info_functions.py`:

```python
"""
Вправа 1: Функції для отримання інформації про об'єкти
"""


def get_object_info(obj):
    """
    Повернути інформацію про об'єкт.

    Args:
        obj: будь-який об'єкт

    Returns:
        dict з ключами:
        - 'length': довжина (або None якщо len() не підтримується)
        - 'type_name': назва типу як рядок (наприклад 'int', 'str', 'list')
        - 'is_numeric': True якщо obj це int або float
    """
    # TODO: реалізуйте
    pass


if __name__ == "__main__":
    print(get_object_info("hello"))    # {'length': 5, 'type_name': 'str', 'is_numeric': False}
    print(get_object_info([1, 2, 3]))  # {'length': 3, 'type_name': 'list', 'is_numeric': False}
    print(get_object_info(42))         # {'length': None, 'type_name': 'int', 'is_numeric': True}
    print(get_object_info(3.14))       # {'length': None, 'type_name': 'float', 'is_numeric': True}
```

**Підказка:** Для length використайте `try/except TypeError` щоб обробити об'єкти без len().

---

## 🏋️ Завдання 2: range(), enumerate() (EASY)

Створіть файл `exercise_2_sequences.py`:

```python
"""
Вправа 2: Робота з послідовностями
"""


def even_numbers(n):
    """
    Повернути список парних чисел від 0 до n включно.

    Args:
        n: верхня межа

    Returns:
        list[int]
    """
    # TODO: використайте range() з кроком 2
    pass


def numbered_items(items):
    """
    Повернути список рядків виду "1. apple", "2. banana", ...

    Args:
        items: список елементів

    Returns:
        list[str]
    """
    # TODO: використайте enumerate() з start=1
    pass


if __name__ == "__main__":
    print(even_numbers(10))  # [0, 2, 4, 6, 8, 10]
    print(numbered_items(['apple', 'banana', 'cherry']))
    # ['1. apple', '2. banana', '3. cherry']
```

---

## 🏋️ Завдання 3: sum(), min(), max(), abs(), round() (MEDIUM)

Створіть файл `exercise_3_math_functions.py`:

```python
"""
Вправа 3: Математичні функції для аналізу даних
"""


def analyze_numbers(numbers):
    """
    Розрахувати статистику для списку чисел.

    Args:
        numbers: список чисел (не порожній)

    Returns:
        dict з ключами: 'sum', 'min', 'max', 'average', 'range'
        average округлити до 2 знаків
    """
    # TODO: використайте sum(), min(), max(), len(), round()
    pass


def absolute_values(numbers):
    """
    Повернути список абсолютних значень.

    Args:
        numbers: список чисел (можуть бути від'ємні)

    Returns:
        list[float]
    """
    # TODO: використайте abs() для кожного елемента
    pass


if __name__ == "__main__":
    stats = analyze_numbers([15, 3, 27, 8, 42, 1, 19])
    print(f"Stats: {stats}")
    # {'sum': 115, 'min': 1, 'max': 42, 'average': 16.43, 'range': 41}

    temps = [-5.7, 3.2, -1.8, 7.4, -3.1]
    print(f"Absolute temps: {absolute_values(temps)}")
    # [5.7, 3.2, 1.8, 7.4, 3.1]
```

---

## 🏋️ Завдання 4: sorted(), zip() (MEDIUM)

Створіть файл `exercise_4_sort_and_zip.py`:

```python
"""
Вправа 4: Сортування та об'єднання даних
"""


def sort_words(words):
    """
    Відсортувати слова трьома способами.

    Args:
        words: список рядків

    Returns:
        dict з ключами:
        - 'alphabetical': за алфавітом
        - 'reversed': за алфавітом у зворотному порядку
        - 'by_length': за довжиною слова
    """
    # TODO: використайте sorted() з різними параметрами
    pass


def make_dict(keys, values):
    """
    Створити словник з двох списків.

    Args:
        keys: список ключів
        values: список значень

    Returns:
        dict
    """
    # TODO: використайте zip() та dict()
    pass


if __name__ == "__main__":
    result = sort_words(['banana', 'apple', 'cherry', 'date', 'elderberry'])
    print(f"Alphabetical: {result['alphabetical']}")
    print(f"Reversed: {result['reversed']}")
    print(f"By length: {result['by_length']}")

    names = ['Alice', 'Bob', 'Charlie']
    ages = [25, 30, 35]
    print(f"Dict: {make_dict(names, ages)}")
    # {'Alice': 25, 'Bob': 30, 'Charlie': 35}
```

---

## 🏋️ Завдання 5: all(), any() (MEDIUM)

Створіть файл `exercise_5_all_any.py`:

```python
"""
Вправа 5: Перевірка умов для колекцій
"""


def check_numbers(numbers):
    """
    Перевірити властивості списку чисел.

    Args:
        numbers: список чисел

    Returns:
        dict з ключами:
        - 'all_positive': чи всі додатні (> 0)?
        - 'all_even': чи всі парні?
        - 'any_negative': чи є від'ємні?
        - 'any_greater_than_100': чи є більші за 100?
    """
    # TODO: використайте all() та any()
    pass


def check_passwords(passwords, min_length=6):
    """
    Перевірити список паролів.

    Args:
        passwords: список рядків
        min_length: мінімальна довжина пароля

    Returns:
        dict з ключами:
        - 'all_long_enough': чи всі довші за min_length?
        - 'any_has_digit': чи є хоч один з цифрою?
    """
    # TODO: використайте all(), any(), len(), str.isdigit() або any(c.isdigit() for c in pwd)
    pass


if __name__ == "__main__":
    print(check_numbers([2, 4, 6, 8, 10]))
    # {'all_positive': True, 'all_even': True, 'any_negative': False, 'any_greater_than_100': False}

    print(check_passwords(["abc", "password123", "qwerty", "MyP@ss1"]))
    # {'all_long_enough': False, 'any_has_digit': True}
```

---

## 🏋️ Завдання 6: Калькулятор статистики (HARD)

Створіть файл `exercise_6_statistics.py`:

```python
"""
Вправа 6: Калькулятор статистики з використанням вбудованих функцій
"""


def calculate_statistics(numbers):
    """
    Розрахувати статистику для списку чисел.

    Використайте: len(), sum(), min(), max(), sorted(), round()

    Args:
        numbers: Список чисел

    Returns:
        Словник з ключами:
        - count, total, average, minimum, maximum, range, sorted
    """
    # TODO: Реалізуйте
    pass


def print_report(students):
    """
    Вивести звіт по студентах.

    Використайте: enumerate(), sorted(), all(), any()

    Args:
        students: Список словників з 'name' та 'grade'
    """
    # TODO: Реалізуйте
    # 1. Виведіть нумерований список (enumerate)
    # 2. Відсортуйте за оцінкою (sorted з key)
    # 3. Перевірте: чи всі склали (grade >= 60)?
    # 4. Перевірте: чи є відмінники (grade >= 90)?
    pass


if __name__ == "__main__":
    numbers = [85, 72, 90, 68, 95, 78, 88]
    stats = calculate_statistics(numbers)
    print(f"Statistics: {stats}")

    students = [
        {'name': 'Alice', 'grade': 85},
        {'name': 'Bob', 'grade': 72},
        {'name': 'Charlie', 'grade': 90},
        {'name': 'Diana', 'grade': 68},
    ]
    print_report(students)
```

---

## ✅ Перевірка

```bash
pytest test_exercises.py -v
```

### Критерії:
- [ ] Код запускається без помилок
- [ ] Всі тести проходять
- [ ] Використано вбудовані функції (не ручні цикли)
- [ ] Результати відповідають очікуванням