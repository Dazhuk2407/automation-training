# Вправи — Lesson 17: Test Data Structures

---

## 🏋️ Вправа 1: Навігація (EASY)

**Файл:** `exercise_1_navigation.py`

| Тест | Що зробити |
|------|-----------|
| `test_status` | Перевірити status == 200 |
| `test_users_count` | Порахувати кількість users |
| `test_first_user_name` | Дістати name першого user |
| `test_safe_access` | Безпечний доступ через .get() |

---

## 🏋️ Вправа 2: Валідація (MEDIUM)

**Файл:** `exercise_2_validation.py`

| Тест | Що зробити |
|------|-----------|
| `test_required_fields` | Кожен user має id, name, email |
| `test_all_emails_valid` | Кожен email містить "@" |
| `test_unique_ids` | ID унікальні (через set) |
| `test_roles_not_empty` | Кожен user має хоча б одну роль |

---

## 🏋️ Вправа 3: Фабрика (MEDIUM)

**Файл:** `exercise_3_factory.py`

| Тест | Що зробити |
|------|-----------|
| `test_default_user` | Фабрика повертає user з правильними defaults |
| `test_override_name` | make_user(name="Bob") |
| `test_base_not_modified` | Оригінал не змінився |

---

## 🏋️ Вправа 4: Реальний API (HARD)

**Файл:** `exercise_4_real_api.py`

| Тест | Що зробити |
|------|-----------|
| `test_completed_count` | Порахувати completed замовлення |
| `test_total_sum` | Сума всіх total |
| `test_user_orders` | Замовлення конкретного user_id |
| `test_no_empty_items` | Кожне замовлення має items |

---

## ✅ Перевірка

```bash
pytest test_exercises.py -v
```