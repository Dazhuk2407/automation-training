# Вправи — Lesson 7: Запуск тестів з CLI

Ці вправи — практичні. Ви виконуєте команди в терміналі та аналізуєте вивід.

---

## 🏋️ Вправа 1: Базовий запуск (EASY)

**Файл:** `test_for_cli.py` (вже створений)

Запустіть тести різними способами і порівняйте вивід:

```bash
# 1. Базовий запуск
pytest test_for_cli.py

# 2. Детальний вивід
pytest test_for_cli.py -v

# 3. Мінімальний вивід
pytest test_for_cli.py -q

# 4. З показом print()
pytest test_for_cli.py -s
```

**Запитання до себе:**
- Яка різниця між `-v` та `-q`?
- Чи видно print() без `-s`?

---

## 🏋️ Вправа 2: Запуск конкретного тесту (EASY)

Запустіть тільки один тест з файлу:

```bash
# Один конкретний тест
pytest test_for_cli.py::test_addition -v

# Тест з класу
pytest test_for_cli.py::TestStrings::test_upper -v
```

**Запитання до себе:**
- Який формат шляху до тесту в класі?

---

## 🏋️ Вправа 3: Фільтрація через -k (MEDIUM)

```bash
# Тести, що містять "add" у назві
pytest test_for_cli.py -k "add" -v

# Тести, що НЕ містять "slow"
pytest test_for_cli.py -k "not slow" -v

# Тести з "string" АБО "list"
pytest test_for_cli.py -k "string or list" -v
```

**Запитання до себе:**
- Скільки тестів знайшов `-k "add"`?
- Чи знаходить `-k` тести всередині класів?

---

## 🏋️ Вправа 4: Контроль помилок (MEDIUM)

```bash
# Зупинитися на першому падінні
pytest test_for_cli.py -x -v

# Зупинитися після 2 падінь
pytest test_for_cli.py --maxfail=2 -v
```

Щоб побачити ефект, тимчасово розкоментуйте падаючий тест у `test_for_cli.py`.

---

## 🏋️ Вправа 5: Traceback та collect-only (MEDIUM)

```bash
# Короткий traceback
pytest test_for_cli.py --tb=short

# Без traceback
pytest test_for_cli.py --tb=no

# Перевірити що pytest знайшов (без запуску)
pytest test_for_cli.py --collect-only
```

**Запитання до себе:**
- Скільки тестів показав `--collect-only`?
- Яка різниця між `--tb=short` та `--tb=no`?

---

## 🏋️ Вправа 6: Комбінування опцій (MEDIUM)

Спробуйте комбінації:

```bash
# Verbose + зупинка на першому + короткий traceback
pytest test_for_cli.py -v -x --tb=short

# Фільтр + verbose + print
pytest test_for_cli.py -k "string" -v -s

# Quiet + collect-only
pytest test_for_cli.py -q --collect-only
```

---

## ✅ Перевірка

Ці вправи — ручні (CLI-практика). Критерії:

- [ ] Ви запустили тести мінімум 10 різними способами
- [ ] Розумієте різницю між `-v`, `-q`, `-s`
- [ ] Вмієте запустити один конкретний тест
- [ ] Вмієте фільтрувати через `-k`
- [ ] Вмієте зупиняти на помилках через `-x`
- [ ] Знаєте що робить `--collect-only`