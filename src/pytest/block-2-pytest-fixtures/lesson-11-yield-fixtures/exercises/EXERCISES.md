# Вправи — Lesson 11: yield Fixtures

---

## 🏋️ Вправа 1: Базова yield-фікстура (EASY)

**Файл:** `exercise_1_yield.py`

Напишіть yield-фікстуру `temp_data`: setup створює `{"opened": True}`, `yield` віддає його, teardown ставить `opened = False`.

| Тест | Що перевірити |
|------|--------------|
| `test_data_is_dict` | `temp_data` — це `dict` |
| `test_opened_is_true` | `temp_data["opened"]` є `True` |
| `test_can_add_key` | після `temp_data["value"] = 10` значення дорівнює 10 |
| `test_fresh_each_time` | у свіжій фікстурі ключа `value` ще немає |

---

## 🏋️ Вправа 2: setup/teardown для ресурсу (MEDIUM)

**Файл:** `exercise_2_cleanup.py`

Напишіть yield-фікстуру `connection`, яка імітує з'єднання: setup відкриває `{"status": "open", "queries": []}`, teardown ставить `status = "closed"`.

| Тест | Що перевірити |
|------|--------------|
| `test_connection_open` | `connection["status"] == "open"` |
| `test_no_queries_initially` | `connection["queries"]` порожній |
| `test_add_query` | після додавання одного запиту довжина == 1 |
| `test_queries_reset` | кожен тест отримує свіже з'єднання (запити скинуті) |

---

## 🏋️ Вправа 3: Виправте teardown (MEDIUM)

**Файл:** `exercise_3_fix_teardown.py`

Фікстура використовує `return` замість `yield`, тому teardown не виконується — один тест падає.

**Завдання:**
1. Запустіть файл — знайдіть тест, що падає (`test_teardown_ran`)
2. Зрозумійте чому teardown не спрацював
3. Виправте фікстуру (`return` → `yield`)
4. Заповніть блок `# ВІДПОВІДЬ:` у файлі

| Тест | Стан ДО виправлення |
|------|--------------------|
| `test_session_open` | проходить |
| `test_session_is_dict` | проходить |
| `test_teardown_ran` | ❌ падає (teardown не виконався) |

---

## ✅ Перевірка

```bash
pytest test_exercises.py -v
```

### Критерії:

- [ ] Всі тести проходять
- [ ] Фікстури використовують `yield`, а не `return`
- [ ] setup — до `yield`, teardown — після `yield`
- [ ] Вправа 3 виправлена, блок `# ВІДПОВІДЬ:` заповнено
