# Вправи — Lesson 13: conftest.py

Усі фікстури живуть у `conftest.py` цієї теки. Використовуйте їх
**БЕЗ** `import` — просто додайте ім'я фікстури як аргумент тесту.

Доступні фікстури (`exercises/conftest.py`):

| Фікстура | Значення |
|----------|----------|
| `sample_user` | `{"name": "Alice", "role": "admin", "age": 30}` |
| `app_config` | `{"base_url": "https://api.example.com", "timeout": 5, "retries": 3}` |
| `test_data` | `{"product": {"id": 42, "name": "Keyboard", "price": 9.99}, "cart": ["Keyboard", "Mouse"]}` |

---

## 🏋️ Вправа 1: Використання фікстур з conftest (EASY)

**Файл:** `exercise_1_use_conftest.py`

| Тест | Що перевірити |
|------|--------------|
| `test_user_name` | `sample_user["name"]` == "Alice" |
| `test_user_role` | `sample_user["role"]` == "admin" |
| `test_config_base_url` | `app_config["base_url"]` == "https://api.example.com" |
| `test_config_timeout` | `app_config["timeout"]` == 5 |
| `test_product_price` | `test_data["product"]["price"]` == 9.99 |

---

## 🏋️ Вправа 2: Кілька conftest-фікстур разом (MEDIUM)

**Файл:** `exercise_2_combine.py`

| Тест | Що перевірити |
|------|--------------|
| `test_user_age` | `sample_user["age"]` == 30 |
| `test_config_retries` | `app_config["retries"]` == 3 |
| `test_cart_contains_mouse` | "Mouse" є в `test_data["cart"]` |
| `test_user_and_config_together` | дві фікстури: `role` == "admin" та `timeout` == 5 |
| `test_all_three_fixtures` | три фікстури разом: name, base_url, product id |

---

## 🏋️ Вправа 3: Виправ conftest-фікстуру (MEDIUM)

**Файл:** `exercise_3_fix_conftest.py`

Один тест навмисно падає.

**Завдання:**
1. Запустіть файл — `test_user_role_is_admin` падає
2. Прочитайте вивід pytest: яке насправді значення `role` у фікстурі?
3. Виправте очікуване значення у тесті
4. Заповніть блок `# ВІДПОВІДЬ:` (зокрема — чи треба import фікстури з conftest)

---

## ✅ Перевірка

```bash
pytest test_exercises.py -v
```

### Критерії:

- [ ] Всі тести проходять
- [ ] Фікстури використано **без** `import` з conftest
- [ ] У вправах 1-2 замінено всі `pass` на `assert`
- [ ] У вправі 3 виправлено падаючий тест і заповнено блок ВІДПОВІДЬ
