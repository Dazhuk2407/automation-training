# Вправи — Lesson 23: Last Failed

---

## 🏋️ Вправа 1: Логіка відбору `--lf` (EASY)

**Файл:** `exercise_1_lf.py`

Функція `last_failed()` вже надана. Замініть `pass` на правильний `assert`.

| Тест | Що перевірити |
|------|--------------|
| `test_only_failed_selected` | впав лише `test_b` → повертається `["test_b"]` |
| `test_two_failed_keep_order` | впали `test_a` і `test_c` → `["test_a", "test_c"]` (порядок з набору) |
| `test_none_failed_runs_all` | все зелене, lfnf за замовчуванням → усі тести |
| `test_none_failed_lfnf_none` | все зелене, `lfnf="none"` → `[]` |
| `test_empty_cache_runs_all` | порожній кеш → усі тести |

---

## 🏋️ Вправа 2: Кеш між прогонами (EASY)

**Файл:** `exercise_2_cache.py`

Функції `write_cache()` і `read_last_failed()` вже надані. Замініть `pass` на `assert`.

| Тест | Що перевірити |
|------|--------------|
| `test_write_then_read` | після запису кеш віддає `["test_b"]` |
| `test_fresh_cache_empty` | свіжий кеш → `[]` |
| `test_cache_overwritten` | другий прогін перезаписує кеш → `["test_b"]` |
| `test_all_green_clears_failed` | усе зелене → у кеші немає впалих |
| `test_clearing_cache_loses_history` | `cache.clear()` → `[]` |

---

## 🏋️ Вправа 3: Знайди і виправ (MEDIUM)

**Файл:** `exercise_3_fix_lf.py`

Один тест навмисно падає — очікуваний результат `--lf` неправильний.

**Завдання:**
1. Запустіть файл — один тест червоний
2. Прочитайте вивід pytest: який результат `--lf` очікується насправді?
3. Заповніть блок `# ВІДПОВІДЬ:`
4. Виправте очікуване значення в `test_lf_picks_failed`, щоб тест проходив

| Тест | Стан |
|------|------|
| `test_lf_picks_failed` | ❌ падає — виправте очікуване значення |
| `test_lf_no_failures_runs_all` | ✅ правильний |
| `test_lf_lfnf_none_runs_nothing` | ✅ правильний |

---

## ✅ Перевірка

```bash
pytest test_exercises.py -v
```

### Критерії:

- [ ] Всі тести проходять
- [ ] У вправах 1 і 2 усі `pass` замінено на `assert`
- [ ] У вправі 3 виправлено очікуване значення `--lf` і заповнено блок `# ВІДПОВІДЬ:`
- [ ] Розумієте: `--lf` бере впалих з кешу, кеш перезаписується щопрогону
