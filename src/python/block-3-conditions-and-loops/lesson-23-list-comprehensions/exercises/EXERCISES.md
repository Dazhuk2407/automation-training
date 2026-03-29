# Вправи — Lesson 23: List Comprehensions

## 🏋️ Вправа 1: List comprehension (EASY)

| Тест | Що зробити |
|------|-----------|
| `test_squares` | [n**2 for n in range(1,6)] |
| `test_filter_errors` | Тільки коди >= 400 |
| `test_upper_names` | Імена в upper case |
| `test_ternary_labels` | "OK"/"ERROR" для кодів |

## 🏋️ Вправа 2: Dict та set (MEDIUM)

| Тест | Що зробити |
|------|-----------|
| `test_dict_from_lists` | dict comprehension з zip |
| `test_unique_domains` | set comprehension з email |
| `test_filter_config` | Dict comp — тільки truthy |

## 🏋️ Вправа 3: Практичні (MEDIUM)

| Тест | Що зробити |
|------|-----------|
| `test_extract_ids` | [u["id"] for u in users] |
| `test_active_names` | Імена active users |
| `test_name_map` | {name: id} через dict comp |

## ✅ Перевірка

```bash
pytest test_exercises.py -v
```