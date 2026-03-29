# Вправи — Lesson 12: Safe Dictionary Access

---

## 🏋️ Вправа 1: .get() основи (EASY)

**Файл:** `exercise_1_get_basics.py`

| Тест | Що перевірити |
|------|--------------|
| `test_get_existing` | .get("name") повертає "Alice" |
| `test_get_missing_none` | .get("email") повертає None |
| `test_get_with_default` | .get("age", 0) повертає 0 |
| `test_get_does_not_modify` | .get() не змінює словник |
| `test_bracket_raises` | [] кидає KeyError при відсутньому ключі |

---

## 🏋️ Вправа 2: Вкладені словники (MEDIUM)

**Файл:** `exercise_2_nested.py`

| Тест | Що зробити |
|------|-----------|
| `test_nested_safe_access` | Дістати name з response["data"]["user"] через .get() |
| `test_missing_level` | Якщо "data" відсутній — повернути default |
| `test_nested_list` | Дістати першого user зі списку users |

---

## 🏋️ Вправа 3: Реальні сценарії (MEDIUM)

**Файл:** `exercise_3_real_scenarios.py`

| Тест | Що зробити |
|------|-----------|
| `test_config_defaults` | host є, port та timeout — default |
| `test_optional_field` | email відсутній → None |
| `test_required_vs_optional` | id через [], email через .get() |
| `test_fallback_value` | nickname → fallback на name |

---

## 🏋️ Вправа 4: setdefault() (MEDIUM)

**Файл:** `exercise_4_setdefault.py`

| Тест | Що зробити |
|------|-----------|
| `test_setdefault_adds` | setdefault додає ключ якщо немає |
| `test_setdefault_keeps` | setdefault не змінює існуючий ключ |
| `test_group_errors` | Використати setdefault для групування |

---

## ✅ Перевірка

```bash
pytest test_exercises.py -v
```