# Вправи — Lesson 16: range() та zip()

---

## 🏋️ Вправа 1: range() (EASY)

**Файл:** `exercise_1_range.py`

| Тест | Що зробити |
|------|-----------|
| `test_range_five` | range(5) → [0, 1, 2, 3, 4] |
| `test_range_start_stop` | range(3, 8) → [3, 4, 5, 6, 7] |
| `test_range_even` | Парні від 0 до 8 |
| `test_range_reverse` | [5, 4, 3, 2, 1] |

---

## 🏋️ Вправа 2: zip() та enumerate() (EASY)

**Файл:** `exercise_2_zip.py`

| Тест | Що зробити |
|------|-----------|
| `test_zip_pairs` | zip двох списків → list of tuples |
| `test_zip_to_dict` | dict(zip(keys, values)) |
| `test_enumerate_indices` | enumerate → [(0, "a"), (1, "b")] |
| `test_enumerate_start` | enumerate з start=1 |

---

## 🏋️ Вправа 3: Практичні сценарії (MEDIUM)

**Файл:** `exercise_3_practical.py`

| Тест | Що зробити |
|------|-----------|
| `test_generate_ids` | range(1, 6) для ID |
| `test_find_error_indices` | enumerate для пошуку кодів >= 400 |
| `test_build_users` | zip для побудови list of dicts |

---

## ✅ Перевірка

```bash
pytest test_exercises.py -v
```