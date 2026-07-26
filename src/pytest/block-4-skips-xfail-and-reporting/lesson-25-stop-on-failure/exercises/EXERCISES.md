# Вправи — Lesson 25: Stop on First Failure

Усі вправи працюють з чистою функцією-симуляцією `run_until_maxfail(results, maxfail)`:
вона повертає, скільки тестів **реально виконалось** до зупинки після `maxfail` помилок.
`results` — список `"passed"` / `"failed"` у порядку виконання.

---

## 🏋️ Вправа 1: Логіка `-x` (EASY)

**Файл:** `exercise_1_stop.py`

`-x` == `--maxfail=1` — зупинка на ПЕРШОМУ падінні.

| Тест | `results` | `maxfail` | Очікувано виконано |
|------|-----------|-----------|--------------------|
| `test_stop_on_first` | `["passed","failed","passed","failed"]` | 1 | 2 |
| `test_first_fails` | `["failed","passed","passed"]` | 1 | 1 |
| `test_all_pass` | `["passed","passed","passed"]` | 1 | 3 |
| `test_last_fails` | `["passed","passed","failed"]` | 1 | 3 |

---

## 🏋️ Вправа 2: Логіка `--maxfail=N` (MEDIUM)

**Файл:** `exercise_2_maxfail.py`

Зупинка після N падінь; тести, що проходять, лічильник помилок не збільшують.

| Тест | `results` | `maxfail` | Очікувано виконано |
|------|-----------|-----------|--------------------|
| `test_maxfail_two` | `["failed","passed","failed","passed"]` | 2 | 3 |
| `test_maxfail_three` | `["failed","failed","passed","failed","passed"]` | 3 | 4 |
| `test_passes_dont_count` | `["passed","passed","failed","passed","passed"]` | 2 | 5 |
| `test_not_enough_fails` | `["failed","passed","passed"]` | 3 | 3 |

---

## 🏋️ Вправа 3: Знайди і виправ (MEDIUM)

**Файл:** `exercise_3_fix_stop.py`

Один assert про кількість виконаних тестів **неправильний** — через це один тест падає.

**Завдання:**
1. Запустіть файл — один тест навмисно падає
2. Прочитайте вивід pytest: яке число очікувалось, а яке отримано?
3. Виправте неправильне очікуване значення
4. Заповніть блок `# ВІДПОВІДЬ:`

---

## ✅ Перевірка

```bash
pytest test_exercises.py -v
```

### Критерії:

- [ ] Всі тести у вправах 1-2 проходять
- [ ] У вправах 1-2 не залишилось `pass` замість `assert`
- [ ] Вправа 3 виправлена — усі тести зелені
- [ ] Заповнено блок `# ВІДПОВІДЬ:` у вправі 3
