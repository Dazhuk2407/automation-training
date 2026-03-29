# Вправи — Lesson 8: Розуміння виводу pytest

Ці вправи — аналітичні. Ви запускаєте тести, читаєте вивід і даєте конкретні відповіді.

**Файл для всіх вправ:** `test_output_practice.py`

---

## 🏋️ Вправа 1: Визначити статуси (EASY)

Запустіть:
```bash
pytest test_output_practice.py -v
```

**Дайте відповіді:**
1. Скільки тестів зі статусом PASSED?
2. Скільки зі статусом FAILED?
3. Скільки зі статусом ERROR?
4. Скільки SKIPPED?
5. Скільки XFAIL?

---

## 🏋️ Вправа 2: Прочитати traceback (EASY)

Подивіться на вивід тесту `test_failed_comparison`.

**Дайте відповіді:**
1. Яка назва тесту що впав?
2. Який статус — FAILED чи ERROR?
3. Який рядок позначений `>`?
4. Що показує рядок з `E`?
5. В якому файлі і на якому рядку помилка?

---

## 🏋️ Вправа 3: FAILED vs ERROR (MEDIUM)

Порівняйте вивід `test_failed_comparison` та `test_error_zero_division`.

**Дайте відповіді:**
1. Чим відрізняється FAILED від ERROR?
2. У `test_failed_comparison` — чи дійшов код до assert?
3. У `test_error_zero_division` — чи дійшов код до assert?
4. Яка помилка в кожному випадку? (AssertionError vs ZeroDivisionError)

---

## 🏋️ Вправа 4: Рівні traceback (MEDIUM)

Запустіть той самий файл з різними `--tb`:

```bash
pytest test_output_practice.py --tb=short
pytest test_output_practice.py --tb=no
pytest test_output_practice.py --tb=long -l
```

**Дайте відповіді:**
1. Що показує `--tb=short` порівняно з дефолтом?
2. Що залишається з `--tb=no`?
3. Що додає `-l` (show locals)?
4. Коли який варіант зручніший?

---

## 🏋️ Вправа 5: Multiple asserts (MEDIUM)

Подивіться на вивід тесту `test_multiple_asserts`.

**Дайте відповіді:**
1. Який assert впав (який за рахунком)?
2. Скільки assert виконалось до падіння?
3. Чи виконався четвертий assert?
4. Чому це проблема для діагностики?
5. Як покращити цей тест? (підказка: розбити)

---

## 🏋️ Вправа 6: Dict diff (MEDIUM)

Подивіться на вивід тесту `test_failed_dict` з опцією `-vv`:

```bash
pytest test_output_practice.py::test_failed_dict -vv
```

**Дайте відповіді:**
1. Що показує pytest у diff?
2. Яке поле відрізняється?
3. Яке значення очікувалось і яке отримали?

---

## 🏋️ Вправа 7: Print та -s (EASY)

Запустіть:
```bash
pytest test_output_practice.py::test_with_print -v
pytest test_output_practice.py::test_with_print -v -s
```

**Дайте відповіді:**
1. Чи видно print() без `-s`?
2. Де саме з'являється вивід print() з `-s`?

---

## ✅ Перевірка

Ці вправи — ручні (аналіз виводу). Критерії:

- [ ] Ви вмієте визначити статус тесту (PASSED/FAILED/ERROR)
- [ ] Ви вмієте знайти рядок падіння (`>`) та причину (`E`)
- [ ] Ви розумієте різницю між FAILED та ERROR
- [ ] Ви знаєте коли використовувати `--tb=short`, `-l`, `-s`
- [ ] Ви розумієте чому multiple asserts — погана практика