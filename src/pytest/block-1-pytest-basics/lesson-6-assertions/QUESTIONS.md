# Questions - Lesson 6: Assertions

## 🎯 Basic Assertions

1. **Як написати простий assert?**
   - A: `assert condition`

2. **Як додати повідомлення до assert?**
   - A: `assert condition, "message"`

3. **Що робить `assert False`?**
   - A: Тест fails з AssertionError

4. **Чи можна мати кілька assertions в одному тесті?**
   - A: Так, але краще один assert = один тест

5. **Що станеться якщо перший assert fails?**
   - A: Тест зупиниться, інші не виконаються

## 📊 Comparison Assertions

6. **Як тестувати рівність?**
   - A: `assert x == y`

7. **Як тестувати нерівність?**
   - A: `assert x != y`

8. **Яка різниця між `is` та `==`?**
   - A: `==` - рівність значень, `is` - ідентичність об'єктів

9. **Як тестувати що x більше y?**
   - A: `assert x > y`

10. **Як тестувати числові порівняння?**
    - A: Використовувати `<`, `>`, `<=`, `>=`

## 🔍 Membership Assertions

11. **Як тестувати що елемент в списку?**
    - A: `assert element in list`

12. **Як тестувати що елемента немає?**
    - A: `assert element not in collection`

13. **Як тестувати що рядок містить підрядок?**
    - A: `assert "sub" in "substring"`

14. **Як тестувати що словник має ключ?**
    - A: `assert "key" in dict`

15. **Чи можна перевіряти значення в словнику?**
    - A: Так, але це менш оптимально

## 🏷️ Type Assertions

16. **Як перевірити тип змінної?**
    - A: `assert isinstance(x, type)`

17. **Як перевірити кілька типів одночасно?**
    - A: `assert isinstance(x, (int, float))`

18. **Це вірна перевірка типу?** `assert type(x) == int`
    - A: Так, але `isinstance()` краще

## ⚠️ Exception Assertions

19. **Як тестувати що функція викидає виключення?**
    - A: `with pytest.raises(ExceptionType):` `function()`

20. **Як перевірити повідомлення виключення?**
    - A: `with pytest.raises(ValueError, match="pattern"):`

21. **Що означає `match` в pytest.raises?**
    - A: Регулярний вираз для перевірки повідомлення

22. **Як тестувати ZeroDivisionError?**
    - A: `with pytest.raises(ZeroDivisionError):` `10 / 0`

## 🔢 Float Assertions

23. **Чому 0.1 + 0.2 != 0.3 в Python?**
    - A: Float precision issues в двійковій арифметиці

24. **Як правильно тестувати float?**
    - A: `assert result == pytest.approx(expected)`

25. **Що таке pytest.approx()?**
    - A: Функція для тестування float з tolerance

26. **Як встановити абсолютну точність?**
    - A: `pytest.approx(value, abs=0.0001)`

27. **Як встановити відносну точність?**
    - A: `pytest.approx(value, rel=1e-5)`

---

**✅ Ready for Lesson 7?**

