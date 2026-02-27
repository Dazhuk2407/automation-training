# Questions - Lesson 4: Test Discovery

## 🎯 Test Discovery Rules

1. **Які файли pytest шукає автоматично?**
   - A: `test_*.py` та `*_test.py`

2. **Як мають називатися тестові функції?**
   - A: Починатися з `test_`

3. **Як мають називатися тестові класи?**
   - A: Починатися з `Test` (без `__init__`)

4. **Чи знайде pytest файл `calculator.py`?**
   - A: Ні, потрібно `test_calculator.py`

5. **Чи знайде pytest функцію `check_result()`?**
   - A: Ні, потрібно `test_check_result()`

## 📂 File Organization

6. **Чи шукає pytest в subdirectories?**
   - A: Так, рекурсивно

7. **Що таке `conftest.py`?**
   - A: Спеціальний файл з fixtures та конфігурацією

8. **Чи потрібен `__init__.py` в tests/?**
   - A: Ні, але може бути корисним

## 🏗️ Test Classes

9. **Навіщо групувати тести в класи?**
   - A: Організація, спільні fixtures, логічне групування

10. **Чи можуть бути тести і в функціях і в класах в одному файлі?**
    - A: Так, це нормально

11. **Яка команда показує які тести знайдено без запуску?**
    - A: `pytest --collect-only`

12. **Де налаштовується пошук тестів?**
    - A: У `pytest.ini` або `pyproject.toml`

---

**✅ Ready for Lesson 5?**

