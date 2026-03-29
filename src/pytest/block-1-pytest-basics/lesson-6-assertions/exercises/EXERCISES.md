# Вправи — Lesson 6: Assertions

---

## 🏋️ Вправа 1: Порівняння та boolean (EASY)

**Файл:** `exercise_1_comparison.py`

| Тест | Що перевірити |
|------|--------------|
| `test_equality` | 10 == 10 |
| `test_inequality` | "hello" != "world" |
| `test_greater` | 15 > 10 |
| `test_truthiness` | `True` є truthy (використовуйте `assert condition`, не `assert condition is True`) |
| `test_none` | `None` перевіряється через `is None` |
| `test_not_none` | число 42 не є None |

---

## 🏋️ Вправа 2: Типи та належність (EASY)

**Файл:** `exercise_2_types_and_membership.py`

| Тест | Що перевірити |
|------|--------------|
| `test_isinstance_int` | 42 — це int |
| `test_isinstance_str` | "hello" — це str |
| `test_isinstance_multiple` | 3.14 — це int або float |
| `test_in_list` | 3 є в [1, 2, 3] |
| `test_in_string` | "test" є підрядком "pytest" |
| `test_not_in_dict` | "phone" немає серед ключів {"name": "Alice"} |

---

## 🏋️ Вправа 3: Винятки (MEDIUM)

**Файл:** `exercise_3_exceptions.py`

Напишіть тести, які перевіряють що код кидає правильний виняток.

| Тест | Код | Очікуваний виняток |
|------|-----|-------------------|
| `test_zero_division` | `10 / 0` | `ZeroDivisionError` |
| `test_value_error` | `int("abc")` | `ValueError` |
| `test_key_error` | `{}["missing"]` | `KeyError` |
| `test_error_message` | `int("xyz")` | `ValueError` з текстом "invalid literal" |

---

## 🏋️ Вправа 4: Assert з повідомленнями (MEDIUM)

**Файл:** `exercise_4_messages.py`

Додайте assert з message **тільки де це дійсно потрібно**.

| Тест | Завдання |
|------|---------|
| `test_simple_no_message` | `assert 2 + 2 == 4` — message НЕ потрібен |
| `test_with_context` | перевірте що user є в списку, з message для контексту |
| `test_precondition` | перевірте що список не порожній перед роботою з ним |

---

## 🏋️ Вправа 5: Розуміння pytest diff (MEDIUM)

**Файл:** `exercise_5_introspection.py`

Ця вправа — для розуміння assert introspection.

**Завдання:**
1. Запустіть файл — один тест навмисно падає
2. Прочитайте вивід pytest: що він показує?
3. Заповніть коментар у файлі: що саме відрізняється у двох словниках?
4. Виправте тест щоб він проходив

---

## ✅ Перевірка

```bash
pytest test_exercises.py -v
```

### Критерії:

- [ ] Всі тести проходять
- [ ] Використано правильний стиль: `assert condition`, не `assert condition is True`
- [ ] Використано `isinstance()`, не `type() == ...`
- [ ] pytest.raises з `match` у вправі 3
- [ ] Message тільки де потрібен контекст