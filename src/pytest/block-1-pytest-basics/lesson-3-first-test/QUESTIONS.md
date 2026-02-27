# Questions - Lesson 3: First Test File

## 🎯 Basic Concepts

1. **Як має називатися тестовий файл?**
   - A: `test_*.py` або `*_test.py`

2. **Як має називатися тестова функція?**
   - A: Починатися з `test_`

3. **Що робить `assert`?**
   - A: Перевіряє умову, якщо False - тест fails

4. **Як запустити тести в файлі?**
   - A: `pytest test_file.py`

5. **Що означає PASSED у виводі?**
   - A: Тест успішно пройшов

## 🧪 Writing Tests

6. **Напишіть простий тест що 5 > 3:**
   ```python
   def test_comparison():
       assert 5 > 3
   ```

7. **Як перевірити що список не порожній?**
   ```python
   assert len(my_list) > 0
   # або
   assert my_list
   ```

8. **Як перевірити що рядок містить підрядок?**
   ```python
   assert "test" in "pytest"
   ```

## 📊 Test Results

9. **Скільки assertions може бути в одному тесті?**
   - A: Необмежено, але краще 1-3

10. **Що станеться якщо перший assert провалиться?**
    - A: Тест зупиниться, наступні assertions не виконаються

---

**✅ Ready for Lesson 4?**
