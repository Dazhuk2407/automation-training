# Питання для самоперевірки - Lesson 12: Python typing

## 🎯 Основи type hints

1. **Навіщо потрібні type hints?**
   - Чи Python перевіряє type hints під час виконання?
   - Які три переваги дають type hints? (документація, IDE, статичний аналіз)
   - Чому type hints — це НЕ runtime validation?

2. **Базовий синтаксис**
   - Як додати type hints до параметрів функції?
   - Як вказати тип повернення?
   - Що означає `-> None`?

## 📦 Контейнерні типи

3. **List, Dict, Tuple, Set**
   - Як типізувати список цілих чисел?
   - Чим `Tuple[int, str]` відрізняється від `List[int]`? (фіксована довжина vs змінна)
   - Як типізувати словник з рядковими ключами та числовими значеннями?

## 🔍 Optional, Union, Any

4. **Optional**
   - Що означає `Optional[str]`?
   - Чим `Optional[str]` відрізняється від просто `str`?
   - Коли функція має повертати `Optional`?

5. **Union vs Any**
   - Чим `Union[int, float]` відрізняється від `Any`?
   - Чому `Any` зменшує користь від type checking?
   - Коли `Any` все ж таки доречний?

6. **Callable**
   - Що означає `Callable[[int], str]`?
   - Як типізувати функцію, яка приймає іншу функцію як параметр?

## 🧠 Питання на розуміння

7. **Чому цей код працює без помилки?**
   ```python
   def add(x: int, y: int) -> int:
       return x + y

   add("hello", "world")  # Працює! Чому?
   ```

8. **Що знайде mypy, а що ні?**
   - mypy знайде: невідповідність типу аргументу
   - mypy НЕ знайде: логічну помилку, баг у runtime, некоректні дані з API

9. **Чому `bool("False")` дає `True`, навіть якщо type hint каже `-> bool`?**

## ✅ Практичні завдання

10. **Додайте type hints:**
    ```python
    def calculate_average(numbers):
        return sum(numbers) / len(numbers)
    ```

11. **Що не так з цим кодом з точки зору mypy?**
    ```python
    def find_user(user_id: int) -> str:
        users = {1: "Alice", 2: "Bob"}
        return users.get(user_id)  # Може повернути None!
    ```

---

**✅ Коли типізація зрозуміла — Ви завершили Block 1!** 🎉