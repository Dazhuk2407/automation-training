# Вправи — Lesson 11: Dictionaries

---

## 🏋️ Вправа 1: Основи (EASY)

**Файл:** `exercise_1_basics.py`

| Тест | Що перевірити |
|------|--------------|
| `test_access` | user["name"] == "Alice" |
| `test_length` | len(config) == 3 |
| `test_key_exists` | "host" є ключем config |
| `test_key_missing` | "password" немає в config |
| `test_value_in_values` | "Alice" є серед values |

---

## 🏋️ Вправа 2: Модифікація (EASY)

**Файл:** `exercise_2_modification.py`

| Тест | Що зробити |
|------|-----------|
| `test_add_key` | Додати "email" до user |
| `test_update_value` | Змінити role на "admin" |
| `test_delete_key` | Видалити "age" через del |
| `test_pop_key` | pop("role") та перевірити повернуте значення |
| `test_update_multiple` | update() з кількома ключами |

---

## 🏋️ Вправа 3: Ітерація (MEDIUM)

**Файл:** `exercise_3_iteration.py`

| Тест | Що зробити |
|------|-----------|
| `test_get_all_keys` | list(config.keys()) містить "host" |
| `test_get_all_values` | max(scores.values()) == 95 |
| `test_items_contain` | ("name", "Alice") є в user.items() |
| `test_no_none_values` | Жодне значення не None |

---

## 🏋️ Вправа 4: Словники як тестові дані (MEDIUM)

**Файл:** `exercise_4_test_data.py`

| Тест | Що зробити |
|------|-----------|
| `test_required_fields` | Перевірити наявність id, name, email |
| `test_status_code` | response["status"] == 200 |
| `test_nested_access` | Дістати name з вкладеної структури |
| `test_user_is_active` | user["active"] is True |

---

## ✅ Перевірка

```bash
pytest test_exercises.py -v
```