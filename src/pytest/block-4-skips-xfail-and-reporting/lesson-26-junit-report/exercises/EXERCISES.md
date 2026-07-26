# Вправи — Lesson 26: JUnit Report

---

## 🏋️ Вправа 1: Підрахунок summary (EASY)

**Файл:** `exercise_1_parse.py`

Функції `parse_summary` та `passed_count` уже реалізовані, а `SAMPLE` (JUnit XML)
надано у файлі. Замініть `pass` на правильні `assert`.

| Тест | Що перевірити |
|------|--------------|
| `test_tests_count` | `tests` дорівнює 4 |
| `test_failures_count` | `failures` дорівнює 1 |
| `test_skipped_count` | `skipped` дорівнює 1 |
| `test_passed_count` | `passed_count(...)` дорівнює 2 |
| `test_root_tag` | кореневий тег — `testsuite` |

---

## 🏋️ Вправа 2: Summary-рядок (MEDIUM)

**Файл:** `exercise_2_summary.py`

Функція `summary_line` уже реалізована, `SAMPLE` надано. Замініть `pass` на `assert`.

| Тест | Що перевірити |
|------|--------------|
| `test_full_line` | рядок дорівнює `Tests: 4, Passed: 2, Failed: 1, Skipped: 1` |
| `test_starts_with_total` | рядок починається з `Tests: 4` |
| `test_contains_passed` | у рядку є `Passed: 2` |
| `test_contains_failed` | у рядку є `Failed: 1` |

---

## 🏋️ Вправа 3: Знайти помилку в підрахунку (MEDIUM)

**Файл:** `exercise_3_fix_report.py`

У файлі є баг: `passed_count` віднімає не той атрибут, тому один тест падає.

**Завдання:**
1. Запустіть файл — один тест навмисно падає
2. Прочитайте вивід pytest: яке значення отримали замість очікуваного?
3. Виправте функцію `passed_count`
4. Заповніть блок `# ВІДПОВІДЬ:`

---

## ✅ Перевірка

```bash
pytest test_exercises.py -v
```

### Критерії:

- [ ] Всі тести у вправах 1-2 проходять
- [ ] Використано `xml.etree.ElementTree`, не регекспи
- [ ] `passed` рахується формулою `tests - failures - skipped`
- [ ] У вправі 3 виправлено `passed_count` і заповнено блок `# ВІДПОВІДЬ:`
