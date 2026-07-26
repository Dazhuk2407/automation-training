# Приклади — Lesson 9: Fixture Basics

## Файли

- `example_1_first_fixture.py` — перша фікстура: `@pytest.fixture` + тести, що її використовують (4 тести)
- `example_2_fixture_returns_data.py` — фікстура може повертати будь-що: dict, list, число, об'єкт (5 тестів)
- `example_3_why_fixtures.py` — «до/після»: дублювання setup vs фікстура (усі тести проходять)

## Як працювати

1. Запустіть кожен приклад:
   ```bash
   pytest example_1_first_fixture.py -v
   pytest example_2_fixture_returns_data.py -v
   ```
2. У `example_3_why_fixtures.py` порівняйте два підходи — з дублюванням і з фікстурою:
   ```bash
   pytest example_3_why_fixtures.py -v
   ```
   Зверніть увагу, наскільки менше повторюваного коду у версії з фікстурою.
