# Вправи — Lesson 14: Fixture Best Practices

---

## 🏋️ Вправа 1: Ізоляція фікстур (EASY)

**Файл:** `exercise_1_isolation.py`

Фікстура `fresh_inbox` вже написана правильно (function-scope). Замініть `pass` на `assert`.

| Тест | Що перевірити |
|------|--------------|
| `test_inbox_starts_empty` | локальний список порожній (`inbox == []`) |
| `test_add_one_message` | після одного `append` довжина == 1 |
| `test_inbox_is_isolated` | скринька знову порожня — попередній тест не вплинув |
| `test_two_messages` | після двох `append` вміст == `["a", "b"]` |
| `test_still_isolated` | `"a"` немає у свіжій скриньці |

---

## 🏋️ Вправа 2: Рефакторинг у малі фікстури (MEDIUM)

**Файл:** `exercise_2_refactor.py`

Було: одна фікстура-«комбайн» `everything()` (див. docstring файлу). Стало: три маленькі композовані фікстури. Допишіть тіла фікстур і `assert` у тестах.

| Що написати | Завдання |
|------|---------|
| фікстура `user` | `return {"name": "Alice"}` |
| фікстура `client(user)` | `return {"user": user, "base_url": "https://example.test"}` |
| фікстура `authed_session(client)` | `return {"client": client, "token": "session-abc"}` |
| `test_user_name` | `user["name"] == "Alice"` |
| `test_client_has_user` | `client["user"]["name"] == "Alice"` |
| `test_client_base_url` | `client["base_url"]` правильний |
| `test_session_composition` | `authed_session` бачить `user` крізь усі шари |
| `test_session_token` | токен == `"session-abc"` |

---

## 🏋️ Вправа 3: Виправ анти-патерн (MEDIUM)

**Файл:** `exercise_3_fix_practice.py`

Фікстура `shared_cart` має `scope="module"` і є мутабельним списком — тести псують стан один одному.

**Завдання:**
1. Запустіть файл — рівно один тест падає (`test_cart_is_isolated`)
2. Прочитайте вивід pytest: чому довжина == 2, а не 1?
3. Виправте фікстуру за блоком `# ВІДПОВІДЬ` (приберіть `scope="module"`)
4. Переконайтесь, що обидва тести проходять

---

## ✅ Перевірка

```bash
pytest test_exercises.py -v
```

### Критерії:

- [ ] У вправі 1 всі `pass` замінені на `assert`
- [ ] У вправі 2 фікстури маленькі та композовані (`user → client → authed_session`), без «комбайна»
- [ ] Імена фікстур зрозумілі (не `data`/`obj`)
- [ ] У вправі 3 прибрано `scope="module"` — тести знову ізольовані
- [ ] Усі тести зелені
