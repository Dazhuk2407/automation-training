# Вправи — Lesson 20: for Loops

---

## 🏋️ Вправа 1: Ітерація (EASY)

**Файл:** `exercise_1_basics.py`

| Тест | Що зробити |
|------|-----------|
| `test_sum_list` | Порахувати суму [10, 20, 30] через for |
| `test_count_chars` | Порахувати символи в рядку "hello" |
| `test_collect_keys` | Зібрати ключі словника в список |
| `test_range_squares` | Квадрати чисел 1-5 через range |

---

## 🏋️ Вправа 2: Збір результатів (MEDIUM)

**Файл:** `exercise_2_collecting.py`

| Тест | Що зробити |
|------|-----------|
| `test_filter_positive` | Залишити тільки > 0 |
| `test_uppercase_names` | Всі імена в upper case |
| `test_extract_ids` | Дістати id з list of dicts |

---

## 🏋️ Вправа 3: Вкладені цикли (MEDIUM)

**Файл:** `exercise_3_nested.py`

| Тест | Що зробити |
|------|-----------|
| `test_flatten` | Сплощити [[1,2],[3,4]] → [1,2,3,4] |
| `test_enumerate_errors` | Знайти індекси кодів >= 400 |
| `test_check_all_fields` | Вкладений цикл: users × required fields |

---

## 🏋️ Вправа 4: Цикли в тестах (MEDIUM)

**Файл:** `exercise_4_test_data.py`

| Тест | Що зробити |
|------|-----------|
| `test_all_emails_valid` | Кожен email містить "@" |
| `test_count_active` | Порахувати active users |
| `test_find_admin` | Знайти першого admin |

## ✅ Перевірка

```bash
pytest test_exercises.py -v
```