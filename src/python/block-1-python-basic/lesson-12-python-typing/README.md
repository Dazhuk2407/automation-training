# Lesson 12: Python Typing and Type Hints

## 🎯 Learning Outcomes

- ✅ Розуміти динамічну vs статичну типізацію
- ✅ Використовувати type hints для функцій та змінних
- ✅ Працювати з typing модулем (List, Dict, Tuple, Set)
- ✅ Використовувати Optional, Union, Any
- ✅ Перевіряти типи з mypy
- ✅ Писати краще документований код

---

## 📖 Теорія

### 1. Динамічна Типізація Python

Python - динамічно типізована мова:

```python
# Тип визначається автоматично
x = 5           # int
x = "hello"     # str - тип змінився!
x = 3.14        # float
x = [1, 2, 3]   # list

# Це працює, але може викликати помилки
def add(a, b):
    return a + b

add(1, 2)       # 3 ✅
add("hello", "world")  # "helloworld" ✅
add(1, "hello")  # TypeError ❌
```

**Проблема:** Помилки виявляються лише під час виконання!

---

### 2. Type Hints (Підказки Типів)

Python 3.5+ дозволяє додавати type hints:

```python
# Функція з type hints
def add(x: int, y: int) -> int:
    """Додати два числа."""
    return x + y

# Змінні з type hints
name: str = "Alice"
age: int = 25
price: float = 19.99
is_active: bool = True
```

**Важливо:** Type hints НЕ перевіряються Python під час виконання!
Вони використовуються для:
- 📝 Документації
- 🔍 Статичного аналізу (mypy, pyright)
- 💡 Автодоповнення в IDE

---

### 3. Базові Type Hints

```python
# Прості типи
def greet(name: str) -> str:
    return f"Hello, {name}!"

def calculate_area(width: int, height: int) -> int:
    return width * height

def get_price() -> float:
    return 19.99

def is_valid(data: str) -> bool:
    return len(data) > 0

# None як результат
def log_message(message: str) -> None:
    print(message)
    # Нічого не повертає
```

---

### 4. Typing Module - Контейнери

#### List - Список

```python
from typing import List

# Список цілих чисел
numbers: List[int] = [1, 2, 3, 4, 5]

# Список рядків
names: List[str] = ["Alice", "Bob", "Charlie"]

# Функція яка приймає та повертає список
def get_even_numbers(numbers: List[int]) -> List[int]:
    return [n for n in numbers if n % 2 == 0]
```

#### Dict - Словник

```python
from typing import Dict

# Словник: ключі string, значення int
ages: Dict[str, int] = {
    "Alice": 25,
    "Bob": 30
}

# Словник з різними типами значень
from typing import Any
user: Dict[str, Any] = {
    "name": "Alice",
    "age": 25,
    "is_active": True
}

# Функція
def count_words(text: str) -> Dict[str, int]:
    words = text.split()
    return {word: words.count(word) for word in set(words)}
```

#### Tuple - Кортеж

```python
from typing import Tuple

# Координати (фіксована довжина)
coords: Tuple[float, float] = (10.5, 20.3)

# RGB колір
color: Tuple[int, int, int] = (255, 128, 0)

# Функція повертає кортеж
def get_min_max(numbers: List[int]) -> Tuple[int, int]:
    return min(numbers), max(numbers)
```

#### Set - Множина

```python
from typing import Set

# Унікальні значення
unique_ids: Set[int] = {1, 2, 3, 4, 5}

# Функція
def get_unique_words(text: str) -> Set[str]:
    return set(text.lower().split())
```

---

### 5. Optional - Може бути None

```python
from typing import Optional

# Може бути str або None
def find_user(user_id: int) -> Optional[str]:
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)  # Повертає str або None

# Змінна
result: Optional[int] = None
result = 42

# Еквівалент Union[str, None]
name: Optional[str] = None
```

---

### 6. Union - Кілька типів

```python
from typing import Union

# Може бути int або float
def square(number: Union[int, float]) -> Union[int, float]:
    return number ** 2

# Може бути str або list
def process(data: Union[str, List[str]]) -> List[str]:
    if isinstance(data, str):
        return [data]
    return data
```

---

### 7. Any - Будь-який тип

```python
from typing import Any

# Приймає будь-що
def print_value(value: Any) -> None:
    print(value)

# Словник з будь-якими значеннями
config: Dict[str, Any] = {
    "name": "App",
    "version": 1.0,
    "debug": True
}
```

**⚠️ Обережно з `Any`:** Він вимикає перевірку типів для цього значення. mypy не знайде помилок. Використовуйте `Any` тільки коли реально не знаєте тип заздалегідь (наприклад, JSON config). Якщо тип відомий — краще `Union` або конкретний тип.

---

### 8. Callable - Функція як параметр

```python
from typing import Callable

# Функція яка приймає функцію
def apply_twice(func: Callable[[int], int], value: int) -> int:
    return func(func(value))

def double(x: int) -> int:
    return x * 2

result = apply_twice(double, 5)  # 20
```

---

### 9. Перевірка типів з mypy

```bash
# Встановлення
pip install mypy

# Перевірка файлу
mypy your_file.py

# Конфігурація .mypy.ini
[mypy]
python_version = 3.12
warn_return_any = True
warn_unused_configs = True
disallow_untyped_defs = True
```

**Приклад помилки:**

```python
def add(x: int, y: int) -> int:
    return x + y

# mypy знайде помилку:
add("hello", "world")  # error: Argument 1 has incompatible type "str"; expected "int"
```

---

### 10. Таблиця Typing Types

| Type | Опис | Приклад |
|------|------|---------|
| `List[T]` | Список типу T | `List[int]` |
| `Dict[K, V]` | Словник: ключ K, значення V | `Dict[str, int]` |
| `Tuple[T1, T2]` | Кортеж з типами | `Tuple[int, str]` |
| `Set[T]` | Множина типу T | `Set[str]` |
| `Optional[T]` | T або None | `Optional[int]` |
| `Union[T1, T2]` | T1 або T2 | `Union[int, float]` |
| `Any` | Будь-який тип | `Any` |
| `Callable` | Функція | `Callable[[int], str]` |

---

### 11. Сучасний синтаксис (Python 3.10+)

Починаючи з Python 3.10, можна писати простіше — без імпорту з `typing`:

```python
# Python 3.9+: вбудовані типи з маленької літери
def get_names() -> list[str]:    # замість List[str]
    return ["Alice", "Bob"]

ages: dict[str, int] = {}        # замість Dict[str, int]

# Python 3.10+: оператор | замість Union та Optional
def square(n: int | float) -> int | float:   # замість Union[int, float]
    return n ** 2

name: str | None = None           # замість Optional[str]
```

**У цьому курсі** ми використовуємо класичний синтаксис через `typing` — він працює в усіх версіях Python 3.5+.

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`
