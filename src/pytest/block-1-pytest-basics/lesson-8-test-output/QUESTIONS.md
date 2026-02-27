# Questions - Lesson 8: Understanding Test Output

## 🎯 Test Status Symbols

1. **Що означає `.` у виводі?**
   - A: PASSED тест

2. **Що означає `F` у виводі?**
   - A: FAILED тест

3. **Що означає `E` у виводі?**
   - A: ERROR (виключення)

4. **Що означає `s` у виводі?**
   - A: SKIPPED тест

5. **Що означає `x` у виводі?**
   - A: XFAIL (expected fail)

## 📊 Output Format

6. **Що показує процент у дужках?**
   - A: Прогрес (скільки тестів завершено)

7. **Як читати: `test_example.py::test_func FAILED`?**
   - A: Тест `test_func` в файлі `test_example.py` впав

8. **Як отримати детальну інформацію про fail?**
   - A: `pytest -v` або `pytest -vv`

## 🔍 Tracebacks

9. **Де знаходиться лінія помилки в traceback?**
   - A: Позначена `>` перед рядком коду

10. **Що означає повідомлення з `E` на початку?**
    - A: Причина помилки

11. **Як отримати коротке трасування?**
    - A: `pytest --tb=short`

12. **Як отримати без трасування?**
    - A: `pytest --tb=no`

## 💻 Print Output

13. **Чому print() не показується за замовчуванням?**
    - A: Pytest придушує їх для чистоти виводу

14. **Як показати print() виводи?**
    - A: `pytest -s`

15. **Де знаходиться print() вивід у тесті?**
    - A: Виводиться перед assertion тесту

## ⚠️ Error Analysis

16. **Що таке AssertionError?**
    - A: Помилка коли assert умова False

17. **Що таке ZeroDivisionError?**
    - A: Помилка при діленні на нуль

18. **Як знайти рядок де тест впав?**
    - A: Шукати файл та номер рядка в traceback

19. **Чи виконується код після failed assertion?**
    - A: Ні, виконання зупиняється

20. **Як отримати локальні змінні при помилці?**
    - A: `pytest -l` (show local variables)

## 📈 Test Summary

21. **Як читати: `5 passed, 2 failed, 1 skipped`?**
    - A: 5 тестів пройшло, 2 впало, 1 пропущено

22. **Що означає `in 0.25s`?**
    - A: Час виконання всіх тестів

23. **Як отримати час кожного тесту?**
    - A: `pytest --durations=10`

24. **Яким exit code=0?**
    - A: Коли всі тесты пройшли

25. **Яким exit code=1?**
    - A: Коли є failed тесты

---

**✅ You've completed Pytest Block 1!**

