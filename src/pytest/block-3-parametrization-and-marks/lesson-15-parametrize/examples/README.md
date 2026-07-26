# Приклади — Lesson 15: Parametrize

## Файли

- `example_1_basic_parametrize.py` — базовий `@pytest.mark.parametrize`: один тест, багато наборів даних (3 тест-функції)
- `example_2_multiple_params.py` — кілька параметрів, кортежі значень (3 тест-функції)
- `example_3_ids.py` — читабельні `ids` для кейсів (3 тест-функції)

## Як працювати

1. Запустіть кожен приклад з `-v` — і зверніть увагу, що **кожен набір даних** стає окремим рядком у звіті:
   ```bash
   pytest example_1_basic_parametrize.py -v
   pytest example_2_multiple_params.py -v
   ```
2. У `example_3_ids.py` порівняйте вивід тестів з `ids` та без них:
   ```bash
   pytest example_3_ids.py -v
   ```
   Побачите різницю між `test_email_validation[valid_user]` та автозгенерованим `test_login[alice-1234]`.

## Що помітити

- Один параметризований тест у звіті розгортається в кілька кейсів: `test_square[2-4]`, `test_square[3-9]`, ...
- Якщо один кейс впаде — інші все одно виконаються.
- `ids` роблять звіт самодокументованим.
