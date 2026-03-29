# Вправи — Lesson 14: Mutable vs Immutable

---

## 🏋️ Вправа 1: Визначити поведінку (EASY)

**Файл:** `exercise_1_identify.py`

| Тест | Що перевірити |
|------|--------------|
| `test_list_is_mutable` | append змінює оригінальний список |
| `test_string_is_immutable` | upper() не змінює оригінал |
| `test_reference_vs_copy` | `other = items` — посилання, не копія |
| `test_copy_is_independent` | `.copy()` створює незалежний список |
| `test_tuple_is_immutable` | Спроба змінити tuple → TypeError |

---

## 🏋️ Вправа 2: Виправити side effects (MEDIUM)

**Файл:** `exercise_2_side_effects.py`

| Тест | Що зробити |
|------|-----------|
| `test_no_side_effect_dict` | Використати `{**user}` замість мутації |
| `test_no_side_effect_list` | Використати `[*items]` замість append |
| `test_fix_default_arg` | Виправити mutable default argument |

---

## 🏋️ Вправа 3: Безпечні тести (MEDIUM)

**Файл:** `exercise_3_safe_tests.py`

| Тест | Що зробити |
|------|-----------|
| `test_modify_role` | Змінити role через фабрику |
| `test_original_intact` | Перевірити що фабрика дає свіжі дані |
| `test_config_override` | Створити test config через spread |
| `test_list_extend_safe` | Розширити список без мутації оригіналу |

---

## ✅ Перевірка

```bash
pytest test_exercises.py -v
```