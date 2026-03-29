# Вправи — Lesson 9: Lists

---

## 🏋️ Вправа 1: Основи (EASY)

**Файл:** `exercise_1_basics.py`

| Тест | Що перевірити |
|------|--------------|
| `test_first_element` | Перший елемент [10, 20, 30] == 10 |
| `test_last_element` | Останній елемент через [-1] == 30 |
| `test_length` | Довжина [200, 301, 404, 500] == 4 |
| `test_slice_first_two` | Перші 2 елементи [:2] |
| `test_slice_last_two` | Останні 2 елементи [-2:] |
| `test_membership` | "GET" є в ["GET", "POST", "PUT"] |

---

## 🏋️ Вправа 2: Методи (EASY)

**Файл:** `exercise_2_methods.py`

| Тест | Що зробити |
|------|-----------|
| `test_append` | Додати 500 до [200, 404], перевірити |
| `test_extend` | Додати [502, 503] до [200], перевірити |
| `test_remove` | Видалити "Bob" з ["Alice", "Bob", "Charlie"] |
| `test_pop_last` | pop() останній елемент, перевірити що повернув |
| `test_sort_ascending` | sorted([3, 1, 2]) == [1, 2, 3] |
| `test_sort_descending` | sorted з reverse=True |

---

## 🏋️ Вправа 3: Пошук та фільтрація (MEDIUM)

**Файл:** `exercise_3_search.py`

| Тест | Що зробити |
|------|-----------|
| `test_count_occurrences` | Порахувати скільки разів 200 зустрічається |
| `test_find_index` | Знайти індекс елемента 404 |
| `test_filter_errors` | Відфільтрувати коди >= 400 |
| `test_all_positive` | Перевірити що всі числа > 0 |

---

## 🏋️ Вправа 4: Списки як тестові дані (MEDIUM)

**Файл:** `exercise_4_test_data.py`

| Тест | Що зробити |
|------|-----------|
| `test_users_not_empty` | Список користувачів не порожній |
| `test_all_have_name` | Кожен user має ключ "name" |
| `test_active_count` | Порахувати active == True |
| `test_response_times_under_limit` | Всі часи < 1000ms |

---

## ✅ Перевірка

```bash
pytest test_exercises.py -v
```