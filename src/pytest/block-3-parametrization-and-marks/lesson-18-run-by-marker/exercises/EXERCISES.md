# Вправи — Lesson 18: Run by Marker

Функція `select_by_marker(tests, expression)` уже реалізована у
`marker_selection.py` і моделює поведінку `pytest -m "<expression>"`.
Модель тесту: `{"name": "test_x", "markers": {"smoke"}}`.

---

## 🏋️ Вправа 1: Відбір за одиночним маркером (EASY)

**Файл:** `exercise_1_select.py`

Замініть `pass` на `assert` для очікуваного відбору.

| Тест | Вираз | Очікуваний відбір |
|------|-------|-------------------|
| `test_select_smoke` | `smoke` | `["test_login", "test_signup"]` |
| `test_select_regression` | `regression` | `["test_edge_case", "test_report"]` |
| `test_select_slow` | `slow` | `["test_report"]` |
| `test_select_unknown_marker_empty` | `unit` | `[]` |
| `test_untagged_not_selected` | `smoke` | `test_health` НЕ у відборі |

---

## 🏋️ Вправа 2: Логічні вирази (MEDIUM)

**Файл:** `exercise_2_expressions.py`

Замініть `pass` на `assert` для складених виразів.

| Тест | Вираз | Очікуваний відбір |
|------|-------|-------------------|
| `test_smoke_and_not_slow` | `smoke and not slow` | `["test_login"]` |
| `test_smoke_or_regression` | `smoke or regression` | `["test_login", "test_quick_check", "test_edge_case", "test_report"]` |
| `test_regression_and_not_slow` | `regression and not slow` | `["test_edge_case"]` |
| `test_not_slow` | `not slow` | `["test_login", "test_edge_case", "test_health"]` |
| `test_smoke_and_slow` | `smoke and slow` | `["test_quick_check"]` |

---

## 🏋️ Вправа 3: Знайди і виправ (MEDIUM)

**Файл:** `exercise_3_fix_selection.py`

Один тест має неправильне очікування відбору і падає.

| Крок | Дія |
|------|-----|
| 1 | Запустіть файл — рівно один тест падає |
| 2 | Прочитайте вивід: що реально відбирає `smoke and not slow`? |
| 3 | Виправте очікуваний список у падаючому тесті |
| 4 | Заповніть блок `# ВІДПОВІДЬ:` |

Підказка: `test_quick_check` має маркери `{"smoke", "slow"}`, тож `not slow`
його відкидає.

---

## ✅ Перевірка

```bash
pytest test_exercises.py -v
```

### Критерії:

- [ ] У вправах 1–2 усі `pass` замінено на `assert`
- [ ] Вправи 1–2 повністю зелені
- [ ] У вправі 3 виправлено очікуваний список — усі тести проходять
- [ ] Блок `# ВІДПОВІДЬ:` у вправі 3 заповнено
