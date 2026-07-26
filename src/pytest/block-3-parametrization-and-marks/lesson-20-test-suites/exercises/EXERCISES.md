# Вправи — Lesson 20: Test Suites

---

## 🏋️ Вправа 1: Класифікація тестів у набори (EASY)

**Файл:** `exercise_1_suite.py`

Функція `suite_of(markers)` вже написана. Замініть `pass` на правильний `assert`.

| Тест | Що перевірити |
|------|--------------|
| `test_smoke_marker` | `suite_of({"smoke"})` дорівнює `"smoke"` |
| `test_regression_marker` | `suite_of({"regression"})` дорівнює `"regression"` |
| `test_both_markers_prefer_smoke` | `suite_of({"smoke", "regression"})` дорівнює `"smoke"` |
| `test_no_suite_marker` | `suite_of({"slow"})` дорівнює `"uncategorized"` |
| `test_empty_markers` | `suite_of(set())` дорівнює `"uncategorized"` |

---

## 🏋️ Вправа 2: Підрахунок тестів у наборах (MEDIUM)

**Файл:** `exercise_2_organize.py`

Функція `count_suites(tests)` приймає список множин маркерів і повертає словник
`{"smoke": n, "regression": n, "uncategorized": n}`. Замініть `pass` на `assert`.

| Тест | Що перевірити |
|------|--------------|
| `test_count_empty` | порожній список -> усі лічильники по 0 |
| `test_count_only_smoke` | два smoke-тести -> `smoke == 2` |
| `test_count_mixed` | змішаний набір -> повний словник `{1, 1, 1}` |
| `test_count_smoke_subset_of_regression` | тест з обома маркерами -> `regression == 0` |
| `test_count_uncategorized` | два тести без smoke/regression -> `uncategorized == 2` |

---

## 🏋️ Вправа 3: Виправте класифікацію (MEDIUM)

**Файл:** `exercise_3_fix_suite.py`

Один тест навмисно падає — у ньому неправильне очікування набору.

**Завдання:**
1. Запустіть файл — рівно один тест падає
2. Прочитайте вивід pytest: що `suite_of` повертає насправді?
3. Згадайте правило **smoke ⊂ regression** (пріоритет має `smoke`)
4. Виправте очікуване значення в `assert`
5. Заповніть блок `# ВІДПОВІДЬ:`

| Тест | Стан |
|------|------|
| `test_smoke` | ✅ проходить |
| `test_both_markers` | ❌ падає — виправити очікування |
| `test_uncategorized` | ✅ проходить |

---

## ✅ Перевірка

```bash
pytest test_exercises.py -v
```

### Критерії:

- [ ] Всі тести у вправах 1-2 проходять
- [ ] У вправах 1-2 не залишилось `pass` замість `assert`
- [ ] Вправа 3 виправлена — усі три тести проходять
- [ ] Блок `# ВІДПОВІДЬ:` у вправі 3 заповнено
