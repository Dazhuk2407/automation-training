# Block 4: Skips, XFail, Execution Control, Basic Reporting

Не кожен тест має виконуватись завжди, і не кожне падіння — несподіванка. Цей блок про керування виконанням: пропуск тестів, очікувані падіння, зручні режими прогону (останні впалі, зупинка на першій помилці) та базовий звіт у форматі JUnit XML для CI.

## 📚 Уроки (6 занять)

### Lesson 21: Skip Tests
📁 Папка: `lesson-21-skip`
- `pytest.skip()`, `@pytest.mark.skip`
- `@pytest.mark.skipif` за умовою

### Lesson 22: Expected Failures (xfail)
📁 Папка: `lesson-22-xfail`
- `@pytest.mark.xfail`, `reason`
- xfail vs xpass, `strict`

### Lesson 23: Run Last Failed Tests
📁 Папка: `lesson-23-last-failed`
- `pytest --lf`
- Пришвидшення дебагу

### Lesson 24: Failed First Mode
📁 Папка: `lesson-24-failed-first`
- `pytest --ff`
- Спочатку впалі, потім решта

### Lesson 25: Stop on First Failure
📁 Папка: `lesson-25-stop-on-failure`
- `pytest -x`, `--maxfail`
- Швидкий зворотний зв'язок

### Lesson 26: Generate Basic Report
📁 Папка: `lesson-26-junit-report`
- `pytest --junitxml=report.xml`
- Звіти для CI

## 🚀 Як почати

1. Почніть з `lesson-21-skip`
2. Прочитайте README в папці уроку
3. Вивчіть файли в `examples/`
4. Виконайте вправи в `exercises/` (див. `EXERCISES.md`)
5. Відповідайте на питання в `QUESTIONS.md`
6. Запустіть перевірку: `pytest exercises/test_exercises.py -v`

---

**Далі:** `lesson-21-skip`
