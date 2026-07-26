# Вправи — Lesson 24: Failed First

У всіх вправах функція `failed_first` (симуляція `pytest --ff`) **уже надана**
у файлі. Ваша задача — написати `assert`, що перевіряють її поведінку.

```python
def failed_first(all_tests, last_results):
    failed = [t for t in all_tests if last_results.get(t) == "failed"]
    rest = [t for t in all_tests if last_results.get(t) != "failed"]
    return failed + rest
```

---

## 🏋️ Вправа 1: Перевірка `failed_first` (EASY)

**Файл:** `exercise_1_ff.py`

| Тест | Що перевірити |
|------|--------------|
| `test_single_failed_first` | впалий `test_b` стає першим: `[test_a, test_b, test_c]` → `[test_b, test_a, test_c]` |
| `test_all_tests_present` | результат містить усі вихідні тести (нічого не пропущено) |
| `test_no_failures_keeps_order` | якщо нічого не впало — порядок незмінний |
| `test_two_failed_first` | обидва впалі (`test_b`, `test_d`) йдуть перед passing |
| `test_length_preserved` | довжина результату дорівнює довжині вхідного списку |

---

## 🏋️ Вправа 2: Порядок і крайні випадки (MEDIUM)

**Файл:** `exercise_2_ordering.py`

| Тест | Що перевірити |
|------|--------------|
| `test_relative_order_failed` | серед впалих зберігається їх взаємний порядок |
| `test_relative_order_rest` | серед passing зберігається їх взаємний порядок |
| `test_unknown_goes_to_rest` | тест без запису в кеші трактується як не-впалий |
| `test_empty_cache_keeps_order` | порожній кеш (перший прогін) → звичайний порядок |
| `test_failed_prefix` | перші N елементів результату — це саме впалі тести |

---

## 🏋️ Вправа 3: Виправ очікуваний порядок (MEDIUM)

**Файл:** `exercise_3_fix_ff.py`

Один тест навмисно падає: очікуваний порядок у `assert` **неправильний**.

**Завдання:**
1. Запустіть файл — один тест падає
2. Прочитайте вивід pytest: який реальний порядок повертає `failed_first`?
3. Виправте очікуване значення в `assert`
4. Заповніть блок `# ВІДПОВІДЬ:`

---

## ✅ Перевірка

```bash
pytest test_exercises.py -v
```

### Критерії:

- [ ] Всі тести у вправах 1–2 проходять
- [ ] У кожному тесті написано `assert` (не залишено `pass`)
- [ ] Вправа 3 виправлена — очікуваний порядок відповідає реальному
- [ ] Блок `# ВІДПОВІДЬ:` у вправі 3 заповнено
