# Вправи - Lesson 12: Python Typing

## 🏋️ Завдання 1: Базові type hints (EASY)

Створіть файл `exercise_1_basic_type_hints.py`:

```python
"""
Вправа 1: Додайте type hints до функцій
"""


def add(x, y):
    """Додати два цілі числа."""
    return x + y


def concat(a, b):
    """Об'єднати два рядки через пробіл."""
    return f"{a} {b}"


def is_adult(age):
    """Повернути True якщо вік >= 18."""
    return age >= 18


def repeat_text(text, times):
    """Повторити текст N разів."""
    return text * times


if __name__ == "__main__":
    print(add(5, 3))            # 8
    print(concat("Hello", "World"))  # "Hello World"
    print(is_adult(25))         # True
    print(repeat_text("ha", 3)) # "hahaha"
```

**Завдання:** Додайте type hints до всіх параметрів та return types.

---

## 🏋️ Завдання 2: Контейнерні типи (EASY)

Створіть файл `exercise_2_container_types.py`:

```python
"""
Вправа 2: Функції з List, Dict, Tuple, Set
"""
from typing import List, Dict, Tuple, Set


def get_even_numbers(numbers: List[int]) -> List[int]:
    """Повернути тільки парні числа."""
    # TODO: реалізуйте
    pass


def count_words(text: str) -> Dict[str, int]:
    """Порахувати кількість кожного слова."""
    # TODO: реалізуйте
    pass


def get_min_max(numbers: List[int]) -> Tuple[int, int]:
    """Повернути (мінімум, максимум)."""
    # TODO: реалізуйте
    pass


def get_unique_words(text: str) -> Set[str]:
    """Повернути множину унікальних слів (в lowercase)."""
    # TODO: реалізуйте
    pass


if __name__ == "__main__":
    print(get_even_numbers([1, 2, 3, 4, 5, 6]))  # [2, 4, 6]
    print(count_words("hello world hello"))        # {'hello': 2, 'world': 1}
    print(get_min_max([5, 2, 9, 1, 7]))           # (1, 9)
    print(get_unique_words("Hello hello World"))    # {'hello', 'world'}
```

---

## 🏋️ Завдання 3: Optional типи (MEDIUM)

Створіть файл `exercise_3_optional_types.py`:

```python
"""
Вправа 3: Функції що можуть повертати None
"""
from typing import Optional, List


def find_first_negative(numbers: List[int]) -> Optional[int]:
    """
    Знайти перше від'ємне число.
    Повернути None якщо від'ємних немає.
    """
    # TODO: реалізуйте
    pass


def safe_divide(a: float, b: float) -> Optional[float]:
    """
    Поділити a на b.
    Повернути None якщо b == 0.
    """
    # TODO: реалізуйте
    pass


def find_user(users: List[str], name: str) -> Optional[int]:
    """
    Знайти індекс користувача за іменем.
    Повернути None якщо не знайдено.
    """
    # TODO: реалізуйте
    pass


if __name__ == "__main__":
    print(find_first_negative([1, 2, -3, 4]))   # -3
    print(find_first_negative([1, 2, 3]))        # None

    print(safe_divide(10, 3))   # 3.333...
    print(safe_divide(10, 0))   # None

    print(find_user(["Alice", "Bob"], "Bob"))     # 1
    print(find_user(["Alice", "Bob"], "Charlie")) # None
```

---

## 🏋️ Завдання 4: Union та Any (MEDIUM)

Створіть файл `exercise_4_union_and_any.py`:

```python
"""
Вправа 4: Union для кількох типів, Any для конфігурації
"""
from typing import Union, Any, Dict


def format_value(value: Union[int, float, str]) -> str:
    """
    Форматувати значення для виводу.
    - int/float: додати "Value: " перед числом
    - str: додати "Text: " перед рядком
    """
    # TODO: реалізуйте
    pass


def get_config_value(config: Dict[str, Any], key: str) -> Any:
    """
    Отримати значення з конфігурації за ключем.
    Повернути None якщо ключ відсутній.
    """
    # TODO: реалізуйте
    pass


if __name__ == "__main__":
    print(format_value(42))        # "Value: 42"
    print(format_value(3.14))      # "Value: 3.14"
    print(format_value("hello"))   # "Text: hello"

    config = {"name": "App", "version": 1.0, "debug": True}
    print(get_config_value(config, "name"))     # "App"
    print(get_config_value(config, "missing"))  # None
```

---

## 🏋️ Завдання 5: Callable та вкладені типи (HARD)

Створіть файл `exercise_5_callable_and_nested.py`:

```python
"""
Вправа 5: Callable та вкладені типи
"""
from typing import List, Dict, Callable


def apply_to_all(
    items: List[int],
    func: Callable[[int], int]
) -> List[int]:
    """Застосувати функцію до кожного елемента."""
    # TODO: реалізуйте
    pass


def extract_names(
    users: List[Dict[str, str]]
) -> List[str]:
    """Витягнути всі імена з списку користувачів."""
    # TODO: реалізуйте (кожен user має ключ 'name')
    pass


def triple(x: int) -> int:
    return x * 3


if __name__ == "__main__":
    print(apply_to_all([1, 2, 3], triple))   # [3, 6, 9]
    print(apply_to_all([10, 20], lambda x: x + 1))  # [11, 21]

    users = [
        {"name": "Alice", "role": "admin"},
        {"name": "Bob", "role": "user"},
    ]
    print(extract_names(users))  # ["Alice", "Bob"]
```

---

## 🏋️ Завдання 6: mypy validation (HARD)

Створіть файл `exercise_6_mypy_validation.py`:

```python
"""
Вправа 6: Виправте 2 помилки типізації, щоб mypy не показував помилок.

Запустіть:
    mypy exercise_6_mypy_validation.py

Зараз mypy покаже 2 помилки. Знайдіть і виправте їх.
"""
from typing import List, Optional


def sum_numbers(numbers: List[int]) -> int:
    """Порахувати суму чисел."""
    return sum(numbers)


def find_longest(words: List[str]) -> str:  # ❌ BUG 1: може повернути None!
    """Знайти найдовше слово. Повернути None якщо список порожній."""
    if not words:
        return None
    return max(words, key=len)


def format_greeting(name: str, age: int) -> str:
    """Сформувати привітання."""
    return f"Hello {name}, you are {age} years old"


if __name__ == "__main__":
    print(sum_numbers([1, 2, 3]))
    print(find_longest(["hi", "hello", "hey"]))
    print(find_longest([]))
    print(format_greeting("Alice", "25"))  # ❌ BUG 2: "25" це str, а має бути int!
```

**Завдання:**
1. Запустіть `mypy exercise_6_mypy_validation.py` — побачите 2 помилки
2. **BUG 1:** `find_longest` повертає `None`, але return type каже `str`. Виправте на `Optional[str]`
3. **BUG 2:** `format_greeting` очікує `age: int`, але викликається з `"25"` (str). Виправте виклик
4. Запустіть mypy знову — має бути `Success: no issues found`

---

## ✅ Перевірка

```bash
pytest test_exercises.py -v
```

### Критерії:
- [ ] Всі файли створено
- [ ] Всі тести проходять
- [ ] Функції мають type hints
- [ ] mypy не знаходить помилок в exercise 6