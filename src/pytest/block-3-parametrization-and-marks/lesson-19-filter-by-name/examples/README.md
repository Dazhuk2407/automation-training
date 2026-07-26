# Приклади — Lesson 19: Filter by Name

## Файли

- `example_1_named_tests.py` — реальні тести зі змістовними іменами (`test_login_valid`, `test_login_invalid`, `test_logout`, ...) — матеріал, на якому зручно тренувати `-k` (6 тестів)
- `example_2_k_logic.py` — чиста функція `select_by_name`, що **симулює** відбір `-k` за підрядком та простими виразами; тести перевіряють логіку (5 тестів)
- `example_3_k_expressions.py` — та сама функція на складніших виразах: `and`, `or`, `not`, комбінації (6 тестів)

## Як працювати

1. Прогоніть приклади:
   ```bash
   pytest example_1_named_tests.py -v
   pytest example_2_k_logic.py -v
   pytest example_3_k_expressions.py -v
   ```

2. Потренуйте **справжній** `-k` на першому файлі (ці команди виконуються, на відміну від симуляції):
   ```bash
   pytest example_1_named_tests.py -k login -v
   pytest example_1_named_tests.py -k "login and not invalid" -v
   pytest example_1_named_tests.py -k "login or logout" -v
   ```
   Порівняйте, кого pytest **selected**, а кого **deselected**.

3. У `example_2` / `example_3` подивіться, як та сама логіка `-k` виражена звичайним Python-кодом — це допомагає зрозуміти, що робить pytest під капотом.
