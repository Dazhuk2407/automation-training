# Питання для самоперевірки - Lesson 13: Python typing

## 🎯 Типізація в Python

1. **Динамічна типізація**
   - Що це означає?
   - Як це відрізняється від статичної?
   - Переваги та недоліки?

2. **Type Hints**
   - Синтаксис type hints
   - Для чого вони потрібні?
   - Чи Python їх перевіряє?

3. **Базові типи з type hints**
   - int, str, float, bool
   - Синтаксис для функцій
   - Синтаксис для змінних

4. **Контейнери**
   - List[int], Dict[str, int]
   - Tuple[int, str]
   - Set[int]

5. **Optional типи**
   - Синтаксис Optional[T]
   - Коли використовувати?

## ✅ Практичні завдання

6. **Напишіть функцію з type hints:**
   ```python
   def greet(name: str, age: int) -> str:
       return f"Hello {name}, age {age}"
   ```

7. **Додайте type hints до змінних:**
   ```python
   name: str = "Alice"
   numbers: List[int] = [1, 2, 3]
   ```

8. **Користуйтесь type checker:**
   ```bash
   pip install mypy
   mypy your_file.py
   ```

---

**✅ Коли типізація зрозуміла - Вы завершили Block 1!** 🎉
