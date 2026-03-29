# Вправи — Lesson 13: Sets

---

## 🏋️ Вправа 1: Основи (EASY)

**Файл:** `exercise_1_basics.py`

| Тест | Що перевірити |
|------|--------------|
| `test_unique_elements` | {1, 2, 2, 3, 3} має 3 елементи |
| `test_add_element` | Додати "critical" до tags |
| `test_discard_safe` | discard неіснуючого — без помилки |
| `test_membership` | 200 є в {200, 301, 404} |
| `test_empty_set_type` | set() — це set, а {} — це dict |

---

## 🏋️ Вправа 2: Операції (MEDIUM)

**Файл:** `exercise_2_operations.py`

| Тест | Що зробити |
|------|-----------|
| `test_union` | smoke \| api — об'єднання |
| `test_intersection` | smoke & regression — спільні |
| `test_difference` | regression - smoke — тільки в regression |
| `test_subset` | smoke <= regression |
| `test_disjoint` | unit та e2e не мають спільних |

---

## 🏋️ Вправа 3: У тестах (MEDIUM)

**Файл:** `exercise_3_tests.py`

| Тест | Що зробити |
|------|-----------|
| `test_required_fields` | required issubset response |
| `test_no_duplicates` | len(ids) == len(set(ids)) |
| `test_new_features` | v2 - v1 — нові функції |
| `test_deduplicate` | Прибрати дублікати зі списку |

---

## ✅ Перевірка

```bash
pytest test_exercises.py -v
```