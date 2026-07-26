# Приклади — Lesson 12: Fixture Scopes

## Файли

- `example_1_function_scope.py` — function scope (default): нова фікстура для кожного тесту, setup виконується 3 рази (4 тести)
- `example_2_module_scope.py` — module scope: одна фікстура на весь файл, setup виконується 1 раз (4 тести)
- `example_3_scope_compare.py` — порівняння function/class/module в одному файлі з лічильниками setup (4 тести)

## Як працювати

1. Запустіть кожен приклад і подивіться на значення лічильників:
   ```bash
   pytest example_1_function_scope.py -v
   pytest example_2_module_scope.py -v
   pytest example_3_scope_compare.py -v
   ```
2. Зверніть увагу, як `function`-фікстура створюється заново для кожного тесту,
   а `module`/`class` — переви­користовуються.
3. У `example_3_scope_compare.py` порівняйте, скільки разів виконався setup
   кожної фікстури для 3 тестів.
