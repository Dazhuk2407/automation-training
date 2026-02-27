# Questions - Lesson 5: Simple Tests

## 🎯 Testing Numbers

1. **Як тестувати що 5 > 3?**
   - A: `assert 5 > 3`

2. **Чому 0.1 + 0.2 != 0.3 в Python?**
   - A: Float precision issue, потрібно використовувати tolerance або pytest.approx()

3. **Як тестувати float з tolerance?**
   - A: `assert abs(result - expected) < 0.0001`

4. **Якій результат 10 // 3?**
   - A: 3 (ціле ділення)

5. **Як тестувати модуль (остача)?**
   - A: `assert 10 % 3 == 1`

## 📝 Testing Strings

6. **Як тестувати що рядок містить підрядок?**
   - A: `assert "test" in "pytest"`

7. **Як тестувати case insensitive?**
   - A: `assert "hello".lower() == "test".lower()`

8. **Як тестувати початок рядка?**
   - A: `assert "pytest".startswith("py")`

9. **Чи є рядки мutable?**
   - A: Ні, рядки immutable

10. **Як отримати першу букву рядка?**
    - A: `text[0]` або `text[:1]`

## 📊 Testing Collections

11. **Як тестувати довжину списку?**
    - A: `assert len([1, 2, 3]) == 3`

12. **Як отримати останній елемент списку?**
    - A: `list[-1]` або `list[len(list)-1]`

13. **Що повертає list[1:3]?**
    - A: Елементи з індексом 1 та 2

14. **Чи можна змінювати список після тесту?**
    - A: Так, але це впливає на сам список

15. **Як тестувати що словник має ключ?**
    - A: `assert "key" in dict`

16. **Чим списки відрізняються від кортежів?**
    - A: Списки mutable, кортежи immutable

17. **Як видалити дублікати зі списку?**
    - A: `set(list)` або `list(set(list))`

18. **Як сортувати список?**
    - A: `sorted(list)` (повертає новий) або `list.sort()` (in-place)

19. **Чи можна мати список списків?**
    - A: Так, `[[1,2], [3,4]]` - nested structures

20. **Як отримати доступ до елементу в nested list?**
    - A: `matrix[0][1]` - індекс рядку, потім елементу

---

## 🎓 Practical Understanding

21. **Який результат порожнього списку в boolean контексті?**
    - A: False (всі порожні колекції це False)

22. **Як перевірити що список НЕ містить елемент?**
    - A: `assert element not in list`

23. **Можна ли сортувати список зі змішаними типами?**
    - A: У Python 3 - ні, буде TypeError

24. **Як отримати ключи словника як список?**
    - A: `list(dict.keys())`

25. **Як отримати значення словника за ключем який може не існувати?**
    - A: `dict.get("key", default_value)`

---

**✅ Ready for Lesson 6?**

