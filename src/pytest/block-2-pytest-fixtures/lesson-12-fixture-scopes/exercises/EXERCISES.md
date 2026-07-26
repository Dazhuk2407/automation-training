# Вправи — Lesson 12: Fixture Scopes

---

## 🏋️ Вправа 1: function scope (EASY)

**Файл:** `exercise_1_scope.py`

Фікстура `number` має function scope і збільшує лічильник при кожному setup.
Замініть `pass` на assert, спираючись на те, що фікстура створюється заново для кожного тесту.

| Тест | Що перевірити |
|------|--------------|
| `test_first` | `number == 1` (setup вперше) |
| `test_second` | `number == 2` (нова фікстура) |
| `test_third` | `number == 3` (знову нова) |
| `test_isolation` | `number` — int і більший за 0 |
| `test_setup_count` | після 4 тестів `counter["n"] == 4` |

---

## 🏋️ Вправа 2: module scope і спільний стан (MEDIUM)

**Файл:** `exercise_2_shared_state.py`

Фікстура `bucket` має `scope="module"` — один список на весь файл.
Замініть `pass` на assert, які показують, що стан **накопичується** між тестами.

| Тест | Що перевірити |
|------|--------------|
| `test_starts_empty` | `bucket == []` |
| `test_add_one` | після `append("a")` → `len(bucket) == 1` |
| `test_state_persists` | `bucket == ["a"]` (стан зберігся) |
| `test_add_second` | після `append("b")` → `bucket == ["a", "b"]` |
| `test_not_reset` | `len(bucket) == 2` (не скинулось) |

---

## 🏋️ Вправа 3: виправте неправильний scope (MEDIUM)

**Файл:** `exercise_3_fix_scope.py`

Фікстура `cart` має `scope="module"`, через що `test_isolation` падає:
стан із `test_add` протікає у наступний тест.

**Завдання:**
1. Запустіть файл — рівно один тест падає
2. Зрозумійте причину: широкий scope + мутація спільного стану
3. Виправте scope так, щоб кожен тест отримував свіжий кошик
4. Заповніть блок `# ВІДПОВІДЬ:` у файлі

| Тест | Стан |
|------|------|
| `test_add` | проходить |
| `test_isolation` | **падає** до виправлення |
| `test_is_list` | проходить |

---

## ✅ Перевірка

```bash
pytest test_exercises.py -v
```

### Критерії:

- [ ] Всі тести у вправах 1-3 проходять
- [ ] У вправі 1 правильно пораховано лічильник setup
- [ ] У вправі 2 враховано, що module-стан накопичується
- [ ] У вправі 3 scope виправлено на `function` (default), а не залишено `module`
- [ ] Заповнено блок `# ВІДПОВІДЬ:` у вправі 3
