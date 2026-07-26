# Вправи — Lesson 19: Filter by Name

Усі вправи працюють із функцією `select_by_name(names, expression)`, яка **симулює**
`pytest -k`: приймає список імен тестів і вираз, повертає імена, що пройшли фільтр.

---

## 🏋️ Вправа 1: Відбір за підрядком (EASY)

**Файл:** `exercise_1_filter.py`

Замініть `pass` на `assert` із правильним очікуваним відбором.

| Тест | Вираз `-k` | Очікуваний відбір |
|------|-----------|-------------------|
| `test_filter_login` | `login` | `["test_login_valid"]` |
| `test_filter_matches_two` | `login` | `["test_login_valid", "test_login_invalid"]` |
| `test_filter_case_insensitive` | `LOGIN` | `["test_login_valid"]` |
| `test_filter_no_match` | `signup` | `[]` |
| `test_filter_signup` | `signup` | `["test_signup_new"]` |

---

## 🏋️ Вправа 2: Вирази and / or / not (MEDIUM)

**Файл:** `exercise_2_expressions.py`

| Тест | Вираз `-k` | Очікуваний відбір |
|------|-----------|-------------------|
| `test_login_and_not_admin` | `login and not admin` | `["test_login_valid"]` |
| `test_login_or_logout` | `login or logout` | `["test_login_valid", "test_logout_ok"]` |
| `test_not_slow` | `not slow` | `["test_fast_ping", "test_quick_check"]` |
| `test_and_requires_both` | `login and invalid` | `["test_login_invalid"]` |
| `test_or_at_least_one` | `admin or root` | `["test_admin_panel", "test_root_access"]` |

---

## 🏋️ Вправа 3: Виправ відбір (MEDIUM)

**Файл:** `exercise_3_fix_filter.py`

Ця вправа — про різницю `-k` (імена) vs `-m` (маркери).

**Завдання:**
1. Запустіть файл — рівно один тест падає
2. Прочитайте вивід pytest: що насправді повертає `select_by_name`?
3. Заповніть блок `# ВІДПОВІДЬ:`
4. Виправте помилкове очікування — `-k` матчить **імена**, а не маркери

| Тест | Стан | Підказка |
|------|------|----------|
| `test_login_substring_ok` | ✅ проходить | еталон правильного відбору |
| `test_k_does_not_match_markers` | ❌ падає | `-k slow` не знайде `test_big_upload` — у імені немає `slow` |
| `test_not_admin_ok` | ✅ проходить | `not admin` прибирає admin-тест |

---

## ✅ Перевірка

```bash
pytest test_exercises.py -v
```

### Критерії:

- [ ] Усі тести у вправах 1–2 проходять (усі `pass` замінено на `assert`)
- [ ] Розумієте, що `-k` матчить **імена**, а не маркери (`-m`)
- [ ] Правильно читаєте вирази `and` / `or` / `not`
- [ ] Вправу 3 виправлено, блок `# ВІДПОВІДЬ:` заповнено
