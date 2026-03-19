# Вправи - Lesson 10: Data Types

## 🏋️ Завдання 1: Всі основні типи (EASY)

Створіть файл `exercise_1_all_types.py`:

```python
"""
Вправа 1: Створити змінні всіх 5 типів та перевірити їх
"""


def get_all_types():
    """
    Повернути словник зі змінними всіх 5 основних типів.

    Returns:
        dict з ключами: 'str', 'int', 'float', 'bool', 'none'
    """
    # TODO: створіть змінні та поверніть словник
    return {
        'str': ...,
        'int': ...,
        'float': ...,
        'bool': ...,
        'none': ...,
    }


if __name__ == "__main__":
    types = get_all_types()
    for name, value in types.items():
        print(f"{name:5s} → value={value!r:15s} type={type(value)}")
```

**Очікуваний результат (приклад):**
```
str   → value='Hello'         type=<class 'str'>
int   → value=42              type=<class 'int'>
float → value=3.14            type=<class 'float'>
bool  → value=True            type=<class 'bool'>
none  → value=None            type=<class 'NoneType'>
```

---

## 🏋️ Завдання 2: Конверсія типів (EASY)

Створіть файл `exercise_2_type_conversion.py`:

```python
"""
Вправа 2: Конверсія між типами
"""


def convert_to_int(value):
    """Конвертувати значення в int."""
    # TODO: return int(value)
    pass


def convert_to_float(value):
    """Конвертувати значення в float."""
    # TODO: return float(value)
    pass


def convert_to_str(value):
    """Конвертувати значення в str."""
    # TODO: return str(value)
    pass


def convert_to_bool(value):
    """Конвертувати значення в bool."""
    # TODO: return bool(value)
    pass


if __name__ == "__main__":
    print(f"int('42') = {convert_to_int('42')}")
    print(f"float('3.14') = {convert_to_float('3.14')}")
    print(f"str(100) = {convert_to_str(100)!r}")
    print(f"bool(0) = {convert_to_bool(0)}")
    print(f"bool('hello') = {convert_to_bool('hello')}")
```

---

## 🏋️ Завдання 3: Truthy / Falsy (MEDIUM)

Створіть файл `exercise_3_truthy_falsy.py`:

```python
"""
Вправа 3: Визначити які значення truthy, а які falsy
"""


def is_truthy(value):
    """
    Повернути True якщо значення truthy, False якщо falsy.

    Args:
        value: будь-яке значення

    Returns:
        bool
    """
    # TODO: реалізуйте
    pass


if __name__ == "__main__":
    test_values = [0, 1, -1, 0.0, 3.14, "", "hello", "False",
                   [], [0], {}, None, True, False]

    for val in test_values:
        print(f"is_truthy({val!r:10s}) → {is_truthy(val)}")
```

**Зверніть увагу:** `"False"` — це непорожній рядок, тому він truthy!

---

## 🏋️ Завдання 4: Безпечна конверсія (MEDIUM)

Створіть файл `exercise_4_safe_convert.py`:

```python
"""
Вправа 4: Безпечна конверсія значень
"""


def safe_int(value, default=0):
    """
    Безпечно конвертувати значення в int.
    Якщо конверсія неможлива — повернути default.

    Args:
        value: значення для конверсії
        default: значення за замовчуванням (0)

    Returns:
        int
    """
    # TODO: використайте try/except для обробки ValueError та TypeError
    pass


if __name__ == "__main__":
    print(f"safe_int('42') = {safe_int('42')}")          # 42
    print(f"safe_int('abc') = {safe_int('abc')}")         # 0
    print(f"safe_int(None) = {safe_int(None)}")           # 0
    print(f"safe_int('??', -1) = {safe_int('??', -1)}")   # -1
    print(f"safe_int('100', -1) = {safe_int('100', -1)}") # 100
```

---

## 🏋️ Завдання 5: Калькулятор з конверсією (HARD)

Створіть файл `exercise_5_calculator.py`:

```python
"""
Вправа 5: Калькулятор, що приймає рядки та числа
"""


def add_values(a, b):
    """
    Додати два значення, конвертувавши їх у float.
    Якщо хоча б одне значення не можна конвертувати — повернути None.

    Args:
        a: перше значення (str, int, або float)
        b: друге значення (str, int, або float)

    Returns:
        float або None
    """
    # TODO: спробуйте float(a) + float(b)
    # Якщо ValueError або TypeError — поверніть None
    pass


if __name__ == "__main__":
    print(f"add_values(10, 20) = {add_values(10, 20)}")         # 30.0
    print(f"add_values('10', '20') = {add_values('10', '20')}") # 30.0
    print(f"add_values('3.5', 2) = {add_values('3.5', 2)}")     # 5.5
    print(f"add_values('abc', 5) = {add_values('abc', 5)}")     # None
    print(f"add_values(None, 5) = {add_values(None, 5)}")       # None
```

---

## ✅ Перевірка

```bash
pytest test_exercises.py -v
```

### Критерії:
- [ ] Всі файли створено
- [ ] Всі тести проходять
- [ ] Код використовує правильні типи та конверсії
- [ ] safe_int() обробляє помилки