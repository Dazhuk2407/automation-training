# Приклади — Lesson 10: Using Fixtures

## Файли

- `example_1_fixture_as_param.py` — фікстура як параметр тесту та незалежність тестів (5 тестів)
- `example_2_multiple_fixtures.py` — кілька фікстур в одному тесті (4 тести)
- `example_3_fixture_using_fixture.py` — фікстура, що залежить від іншої фікстури (ланцюг `config` → `client`) (4 тести)

## Як працювати

1. Запустіть кожен приклад:
   ```bash
   pytest example_1_fixture_as_param.py -v
   pytest example_2_multiple_fixtures.py -v
   pytest example_3_fixture_using_fixture.py -v
   ```
2. Зверніть увагу у `example_1`, як кожен тест отримує **свіжий** результат фікстури.
3. У `example_3` подивіться, як `client` будується на основі `config` — це ланцюг фікстур.
