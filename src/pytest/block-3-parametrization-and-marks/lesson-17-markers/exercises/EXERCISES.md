# Вправи — Lesson 17: Markers

---

## 🏋️ Вправа 1: Готові маркери (EASY)

**Файл:** `exercise_1_apply_markers.py`

Маркери вже проставлено. Замініть `pass` на правильний `assert`.

| Тест | Маркер | Що перевірити |
|------|--------|--------------|
| `test_status_code_ok` | `smoke` | `status_code == 200` |
| `test_user_is_authenticated` | `smoke` | `authenticated` є truthy |
| `test_cart_total` | `regression` | `total == 100` |
| `test_username_in_response` | `regression` | `"alice"` є в `users` |
| `test_large_dataset_length` | `slow` | `len(data) == 1000` |

---

## 🏋️ Вправа 2: Власні маркери (MEDIUM)

**Файл:** `exercise_2_custom.py`

Власні маркери (`api`, `ui`, `critical`) зареєстровані у `conftest.py`.
Замініть `pass` на правильний `assert`.

| Тест | Маркер(и) | Що перевірити |
|------|-----------|--------------|
| `test_response_status` | `api` | `response["status"] == 201` |
| `test_response_has_id` | `api` | `"id"` є серед ключів `response` |
| `test_button_visible` | `ui` | `"submit"` є в `elements` |
| `test_payment_completed` | `critical` | `payment["status"] == "completed"` |
| `test_health_endpoint` | `smoke` + `api` | `service_up` є truthy |

---

## 🏋️ Вправа 3: Виправте баг (MEDIUM)

**Файл:** `exercise_3_fix_marker.py`

Маркери правильні та зареєстровані — файл збирається. Проблема у **логіці**
одного тесту: його `assert` падає.

| Тест | Маркер | Стан |
|------|--------|------|
| `test_status_ok` | `smoke` | проходить |
| `test_user_count` | `api` | **падає** — виправте значення |
| `test_order_total` | `critical` | проходить |

**Завдання:**
1. Запустіть файл — рівно один тест падає
2. Прочитайте вивід pytest: що саме не збіглося?
3. Виправте значення так, щоб `assert` проходив
4. Заповніть блок `# ВІДПОВІДЬ:` у файлі

---

## ✅ Перевірка

```bash
pytest test_exercises.py -v
```

### Критерії:

- [ ] Усі тести проходять
- [ ] У вправах 1–2 `pass` замінено на `assert`
- [ ] Маркери НЕ змінювали (вони вже правильні та зареєстровані)
- [ ] У вправі 3 виправлено логіку падаючого тесту
- [ ] Блок `# ВІДПОВІДЬ:` у вправі 3 заповнено
