# Приклади — Lesson 18: Run by Marker

## Файли

- `conftest.py` — локальна реєстрація маркерів `smoke` / `regression` / `slow`
- `example_1_marked_tests.py` — реальні тести з маркерами; «матеріал» для відбору через `-m` (7 тестів)
- `example_2_selection_logic.py` — чиста функція `select_by_marker`: одиночний маркер та `not` (5 тестів)
- `example_3_marker_expressions.py` — складені вирази `and` / `or` (5 тестів)

## Як працювати

1. Спершу подивіться на «матеріал» і потренуйте справжні команди `-m`:
   ```bash
   pytest example_1_marked_tests.py -m smoke -v
   pytest example_1_marked_tests.py -m "smoke and not slow" -v
   pytest example_1_marked_tests.py -m "smoke or regression" -v
   ```
   Звертайте увагу на рядок `N deselected / M selected` у виводі.

2. Далі — модель відбору чистою функцією (її можна тестувати без запуску pytest):
   ```bash
   pytest example_2_selection_logic.py -v
   pytest example_3_marker_expressions.py -v
   ```

> Порада: `example_2` та `example_3` показують, **як саме** вираз маркера
> перетворюється на набір тестів — без «магії» командного рядка.
