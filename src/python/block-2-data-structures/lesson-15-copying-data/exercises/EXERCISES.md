# Вправи — Lesson 15: Copying Data

---

## 🏋️ Вправа 1: Shallow copy (EASY)

**Файл:** `exercise_1_shallow.py`

| Тест | Що зробити |
|------|-----------|
| `test_list_copy` | .copy() списку — оригінал не змінюється |
| `test_dict_copy` | .copy() словника — оригінал не змінюється |
| `test_spread_copy` | {**d} — створити копію з додатковим ключем |

---

## 🏋️ Вправа 2: Deep copy (MEDIUM)

**Файл:** `exercise_2_deep.py`

| Тест | Що зробити |
|------|-----------|
| `test_shallow_fails_nested` | Показати що shallow copy не копіює вкладений list |
| `test_deep_copy_safe` | deepcopy вкладеної структури — оригінал чистий |
| `test_nested_dict_deep` | deepcopy dict з вкладеними dict |

---

## 🏋️ Вправа 3: Тестові дані (MEDIUM)

**Файл:** `exercise_3_test_data.py`

| Тест | Що зробити |
|------|-----------|
| `test_factory_returns_fresh` | Фабрика повертає нову копію кожен раз |
| `test_modify_copy_not_original` | Зміна копії не впливає на оригінал |
| `test_two_copies_independent` | Дві копії незалежні одна від одної |

---

## ✅ Перевірка

```bash
pytest test_exercises.py -v
```