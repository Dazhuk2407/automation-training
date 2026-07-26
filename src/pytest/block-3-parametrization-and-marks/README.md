# Block 3: Parametrization and Marks

Один тест — багато наборів даних. Мітки (marks) — щоб позначати та обирати тести. Цей блок про параметризацію (data-driven тести) і маркери: як групувати тести у смоук/регрес та запускати потрібні підмножини.

## 📚 Уроки (6 занять)

### Lesson 15: Parametrized Tests
📁 Папка: `lesson-15-parametrize`
- `@pytest.mark.parametrize`
- Один тест — багато наборів даних

### Lesson 16: Data-Driven Testing
📁 Папка: `lesson-16-data-driven`
- Концепція data-driven
- Набори даних, `ids`, негативні кейси

### Lesson 17: Markers
📁 Папка: `lesson-17-markers`
- `@pytest.mark.smoke`, custom markers
- Реєстрація маркерів

### Lesson 18: Run Tests by Marker
📁 Папка: `lesson-18-run-by-marker`
- `pytest -m smoke`
- Логічні вирази маркерів

### Lesson 19: Filter Tests by Name
📁 Папка: `lesson-19-filter-by-name`
- `pytest -k login`
- Вирази `-k`

### Lesson 20: Organizing Test Suites
📁 Папка: `lesson-20-test-suites`
- Smoke vs regression
- Організація наборів тестів

## 🚀 Як почати

1. Почніть з `lesson-15-parametrize`
2. Прочитайте README в папці уроку
3. Вивчіть файли в `examples/`
4. Виконайте вправи в `exercises/` (див. `EXERCISES.md`)
5. Відповідайте на питання в `QUESTIONS.md`
6. Запустіть перевірку: `pytest exercises/test_exercises.py -v`

---

**Далі:** `lesson-15-parametrize`
