# Questions - Lesson 7: Run Tests from CLI

## 🎯 Basic Commands

1. **Як запустити всі тесты?**
   - A: `pytest`

2. **Як запустити з детальним виводом?**
   - A: `pytest -v`

3. **Як запустити мінімальний вивід?**
   - A: `pytest -q`

4. **Як запустити один файл?**
   - A: `pytest tests/test_file.py`

5. **Як запустити один тест?**
   - A: `pytest tests/test_file.py::test_function`

## 🔍 Filtering

6. **Як запустити тесты за ключовим словом?**
   - A: `pytest -k "keyword"`

7. **Як запустити тесты що НЕ містять слово?**
   - A: `pytest -k "not slow"`

8. **Як запустити тільки failed тесты?**
   - A: `pytest --lf`

9. **Як запустити failed перші?**
   - A: `pytest --ff`

## 🛑 Control Execution

10. **Як зупинити на першій помилці?**
    - A: `pytest -x`

11. **Як зупинити після N помилок?**
    - A: `pytest --maxfail=N`

12. **Як показати print() виводи?**
    - A: `pytest -s`

## 🏷️ Markers

13. **Як позначити тест як slow?**
    - A: `@pytest.mark.slow`

14. **Як запустити тільки slow тесты?**
    - A: `pytest -m slow`

15. **Як пропустити тест?**
    - A: `@pytest.mark.skip`

16. **Як позначити тест як очекуємо fail?**
    - A: `@pytest.mark.xfail`

## 📊 Options

17. **Що таке -vv?**
    - A: Дуже детальний вивід

18. **Як показати локальні змінні?**
    - A: `pytest -l`

19. **Як показати найповільніші тесты?**
    - A: `pytest --durations=N`

20. **Як запустити тесты паралельно?**
    - A: `pytest -n auto` (потребує pytest-xdist)

---

**✅ Ready for Lesson 8?**

