# Block 2: Pytest Fixtures

Фікстури — серце pytest. Вони готують дані та ресурси для тестів, прибирають після них і усувають дублювання setup-коду. Цей блок веде від першої фікстури до конфігурації спільних фікстур у `conftest.py` та найкращих практик.

## 📚 Уроки (6 занять)

### Lesson 9: What is a Fixture
📁 Папка: `lesson-9-fixture-basics`
- `@pytest.fixture` — що це і навіщо
- Фікстура повертає значення для тесту

### Lesson 10: Using Fixtures in Tests
📁 Папка: `lesson-10-using-fixtures`
- Фікстура як параметр тесту
- Кілька фікстур, фікстура всередині фікстури

### Lesson 11: Setup/Teardown with yield
📁 Папка: `lesson-11-yield-fixtures`
- `yield` — код до і після тесту
- Гарантоване прибирання ресурсів

### Lesson 12: Fixture Scopes
📁 Папка: `lesson-12-fixture-scopes`
- function / class / module / session
- Коли фікстура створюється й знищується

### Lesson 13: Shared Fixtures in conftest.py
📁 Папка: `lesson-13-conftest-fixtures`
- Спільні фікстури без імпорту
- Роль `conftest.py`

### Lesson 14: Fixture Best Practices
📁 Папка: `lesson-14-fixture-best-practices`
- Ізоляція, мінімальний scope
- Одна відповідальність, обережність з autouse

## 🚀 Як почати

1. Почніть з `lesson-9-fixture-basics`
2. Прочитайте README в папці уроку
3. Вивчіть файли в `examples/`
4. Виконайте вправи в `exercises/` (див. `EXERCISES.md`)
5. Відповідайте на питання в `QUESTIONS.md`
6. Запустіть перевірку: `pytest exercises/test_exercises.py -v`

---

**Далі:** `lesson-9-fixture-basics`
