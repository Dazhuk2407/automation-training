# Вправи — Lesson 21: Skip Tests

> Памʼятайте: пропущений (`SKIPPED`) тест — це **не падіння**.
> Мета кожної вправи — **0 failures** (пропуски дозволені й очікувані).

---

## 🏋️ Вправа 1: Безумовний skip (EASY)

**Файл:** `exercise_1_skip.py`

| Тест | Що зробити |
|------|-----------|
| `test_addition` | дописати `assert 2 + 2 == 4` |
| `test_string_length` | дописати `assert len("pytest") == 6` |
| `test_not_ready_feature` | додати `@pytest.mark.skip(reason="фіча ще не реалізована")` |
| `test_list_reverse` | дописати `assert list(reversed([1, 2, 3])) == [3, 2, 1]` |
| `test_blocked_by_bug` | додати `@pytest.mark.skip(reason="блокує баг #4321")` |

Обовʼязково вказуйте `reason`.

---

## 🏋️ Вправа 2: Умовний skipif (MEDIUM)

**Файл:** `exercise_2_skipif.py`

| Тест | Що зробити |
|------|-----------|
| `test_multiplication` | дописати `assert 3 * 4 == 12` |
| `test_python_version_check` | `@pytest.mark.skipif(sys.version_info < (3, 12), reason=...)` + assert |
| `test_windows_only` | `@pytest.mark.skipif(sys.platform != "win32", reason=...)` + assert |
| `test_string_join` | дописати `assert "-".join(["a", "b", "c"]) == "a-b-c"` |
| `test_env_variable` | `@pytest.mark.skipif(os.getenv("CI") is None, reason=...)` + assert |

Умова — це **вираз**, а не викликаний результат зі побічними ефектами.

---

## 🏋️ Вправа 3: Виправ пропуск (MEDIUM)

**Файл:** `exercise_3_fix_skip.py`

Один тест (`test_search_feature`) навмисно **падає**: фіча ще не готова,
а тест уже очікує результат.

**Завдання:**
1. Запустіть файл — побачите рівно 1 `FAILED`
2. Виправте `test_search_feature` одним зі способів:
   - (а) додайте `@pytest.mark.skip(reason="фіча ще не реалізована")`, АБО
   - (б) виправте `assert` під реальний результат `search()`
3. Заповніть блок `# ВІДПОВІДЬ:` унизу файлу
4. Переконайтесь: після виправлення — **0 failures**

---

## ✅ Перевірка

```bash
pytest test_exercises.py -v
```

### Критерії:

- [ ] Всі файли дають **0 failures** (пропуски дозволені)
- [ ] Кожен skip/skipif має `reason`
- [ ] У вправі 2 умова передана як вираз (`sys...`, `os.getenv(...) is None`)
- [ ] У вправі 3 падаючий тест виправлено (skip або коректний assert)
- [ ] Блок `# ВІДПОВІДЬ:` у вправі 3 заповнено
