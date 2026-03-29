# Вправи — Lesson 10: Tuples

---

## 🏋️ Вправа 1: Основи (EASY)

**Файл:** `exercise_1_basics.py`

| Тест | Що перевірити |
|------|--------------|
| `test_create_tuple` | (10, 20, 30) має довжину 3 |
| `test_single_element` | (42,) — це tuple, а (42) — int |
| `test_first_element` | Перший елемент (200, "OK") == 200 |
| `test_last_element` | Останній елемент через [-1] |
| `test_membership` | 404 є в (200, 301, 404, 500) |
| `test_immutable` | Спроба змінити tuple кидає TypeError |

---

## 🏋️ Вправа 2: Unpacking (EASY)

**Файл:** `exercise_2_unpacking.py`

| Тест | Що зробити |
|------|-----------|
| `test_basic_unpacking` | Розпакувати (10, 20) у x, y |
| `test_three_values` | Розпакувати ("Alice", "admin", True) |
| `test_ignore_value` | Розпакувати (200, "OK") ігноруючи message |
| `test_star_unpacking` | first, *rest = (1, 2, 3, 4) |
| `test_swap` | Обміняти a, b через tuple unpacking |

---

## 🏋️ Вправа 3: Функції з tuples (MEDIUM)

**Файл:** `exercise_3_functions.py`

Напишіть функції та тести:

| Функція | Повертає | Тест |
|---------|---------|------|
| `min_max(numbers)` | tuple (min, max) | `test_min_max` |
| `split_name(full_name)` | tuple (first, last) | `test_split_name` |
| `http_status(code)` | tuple (code, message) | `test_http_status` |

---

## 🏋️ Вправа 4: Tuples як тестові дані (MEDIUM)

**Файл:** `exercise_4_test_data.py`

| Тест | Що зробити |
|------|-----------|
| `test_valid_codes` | Перевірити що 200 є в VALID_CODES |
| `test_error_codes` | Перевірити що 500 є в ERROR_CODES |
| `test_parametrize` | Написати parametrize тест для функції |

---

## ✅ Перевірка

```bash
pytest test_exercises.py -v
```