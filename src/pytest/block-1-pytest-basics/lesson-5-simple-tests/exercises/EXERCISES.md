# Вправи — Lesson 5: Прості тести для базових типів

---

## 🏋️ Вправа 1: Тести для чисел (EASY)

**Файл:** `exercise_1_numbers.py`

Напишіть тести для базових операцій з числами.

| Тест | Що перевірити |
|------|--------------|
| `test_addition` | 5 + 3 == 8 |
| `test_subtraction` | 10 - 4 == 6 |
| `test_multiplication` | 3 * 7 == 21 |
| `test_integer_division` | 10 // 3 == 3 |
| `test_modulo` | 10 % 3 == 1 |
| `test_negative` | abs(-15) == 15 |

---

## 🏋️ Вправа 2: Тести для рядків (EASY)

**Файл:** `exercise_2_strings.py`

Напишіть тести для рядкових операцій.

| Тест | Що перевірити |
|------|--------------|
| `test_upper` | "hello".upper() == "HELLO" |
| `test_lower` | "WORLD".lower() == "world" |
| `test_contains` | "test" є підрядком "pytest" |
| `test_not_contains` | "java" немає в "python" |
| `test_starts_with` | "https://example.com" починається з "https://" |
| `test_split` | "a,b,c".split(",") == ["a", "b", "c"] |

---

## 🏋️ Вправа 3: Тести для колекцій (MEDIUM)

**Файл:** `exercise_3_collections.py`

Напишіть тести для списків та словників.

**Списки:**

| Тест | Що перевірити |
|------|--------------|
| `test_list_length` | len([1, 2, 3, 4, 5]) == 5 |
| `test_list_first_last` | перший == 1, останній == 5 |
| `test_list_membership` | "apple" є в ["apple", "banana"] |
| `test_list_sorted` | sorted([3, 1, 2]) == [1, 2, 3] |

**Словники:**

| Тест | Що перевірити |
|------|--------------|
| `test_dict_access` | user["name"] == "Alice" |
| `test_dict_key_exists` | "name" є ключем словника |
| `test_dict_key_missing` | "phone" НЕ є ключем |
| `test_dict_get_default` | user.get("phone") is None |

---

## 🏋️ Вправа 4: Порівняння float (MEDIUM)

**Файл:** `exercise_4_float.py`

Напишіть тести з використанням `pytest.approx`.

| Тест | Що перевірити |
|------|--------------|
| `test_float_sum` | 0.1 + 0.2 приблизно 0.3 |
| `test_division` | 1 / 3 приблизно 0.333 (abs=0.001) |
| `test_pi` | 22 / 7 приблизно 3.14 (abs=0.01) |

---

## 🏋️ Вправа 5: Edge cases (MEDIUM)

**Файл:** `exercise_5_edge_cases.py`

Напишіть окремий тест для кожного граничного випадку.

| Тест | Що перевірити |
|------|--------------|
| `test_empty_list` | len([]) == 0 |
| `test_empty_string` | len("") == 0 |
| `test_empty_dict` | len({}) == 0 |
| `test_empty_is_falsy` | not [] (порожній список — False) |
| `test_set_removes_duplicates` | len({1, 1, 2, 2, 3}) == 3 |
| `test_none_check` | None is None |

---

## ✅ Перевірка

```bash
pytest test_exercises.py -v
```

### Критерії:

- [ ] Всі тести проходять
- [ ] Кожен тест містить `assert`
- [ ] Один тест — одна ідея (без "комбайнних" тестів)
- [ ] Використано `pytest.approx` для float