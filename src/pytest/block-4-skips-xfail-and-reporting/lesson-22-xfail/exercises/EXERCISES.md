# Вправи — Lesson 22: xfail

---

## 🏋️ Вправа 1: Базовий xfail (EASY)

**Файл:** `exercise_1_xfail.py`

Додайте декоратор `@pytest.mark.xfail(reason="...")` та замініть `pass` на assert.

| Тест | Декоратор | assert |
|------|-----------|--------|
| `test_known_bug_division` | `xfail(reason="bug #1")` | падаючий → `xfailed` |
| `test_known_bug_concat` | `xfail(reason="bug #2")` | падаючий → `xfailed` |
| `test_maybe_fixed` | `xfail(reason="bug #3")` | що проходить → `xpassed` |
| `test_known_bug_sort` | `xfail(reason="bug #4")` | падаючий → `xfailed` |
| `test_normal` | — (без маркера) | що проходить → `passed` |

**Підсумок:** `0 failed`.

---

## 🏋️ Вправа 2: Умовний xfail (MEDIUM)

**Файл:** `exercise_2_conditions.py`

`assert` вже написані і проходять. Допишіть лише **декоратор умовного xfail**.

| Тест | Декоратор |
|------|-----------|
| `test_windows_only_bug` | `xfail(sys.platform == "win32", reason=...)` |
| `test_python_version_bug` | `xfail(sys.version_info < (3, 8), reason=...)` |
| `test_macos_bug` | `xfail(sys.platform == "darwin", reason=...)` |
| `test_disabled_condition` | `xfail(False, reason=...)` |
| `test_arch_bug` | `xfail(sys.maxsize > 2**32, reason=...)` |

Оскільки asserts проходять, підсумок `0 failed` (тести будуть `passed` або `xpassed` залежно від умови на вашій платформі).

---

## 🏋️ Вправа 3: Виправ падаючий тест (MEDIUM)

**Файл:** `exercise_3_fix_xfail.py`

Зараз рівно **один** тест падає (`test_known_bug_rounding`) — відомий баг без маркера.

**Завдання (один варіант):**
1. Запустіть файл — переконайтесь, що `1 failed`.
2. Варіант A: позначте падаючий тест `@pytest.mark.xfail(reason="...")` → `xfailed`.
3. Варіант B: виправте `assert` під реальну поведінку → `passed`.
4. Заповніть/звірте блок `# ВІДПОВІДЬ:` у файлі.

**Підсумок після виправлення:** `0 failed`.

---

## ✅ Перевірка

```bash
pytest test_exercises.py -v
```

### Критерії:

- [ ] Всі три файли існують
- [ ] У кожному достатньо тестів (5 / 5 / 3)
- [ ] Кожен тест містить `assert`
- [ ] Кожен файл дає `0 failed` (xfailed / xpassed — це не failure)
- [ ] `reason` вказано в кожному xfail-маркері
